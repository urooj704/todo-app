<!--
SYNC IMPACT REPORT
==================
Version change: [NEW] → 1.0.0 (Initial Phase II Constitution)

Added sections:
- I. Scope
- II. Architecture
- III. Authentication & Security
- IV. API Rules
- V. Data Rules
- VI. Frontend Rules
- Quality Gates
- Completion Criteria
- Governance

Modified principles: N/A (new constitution)
Removed sections: N/A (new constitution)

Templates requiring updates:
- .specify/templates/plan-template.md ✅ (compatible - Constitution Check section exists)
- .specify/templates/spec-template.md ✅ (compatible - requirements structure aligns)
- .specify/templates/tasks-template.md ✅ (compatible - phase structure supports auth/data tasks)

Follow-up TODOs: None
-->

# Todoo App Constitution — Phase II

## Core Principles

### I. Scope

Phase II defines an authenticated, multi-user Todo web application with basic features only.

**Allowed Features:**
- Create tasks
- Read tasks
- Update tasks
- Delete tasks
- Complete tasks

**Constraints:**
- Phase II scope only — no features beyond those listed above
- Multi-user support is REQUIRED
- Authentication is REQUIRED for all operations

### II. Architecture

The system MUST follow strict layer separation:

| Layer | Responsibility |
|-------|---------------|
| **Frontend** | UI rendering, auth handling, API calls |
| **Backend** | Authorization, business logic, data access |
| **Database** | Persistent storage only |

**Rules:**
- Frontend MUST NOT access database directly
- Backend MUST NOT render UI
- Database MUST NOT contain business logic
- Each layer MUST be independently deployable
- Cross-layer communication MUST use defined APIs only

### III. Authentication & Security

**JWT Requirements:**
- Every API request MUST include a valid JWT
- Missing JWT → 401 Unauthorized
- Invalid JWT → 401 Unauthorized
- Expired JWT → 401 Unauthorized

**Identity Management:**
- User identity MUST be derived exclusively from JWT claims
- User identity MUST NOT be passed via request body, query params, or headers
- Shared secret MUST be stored in `BETTER_AUTH_SECRET` environment variable
- Secret MUST NOT be hardcoded in source code

**Ownership Enforcement:**
- Every data operation MUST verify ownership
- Users MUST NOT access other users' tasks
- Cross-user access attempts MUST return 403 Forbidden
- Ownership check MUST occur before any data mutation

### IV. API Rules

**Protocol:**
- All endpoints MUST be RESTful
- Response format MUST be JSON only
- Content-Type MUST be `application/json`

**HTTP Methods:**
| Method | Purpose |
|--------|---------|
| GET | Read operations |
| POST | Create operations |
| PUT/PATCH | Update operations |
| DELETE | Delete operations |

**Status Codes:**
| Code | Usage |
|------|-------|
| 200 | Successful read/update |
| 201 | Successful create |
| 204 | Successful delete |
| 400 | Invalid request body |
| 401 | Missing/invalid authentication |
| 403 | Forbidden (ownership violation) |
| 404 | Resource not found |
| 500 | Server error |

**Error Handling:**
- All errors MUST return structured JSON with `error` field
- Error messages MUST NOT expose internal details
- Stack traces MUST NOT appear in production responses

### V. Data Rules

**Query Constraints:**
- All database queries MUST be scoped to the authenticated user
- Global queries (unfiltered by user) are FORBIDDEN
- Queries MUST include `user_id` filter derived from JWT

**Ownership Model:**
- Each task MUST belong to exactly one user
- `user_id` foreign key MUST be set on task creation
- `user_id` MUST NOT be modifiable after creation

**Schema Compliance:**
- Database schema MUST be followed exactly
- Ad-hoc columns or tables are FORBIDDEN without schema migration
- All migrations MUST be reversible

### VI. Frontend Rules

**Authentication State:**
- All task views MUST be gated by authentication state
- Unauthenticated users MUST be redirected to login
- Auth state MUST be checked on every protected route

**API Communication:**
- A single API client abstraction MUST be used
- JWT MUST be attached to every API request automatically
- Token refresh MUST be handled transparently

**Responsiveness:**
- UI MUST be responsive (mobile + desktop)
- Breakpoints MUST support common device sizes
- Touch targets MUST be appropriately sized for mobile

## Quality Gates

All code MUST pass these gates before merge:

- [ ] No hardcoded IDs or user identifiers
- [ ] No hardcoded secrets or tokens
- [ ] No hidden state that bypasses authentication
- [ ] No behavior outside this constitution
- [ ] All API endpoints return correct status codes
- [ ] All queries are user-scoped
- [ ] JWT validation on every protected endpoint

## Completion Criteria

Phase II is complete when:

- [ ] Multiple users can register and authenticate
- [ ] Each user accesses only their own tasks
- [ ] All task data is persisted in PostgreSQL
- [ ] All API endpoints are secured with JWT authentication
- [ ] Frontend correctly handles auth state
- [ ] No cross-user data leakage is possible

## Governance

**Amendment Process:**
1. Propose change with rationale
2. Document impact on existing code
3. Update version according to semantic versioning
4. Propagate changes to dependent templates

**Versioning Policy:**
- MAJOR: Backward-incompatible changes (principle removal/redefinition)
- MINOR: New principle or section added
- PATCH: Clarifications or wording fixes

**Compliance:**
- All PRs MUST verify compliance with this constitution
- Code review MUST include constitution checklist verification
- Violations MUST be resolved before merge

## Final Rule

**Anything not explicitly allowed in this constitution is disallowed.**

When in doubt:
1. Check this constitution
2. If not covered, it is not permitted
3. Request a constitution amendment if functionality is needed

---

**Version**: 1.0.0 | **Ratified**: 2026-02-05 | **Last Amended**: 2026-02-05
