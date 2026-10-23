# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/). Versions match `backend/pyproject.toml` and `honest_practice.__version__`.

## 0.1.0 — 2026-10-23

Phase 0 skeleton.

- Python package `honest_practice` with settings, a `/health` route, and an idle worker.
- Next.js page that reports API health.
- Docker Compose services for Postgres (pgvector), the API, the worker, and the web app.
- Documentation tree, MkDocs site, and architecture decisions 0001–0006.
- CI for lint, types, tests, import boundaries, the docs build, and the frontend.
