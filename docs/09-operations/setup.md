# Setup

Phase 0 runs as four Compose services. Later phases add behaviour inside the same services.

## Services

| Service | Image | Port on the host | Role |
| --- | --- | --- | --- |
| `postgres` | `pgvector/pgvector:pg16` | 5432 | Database. pgvector is unused until embeddings arrive |
| `api` | Built from `backend/Dockerfile` | 8000 | FastAPI. Health check calls `/health` |
| `worker` | Same image, command `python -m honest_practice.worker` | none | Idle heartbeat until Phase 5 |
| `web` | Built from `frontend/Dockerfile` | 3000 | Next.js page |

The Compose project name is `honest-practice`.

```powershell
docker compose -f deploy/docker-compose.yml up --build
```

Stop it with `docker compose -f deploy/docker-compose.yml down`. The database volume `pgdata` survives `down`. `down -v` deletes it.

## Health

The API is healthy when `/health` returns HTTP 200. That requires Postgres to answer `SELECT 1`. Compose waits for `pg_isready` before starting the API, then waits for `/health` before starting the web container.

A failed database check returns HTTP 503 and a body whose `checks.database` is `error:` plus an exception class name. The body does not contain the database URL.

## Tools for local development

| Tool | Version used here | What for |
| --- | --- | --- |
| Python | 3.12 | Backend. `backend/.python-version` pins it for uv |
| uv | 0.9.x | Backend installs and the lockfile |
| Node.js | 22 | Frontend |
| pnpm | 10.21.0, pinned in `frontend/package.json` | Frontend workspace. pnpm 12 rejects the lockfile under its release-age policy |

Commands are in the [quickstart](../00-start-here/quickstart.md).

## What is intentionally absent

- No login. The published ports are for a machine you control. Phase 12 adds authentication before a VPS deploy.
- No Redis, no separate queue process. See [ADR-0003](../03-architecture/adr/0003-postgres-queue.md).
- The worker does not dequeue anything yet.
