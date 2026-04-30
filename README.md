## Todoo App

Full-stack multi-user todo app.

### Stack

- **Frontend**: Next.js (`frontend/`)
- **Backend**: FastAPI + SQLAlchemy async (`backend/`)
- **Deploy**:
  - Backend on **Hugging Face Spaces (Docker)**
  - Frontend on **Vercel**

### Local development

#### Backend

Create `backend/.env` (see `backend/.env.example`) then run:

```bash
cd backend
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Health check:

- `GET http://localhost:8000/health`

#### Frontend

Create `frontend/.env.local` (see `frontend/.env.local.example`) then run:

```bash
cd frontend
npm ci
npm run dev
```

### Deployment

#### Backend (Hugging Face Spaces)

Follow `backend/DEPLOY_HUGGINGFACE.md`.

Your API base URL will be:

- `https://<your-space-subdomain>.hf.space/api`

#### Frontend (Vercel)

Follow `frontend/DEPLOY_VERCEL.md`.

Key env var on Vercel:

- `NEXT_PUBLIC_API_URL=https://<your-space-subdomain>.hf.space/api`

