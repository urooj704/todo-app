# Deploy Backend on Hugging Face (Docker Space)

## 1. Create a new Space
- Space SDK: `Docker`
- Visibility: your choice (public/private)

## 2. Upload backend files
Use the `backend/` directory as the Space repository root.

## 3. Set Space Variables/Secrets
Set these in Space settings:

- `DATABASE_URL`
- `BETTER_AUTH_SECRET`
- `BETTER_AUTH_URL`
- `CORS_ORIGINS`
- `GEMINI_API_KEY`
- `GROK_API_KEY`
- `GEMINI_MODEL` (optional, default is `gemini-2.0-flash`)
- `GROK_MODEL` (optional, default is `grok-2-latest`)
- `MAX_CONVERSATION_HISTORY` (optional, default `50`)
- `PORT` (set to `7860`)

## 4. Public backend URL
After deployment, your API base URL is:
- `https://<your-space-subdomain>.hf.space/api`

## 5. Connect frontend
Set frontend env on Vercel:
- `NEXT_PUBLIC_API_URL=https://<your-space-subdomain>.hf.space/api`
