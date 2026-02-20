# my-web-app

A FastAPI web application.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

API docs available at http://localhost:8000/docs

## Test

```bash
pytest
pytest tests/test_main.py::test_root   # single test
```
