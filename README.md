# RMOS Monorepo

Production-ready starter monorepo for:

- **FastAPI** backend
- **Next.js** frontend
- **Docker** local/prod setup
- **GitHub Actions** CI

## Project structure

```text
.
├── backend
│   ├── app
│   │   ├── api
│   │   │   └── health.py
│   │   ├── core
│   │   │   └── config.py
│   │   └── main.py
│   ├── tests
│   │   └── test_health.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── requirements-dev.txt
├── frontend
│   ├── app
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── Dockerfile
│   ├── next.config.js
│   ├── package.json
│   └── tsconfig.json
├── .github/workflows/ci.yml
├── docker-compose.yml
└── Makefile
```

## Quick start (local)

### 1) Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 2) Frontend

```bash
cd frontend
npm install
npm run dev
```

### 3) Docker Compose

```bash
docker compose up --build
```

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API docs: http://localhost:8000/docs

## Environment variables

Copy `.env.example` to `.env` and update values.
