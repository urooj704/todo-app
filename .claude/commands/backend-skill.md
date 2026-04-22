---
description: Build backend routes, handle requests and responses, and connect application logic to the database.
handoffs:
  - label: Design Database Schema
    agent: neon-database-architect
    prompt: Design the database schema to support the backend routes and data requirements.
  - label: Implement API Endpoints
    agent: fastapi-backend
    prompt: Implement the API endpoints with proper validation and error handling.
  - label: Add Authentication
    agent: auth-security
    prompt: Add authentication and authorization to protect the backend routes.
---

# Backend Skill

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Instructions

### 1. Route Generation

- Define RESTful routes clearly
- Use proper HTTP methods (GET, POST, PUT, DELETE)
- Organize routes by feature or resource
- Apply consistent naming conventions

### 2. Request Handling

- Parse and validate incoming requests
- Enforce required fields and data types
- Sanitize inputs to prevent abuse
- Handle edge cases gracefully

### 3. Response Handling

- Return structured and consistent responses
- Use correct HTTP status codes
- Provide meaningful error messages
- Avoid leaking internal details

### 4. Database Connectivity

- Connect backend routes to database operations
- Use transactions for multi-step operations
- Handle query failures safely
- Separate data access from route logic

### 5. Auth & Middleware Integration

- Protect routes with authentication where required
- Apply authorization checks
- Use middleware/dependencies cleanly
- Keep cross-cutting concerns centralized

## Best Practices

- Keep routes thin and services thick
- Validate everything at the boundary
- Use async/non-blocking I/O where possible
- Maintain clear separation of concerns
- Log errors consistently
- Follow backend framework conventions

## Example Structure (Pseudocode)

```ts
GET /todos
  -> authenticate request
  -> fetch todos from database
  -> return 200 with data

POST /todos
  -> validate request body
  -> insert record into database
  -> return 201 with created resource
```

## Execution Steps

1. **Analyze Requirements**: Review $ARGUMENTS to understand the API needs.

2. **Check Existing Routes**: Search for existing route definitions and patterns.

3. **Design API Contract**: Based on requirements, design:
   - Endpoint paths and methods
   - Request/response schemas
   - Error responses
   - Authentication requirements

4. **Create Route Handlers**:
   - Define route functions
   - Add request validation (Pydantic schemas, etc.)
   - Implement business logic
   - Connect to database layer

5. **Add Middleware/Dependencies**:
   - Authentication checks
   - Authorization guards
   - Request logging
   - Error handling

6. **Implement Response Handling**:
   - Consistent response format
   - Proper status codes
   - Error serialization

7. **Test Endpoints**: Verify routes handle:
   - Valid requests
   - Invalid inputs
   - Authentication failures
   - Database errors

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent-native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3-7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` -> `history/prompts/constitution/`
     - Feature stages -> `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` -> `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent-native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/...`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.
