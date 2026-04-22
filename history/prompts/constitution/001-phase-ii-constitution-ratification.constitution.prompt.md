---
id: 001
title: Phase II Constitution Ratification
stage: constitution
date: 2026-02-05
surface: agent
model: claude-opus-4-5-20251101
feature: none
branch: master
user: king
command: /sp.constitution
labels: ["constitution", "phase-ii", "governance", "auth", "multi-user"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - null
---

## Prompt

/sp.constitution

# Phase II Constitution

## Scope

* Phase II only
* Authenticated, multi-user Todo web app
* Basic features only: create, read, update, delete, complete

---

## Architecture

* Frontend: UI, auth handling, API calls
* Backend: authorization, business logic, data access
* Database: persistent storage only
* Strict separation between layers

---

## Authentication & Security

* Every API request requires a valid JWT
* Missing/invalid JWT → 401
* User identity comes only from JWT
* Shared secret via `BETTER_AUTH_SECRET`
* Ownership enforced on every operation
* Cross-user access is forbidden

---

## API Rules

* RESTful endpoints only
* Correct HTTP methods and status codes
* Explicit error handling
* JSON responses only

---

## Data Rules

* All queries must be user-scoped
* Tasks belong to one user only
* No global or unfiltered queries
* Database schema must be followed exactly

---

## Frontend Rules

* Auth state gates all task views
* Single API client abstraction
* JWT attached to every request
* Responsive UI (mobile + desktop)

---

## Quality Gates

* No hardcoded IDs or secrets
* No hidden state
* No behavior outside this constitution

---

## Completion Criteria

* Multiple users supported safely
* Users access only their own tasks
* Data persisted in PostgreSQL
* All endpoints secured

---

## Final Rule

**Anything not explicitly allowed here is disallowed.**

## Response snapshot

Created Phase II Constitution v1.0.0 for the Todoo App with 6 core principles:

1. **Scope** - Multi-user authenticated Todo app with CRUD + complete operations only
2. **Architecture** - Strict Frontend/Backend/Database layer separation
3. **Authentication & Security** - JWT-based auth, ownership enforcement, BETTER_AUTH_SECRET
4. **API Rules** - RESTful, JSON-only, proper HTTP methods and status codes
5. **Data Rules** - User-scoped queries, single ownership model, schema compliance
6. **Frontend Rules** - Auth-gated views, single API client, responsive design

Plus Quality Gates, Completion Criteria, Governance rules, and Final Rule (deny by default).

## Outcome

- Impact: Established foundational governance for Phase II development
- Tests: N/A (governance document)
- Files: .specify/memory/constitution.md (created/updated)
- Next prompts: /sp.specify to create feature spec, or /sp.plan to begin implementation planning
- Reflection: Clear, testable principles with deny-by-default security posture

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): Standard constitution workflow
- Next experiment (smallest change to try): N/A
