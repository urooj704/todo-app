---
description: Implement secure user authentication including signup, signin, password hashing, JWT tokens, and Better Auth integration.
handoffs:
  - label: Create Database Schema
    agent: neon-database-architect
    prompt: Design the user authentication database schema including users table, sessions, and refresh tokens.
  - label: Build Auth Endpoints
    agent: fastapi-backend
    prompt: Create the authentication API endpoints based on the auth implementation.
---

# Auth Skill

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Instructions

### 1. Signup & Signin

- Implement email/password-based signup
- Secure signin with credential verification
- Prevent duplicate accounts
- Apply rate limiting where applicable

### 2. Password Handling

- Hash passwords using modern algorithms (bcrypt / argon2)
- Never store plaintext passwords
- Use proper salt and cost factors
- Support password verification securely

### 3. JWT Tokens

- Generate short-lived access tokens
- Implement refresh tokens when required
- Validate token signatures and expiration
- Rotate and revoke tokens securely

### 4. Better Auth Integration

- Configure Better Auth correctly
- Use Better Auth abstractions instead of custom hacks
- Integrate with backend route protection
- Align Better Auth with JWT/session strategy

### 5. Validation & Security

- Validate auth inputs (email, password, tokens)
- Enforce strong password rules
- Protect against common auth attacks (OWASP Top 10)
- Ensure secure error responses (no sensitive leaks)

## Best Practices

- Follow OWASP authentication guidelines
- Use HTTPS-only cookies when applicable
- Keep access tokens short-lived
- Separate auth logic from business logic
- Centralize auth configuration
- Avoid reinventing cryptography

## Example Flow (Pseudocode)

```ts
POST /auth/signup
  -> validate email & password
  -> hash password
  -> store user
  -> issue JWT token

POST /auth/signin
  -> validate credentials
  -> verify password hash
  -> issue JWT token

GET /protected-route
  -> verify JWT
  -> allow or deny access
```

## Execution Steps

1. **Analyze Requirements**: Review $ARGUMENTS to understand the specific auth requirements.

2. **Check Existing Auth Code**: Search for any existing authentication implementation.

3. **Design Auth Flow**: Based on requirements, design the authentication flow covering:
   - User registration
   - User login
   - Token management
   - Session handling

4. **Implement Core Components**:
   - Password hashing service
   - JWT token generation and validation
   - User credential verification
   - Session management (if applicable)

5. **Integrate with Database**: Ensure user credentials are stored securely with proper schema.

6. **Add Route Protection**: Implement middleware/guards for protected routes.

7. **Test Security**: Verify implementation against common vulnerabilities.

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
