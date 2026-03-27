.PHONY: up down backend-dev frontend-dev test lint

up:
	docker compose up --build

down:
	docker compose down --remove-orphans

backend-dev:
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

frontend-dev:
	cd frontend && npm run dev

test:
	cd backend && pytest

lint:
	cd frontend && npm run lint
