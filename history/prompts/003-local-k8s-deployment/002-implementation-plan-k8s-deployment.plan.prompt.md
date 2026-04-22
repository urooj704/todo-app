---
id: 002
title: Implementation Plan K8s Deployment
stage: plan
date: 2026-02-07
surface: agent
model: claude-opus-4-6
feature: 003-local-k8s-deployment
branch: 003-local-k8s-deployment
user: king
command: /sp.plan
labels: ["kubernetes", "docker", "helm", "minikube", "infrastructure", "planning"]
links:
  spec: specs/003-local-k8s-deployment/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/003-local-k8s-deployment/plan.md
  - specs/003-local-k8s-deployment/research.md
  - specs/003-local-k8s-deployment/data-model.md
  - specs/003-local-k8s-deployment/quickstart.md
  - specs/003-local-k8s-deployment/contracts/helm-values-contract.yaml
  - specs/003-local-k8s-deployment/contracts/docker-build-contract.md
  - specs/003-local-k8s-deployment/contracts/deployment-flow-contract.md
tests:
  - Constitution check — all 11 gates PASSED (pre-design and post-design)
---

## Prompt

/sp.plan with detailed execution strategy for Phase IV: Local Kubernetes Deployment.

User provided a layered execution strategy:
- Phase A: Containerization (Backend + Frontend Dockerfiles)
- Phase B: Local Kubernetes Setup (Minikube cluster + namespace)
- Phase C: Helm Chart Development (chart structure, templates, config, secrets)
- Phase D: Deployment (Helm install + service exposure + validation)
- Phase E: Scaling & Diagnostics (scaling tests + AI DevOps tooling)
- Phase F: Hardening & Validation (restart test, resource review, reproducibility)

## Response snapshot

Generated complete implementation plan with 7 artifacts:

1. **research.md** — 8 technology decisions with rationale and alternatives:
   - R1: Multi-stage Alpine build for Next.js frontend (standalone output)
   - R2: python:3.11-slim for FastAPI backend
   - R3: MCP server as separate K8s Deployment (shared backend image, different entrypoint)
   - R4: `minikube image load` for local image delivery
   - R5: Single Helm chart with sub-templates
   - R6: Conservative resource limits for local dev
   - R7: Both frontend AND backend on NodePort (browser needs direct API access)
   - R8: Secrets via `--set` overrides (never committed)

2. **plan.md** — 5-phase implementation plan (A-E) with:
   - Technical context, constitution check (all PASS), project structure
   - Phase A: Containerization (backend Dockerfile + frontend multi-stage Dockerfile)
   - Phase B: Helm chart (Chart.yaml, values.yaml, 10 templates)
   - Phase C: Deployment & validation
   - Phase D: Scaling & hardening
   - Phase E: AI DevOps integration
   - Risk analysis (4 risks with mitigations)
   - 7 key decisions summarized

3. **data-model.md** — Infrastructure entity model (Docker images, K8s resources, Helm chart, communication flow diagram)

4. **contracts/** — 3 contract files:
   - helm-values-contract.yaml — Complete values structure
   - docker-build-contract.md — Build specs for both images
   - deployment-flow-contract.md — 9-step deployment flow with verification commands

5. **quickstart.md** — 5-command deployment quick reference

Key architectural insight: The MCP server (port 8001) must be a separate Kubernetes Deployment (not sidecar) because the backend agent connects to it via HTTP URL. It shares the `todo-backend:phase4` image with a different entrypoint command (`python -m mcp_server.run`).

## Outcome

- Impact: Complete implementation plan ready for task generation via /sp.tasks
- Tests: Constitution check — all 11 gates PASSED
- Files: 7 artifacts created (plan.md, research.md, data-model.md, quickstart.md, 3 contracts)
- Next prompts: `/sp.tasks` to generate the implementation task list
- Reflection: The user's detailed execution strategy aligned closely with the technical research. The critical discovery was the MCP server needing its own Deployment due to the HTTP-based connection from the backend agent, and the frontend needing NodePort for the backend too since API calls happen client-side in the browser.

## Evaluation notes (flywheel)

- Failure modes observed: None — user execution strategy was well-structured and aligned with best practices
- Graders run and results (PASS/FAIL): Constitution check PASS (11/11 gates), Post-design recheck PASS
- Prompt variant (if applicable): Standard /sp.plan with user-provided execution strategy
- Next experiment (smallest change to try): N/A — proceeding to /sp.tasks
