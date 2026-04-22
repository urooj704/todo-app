---
description: Validate inputs, outputs, and data contracts across frontend and backend boundaries.
handoffs:
  - label: Implement Backend Validation
    agent: fastapi-backend
    prompt: Implement Pydantic schemas and request/response validation for the API endpoints.
  - label: Add Frontend Validation
    agent: frontend-nextjs
    prompt: Add client-side validation with Zod or similar to match backend schemas.
---

# Validation Skill

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Instructions

### 1. Input Validation

- Validate all incoming user input
- Enforce required fields and correct data types
- Reject malformed or unexpected data
- Normalize input where necessary

### 2. Request & Response Validation

- Define strict request schemas
- Validate API responses before returning
- Ensure response shape consistency
- Prevent leaking internal or sensitive fields

### 3. Schema Design

- Use schema-based validation (Pydantic, Zod, Yup, etc.)
- Keep schemas centralized and reusable
- Version schemas when contracts change
- Align schemas with database constraints

### 4. Error Handling

- Return clear, user-safe validation errors
- Use structured error formats
- Avoid exposing stack traces or internals
- Map validation errors to correct status codes

### 5. Cross-Layer Consistency

- Ensure frontend and backend validation rules match
- Avoid duplicate logic drifting over time
- Validate data at system boundaries only
- Trust validated data internally

## Best Practices

- Validate early, fail fast
- Never trust client-side validation alone
- Prefer schemas over manual checks
- Keep validation separate from business logic
- Reuse schemas wherever possible
- Be strict on input, flexible on output

## Example Structure (Pseudocode)

```ts
CreateUserSchema:
  email: string (email, required)
  password: string (min 8 chars)

POST /signup
  -> validate request with schema
  -> process request
  -> validate response
  -> return success
```

## Execution Steps

1. **Analyze Requirements**: Review $ARGUMENTS to understand validation needs.

2. **Check Existing Schemas**: Search for existing validation schemas and patterns.

3. **Design Validation Strategy**: Based on requirements, design:
   - Schema definitions
   - Validation rules
   - Error response format
   - Cross-layer alignment

4. **Create Backend Schemas**:
   - Define Pydantic models (or equivalent)
   - Add field constraints
   - Set up custom validators
   - Configure error responses

5. **Create Frontend Schemas**:
   - Define Zod/Yup schemas (or equivalent)
   - Mirror backend validation rules
   - Add client-side error messages
   - Connect to form handling

6. **Implement Error Handling**:
   - Structured error format
   - Field-level error mapping
   - Status code assignment
   - User-friendly messages

7. **Verify Consistency**:
   - Compare frontend and backend rules
   - Test edge cases
   - Ensure no validation drift
   - Document schema contracts

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
