# ADR-0001: Stack

- Status: Accepted
- Date: 2026-10-23

## Context

Honest Practice has to do four kinds of work: serve a learner's interface, run a daily pipeline, call the Cursor SDK, and remember years of patterns well enough to refuse duplicates. The pipeline is unattended. The interface is something a person reads every day, so it is a real web app and not a notebook.

The Cursor SDK exists for Python and TypeScript. The person building this chose Python for the backend, local development first, and a documented path onto a VPS later.

## Decision

- Python 3.12, FastAPI, Pydantic v2, and uv for the backend.
- SQLAlchemy 2.0 and Alembic against Postgres 16 with the pgvector image. Vectors are how later phases compare a new pattern with the archive.
- Next.js (App Router) and TypeScript for the frontend, in a pnpm workspace.
- The `cursor-sdk` async client, called from one gateway module. Phase 2 writes that module. The runtime is set explicitly to local.
- Docker Compose for local runs. A production profile with a reverse proxy and single-user authentication is Phase 12, recorded here so the local file does not grow production concerns by accident.

## Consequences

- Two languages. The API schema is the contract between them, which [ADR-0004](0004-openapi-client.md) makes mechanical.
- Postgres is a hard dependency, including for local development. Compose starts it.
- The Python SDK's async client must be the only client in the process. Mixing the sync client and the async client is a known footgun and the gateway will not do it.
- Model calls cost money. Budget fields exist in settings now (`HP_BUDGET_PER_RUN_USD`, `HP_BUDGET_PER_DAY_USD`) so Phase 2 has a place to enforce them.
