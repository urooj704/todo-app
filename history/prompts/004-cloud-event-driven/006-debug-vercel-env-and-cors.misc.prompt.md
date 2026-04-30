---
id: 006
title: Debug Vercel env and CORS
stage: misc
date: 2026-04-30
surface: agent
model: GPT-5.2
feature: 004-cloud-event-driven
branch: main
user: king
command: null
labels: ["vercel","env","cors","huggingface","auth"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - C:\Users\king\Desktop\todoo-app\frontend\src\lib\auth.ts
 - C:\Users\king\Desktop\todoo-app\backend\app\config.py
tests:
 - N/A (requires user browser network inspection)
---

## Prompt

DATABASE_URL·Updated about 1 hour ago
 
BETTER_AUTH_SECRET·Updated about 1 hour ago
 
BETTER_AUTH_URL·Updated less than a minute ago
 
CORS_ORIGINS·Updated less than a minute ago
 
GEMINI_API_KEY·Updated about 1 hour ago
 
GROK_API_KEY·Updated about 1 hour ago
 
PORT·Updated about 1 hour ago i added thes api keys and vercel BETTER_AUTH_SECRET
Sensitive
Production and Preview
Added 
3m ago


BETTER_AUTH_URL
Sensitive
Production and Preview
Added 
3m ago


NEXT_PUBLIC_API_URL  i add this plese check why its not working

## Response snapshot

- Identified that frontend auth calls depend on `NEXT_PUBLIC_API_URL` (must include `/api`) and values only apply after redeploy.
- Suspected mismatch between Vercel Preview/Production env selection and deployed URL, or missing CORS allowlist for the Vercel domain on the backend Space.
- Guided user to confirm the exact request URL and CORS errors via browser Network tab.

## Outcome

- ✅ Impact: Provides concrete steps to pinpoint misconfiguration and fix without code changes.
- 🧪 Tests: Pending user verification.
- 📁 Files: No changes.
- 🔁 Next prompts: Verify request URL and update Vercel env + HF `CORS_ORIGINS`, then redeploy.
- 🧠 Reflection: For client-side Next.js, env must be correct at build time; backend must allow frontend origin.

## Evaluation notes (flywheel)

- Failure modes observed: Env set but not redeployed; Preview env not set; missing `/api`; backend CORS origin mismatch.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Add a UI debug banner showing resolved API base URL in non-prod.

