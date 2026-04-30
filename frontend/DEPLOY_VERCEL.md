# Deploy Frontend on Vercel

## 1. Import project
- Import the repository in Vercel.
- Set **Root Directory** to `frontend`.

## 2. Framework/build
- Framework preset: `Next.js`
- Build command: `npm run build`
- Install command: `npm ci`

## 3. Environment variable
Set:

- `NEXT_PUBLIC_API_URL=https://<your-backend-space-subdomain>.hf.space/api`

## 4. Deploy
After deployment, your frontend URL will be:
- `https://<your-vercel-project>.vercel.app`
