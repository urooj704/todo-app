"""Chat service orchestrating conversation flow with Gemini/Grok inference."""

import httpx
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import get_settings
from app.services.conversation_service import (
    create_conversation,
    get_conversation,
    store_message,
    load_conversation_history,
)
from app.schemas.chat import ChatResponse


class ChatServiceError(Exception):
    """Raised when the chat service encounters an error."""

    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


async def process_chat_message(
    db: AsyncSession,
    user_id: str,
    message: str,
    conversation_id: str | None = None,
) -> ChatResponse:
    """Process a user chat message and return an AI response.

    1. Load or create conversation
    2. Load bounded history
    3. Run agent with history + new message
    4. Persist user and assistant messages
    5. Return response
    """
    settings = get_settings()

    # Load or create conversation
    if conversation_id:
        conversation = await get_conversation(db, conversation_id, user_id)
        if not conversation:
            raise ChatServiceError(
                "Conversation not found or access denied", status_code=403
            )
    else:
        conversation = await create_conversation(db, user_id)

    # Load bounded conversation history
    history_messages = await load_conversation_history(
        db, conversation.id, user_id, limit=settings.max_conversation_history
    )

    # Build bounded prompt from history + new user message
    prompt_parts = [
        "You are a concise, helpful assistant for the Todoo task manager app.",
        "Keep answers practical and short.",
    ]
    for msg in history_messages:
        role = "User" if msg.role == "user" else "Assistant"
        prompt_parts.append(f"{role}: {msg.content}")
    prompt_parts.append(f"User: {message}")
    prompt_parts.append("Assistant:")
    prompt = "\n".join(prompt_parts)

    try:
        response_text = await _generate_ai_response(settings, prompt)
    except Exception as e:
        raise ChatServiceError(
            "The AI service is temporarily unavailable. Please try again in a moment.",
            status_code=502,
        ) from e

    # Persist user message
    await store_message(db, conversation.id, user_id, "user", message)

    # Persist assistant response
    await store_message(db, conversation.id, user_id, "assistant", response_text)

    return ChatResponse(
        conversation_id=conversation.id,
        response=response_text,
        tool_calls=[],
    )


async def _generate_ai_response(settings, prompt: str) -> str:
    """Generate assistant text using Gemini first, then Grok as fallback."""
    if settings.gemini_api_key:
        response = await _call_gemini(
            prompt=prompt,
            api_key=settings.gemini_api_key,
            model=settings.gemini_model,
        )
        if response:
            return response

    if settings.grok_api_key:
        response = await _call_grok(
            prompt=prompt,
            api_key=settings.grok_api_key,
            model=settings.grok_model,
        )
        if response:
            return response

    raise ChatServiceError(
        "No AI provider API key is configured. Set GEMINI_API_KEY or GROK_API_KEY.",
        status_code=503,
    )


async def _call_gemini(prompt: str, api_key: str, model: str) -> str:
    """Call Gemini generateContent API."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.4,
            "maxOutputTokens": 220,
        },
    }
    async with httpx.AsyncClient(timeout=45.0) as client:
        response = await client.post(url, json=payload)
        response.raise_for_status()
        data = response.json()

    candidates = data.get("candidates") or []
    if not candidates:
        return ""
    content = candidates[0].get("content") or {}
    parts = content.get("parts") or []
    texts = [part.get("text", "") for part in parts if isinstance(part, dict)]
    return "\n".join([t for t in texts if t]).strip()


async def _call_grok(prompt: str, api_key: str, model: str) -> str:
    """Call xAI OpenAI-compatible chat completions API."""
    url = "https://api.x.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a concise, helpful task assistant."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.4,
        "max_tokens": 220,
    }
    async with httpx.AsyncClient(timeout=45.0) as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

    choices = data.get("choices") or []
    if not choices:
        return ""
    message = choices[0].get("message") or {}
    content = message.get("content")
    return content.strip() if isinstance(content, str) else ""
