---
description: Design relational database schemas, create tables, and manage migrations with best practices.
handoffs:
  - label: Implement Database Schema
    agent: neon-database-architect
    prompt: Execute the database design and create the schema with migrations.
  - label: Create Backend Models
    agent: fastapi-backend
    prompt: Create backend models and database interactions based on the schema design.
---

# Database Skill

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Instructions

### 1. Schema Design

- Design normalized relational schemas
- Define clear table responsibilities
- Use appropriate data types
- Apply primary keys and foreign keys correctly

### 2. Table Creation

- Create tables with explicit constraints
- Enforce NOT NULL, UNIQUE, and CHECK constraints
- Add timestamps for auditing where needed
- Design tables to support future scalability

### 3. Migrations

- Create reversible and incremental migrations
- Avoid destructive schema changes without safeguards
- Version and document migrations clearly
- Ensure migrations are safe for production environments

### 4. Indexes & Performance

- Add indexes for frequently queried columns
- Avoid over-indexing
- Optimize for read/write balance
- Use composite indexes when appropriate

### 5. Data Integrity & Safety

- Enforce referential integrity
- Use transactions for multi-step operations
- Prevent orphaned records
- Handle cascading rules explicitly

## Best Practices

- Keep schema simple and explicit
- Prefer constraints over application-level checks
- Use migrations instead of manual schema edits
- Name tables and columns consistently
- Plan schema changes carefully
- Document assumptions in migration files

## Example Structure (SQL)

```sql
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT now()
);

CREATE INDEX idx_users_email ON users(email);
```

## Execution Steps

1. **Analyze Requirements**: Review $ARGUMENTS to understand the data model needs.

2. **Check Existing Schema**: Search for any existing database schema or migrations.

3. **Design Entity Relationships**: Based on requirements, design:
   - Entity definitions
   - Relationships (one-to-one, one-to-many, many-to-many)
   - Cardinality constraints

4. **Define Tables**:
   - Primary keys (UUID vs serial)
   - Foreign key relationships
   - Column types and constraints
   - Default values

5. **Plan Indexes**: Identify columns needing indexes based on:
   - Query patterns
   - Join operations
   - Unique constraints

6. **Create Migration Files**: Generate migration scripts that are:
   - Incremental and versioned
   - Reversible (up/down)
   - Production-safe

7. **Document Schema**: Add comments or documentation for complex relationships.

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
