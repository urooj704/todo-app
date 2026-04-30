---
id: 005
title: Fix Vercel login Not Found
stage: misc
date: 2026-04-30
surface: agent
model: GPT-5.2
feature: 004-cloud-event-driven
branch: main
user: king
command: null
labels: ["vercel","nextjs","auth","env","404"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - C:\Users\king\Desktop\todoo-app\frontend\src\lib\auth.ts
tests:
 - N/A (requires Vercel env update + redeploy)
---

## Prompt

Not Found yeh likh arha hai when i tried to login in to toodo app on vercel fix this

## Response snapshot

- Determined the UI error "Not Found" matches FastAPI 404 JSON `{ "detail": "Not Found" }` from calling the wrong endpoint base.
- Root cause: Vercel env `NEXT_PUBLIC_API_URL` likely set to `https://ujjee-todoo-app.hf.space` (missing `/api`), so frontend calls `/auth/signin` instead of `/api/auth/signin`.
- Fix: set `NEXT_PUBLIC_API_URL=https://ujjee-todoo-app.hf.space/api` in Vercel and redeploy.

## Outcome

- ✅ Impact: After correcting Vercel env + redeploy, signin/signup should hit the correct backend routes.
- 🧪 Tests: Pending redeploy validation.
- 📁 Files: No code change required; configuration fix only.
- 🔁 Next prompts: Confirm Vercel env var and redeploy; optionally add token persistence to avoid logout on refresh.
- 🧠 Reflection: Prefer strict env validation / runtime banner to catch misconfigured API base URLs early.

## Evaluation notes (flywheel)

- Failure modes observed: Missing `/api` prefix in `NEXT_PUBLIC_API_URL` yields FastAPI 404 detail "Not Found".
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Add a startup check that warns if `NEXT_PUBLIC_API_URL` doesn’t end with `/api`.

