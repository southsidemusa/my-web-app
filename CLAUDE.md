# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt

# Run dev server (auto-reload)
uvicorn app.main:app --reload

# Run all tests
pytest

# Run a single test
pytest tests/test_main.py::test_root
```

## Architecture

This is a FastAPI application with the following structure:

- `app/main.py` — app entry point; creates the `FastAPI` instance and registers routers
- `app/routers/` — one file per resource (e.g. `items.py`); each exports an `APIRouter` that is included in `main.py`
- `tests/` — pytest tests using FastAPI's `TestClient` (from `httpx`)

**Adding a new resource:** create `app/routers/<name>.py`, define an `APIRouter`, then include it in `app/main.py` with `app.include_router(...)`.

Interactive API docs are served at `http://localhost:8000/docs` when the dev server is running.
