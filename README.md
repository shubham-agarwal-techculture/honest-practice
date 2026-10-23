# Honest Practice

A daily desk for DSA and system design. The system publishes new patterns from public sources, keeps every edition, and lets you define further tasks of the same kind. You can run any of those tasks by hand.

This repository is at **Phase 0**: the skeleton runs, and the later phases have a place to land. The [documentation](docs/index.md) is the map. The [quickstart](docs/00-start-here/quickstart.md) is how you start it.

```powershell
docker compose -f deploy/docker-compose.yml up --build
```

- Web: <http://localhost:3000>
- API health: <http://localhost:8000/health>

## Layout

| Path | What it is |
| --- | --- |
| `backend/` | Python package `honest_practice`. API, worker, and domain code |
| `frontend/` | pnpm workspace: `web`, `ui`, `api-client` |
| `docs/` | The only copy of the documentation |
| `deploy/` | Docker Compose |

## Decisions worth knowing before you edit

- [One package, checked import boundaries](docs/03-architecture/adr/0002-package-boundaries.md)
- [Postgres is the queue](docs/03-architecture/adr/0003-postgres-queue.md)
- [Memory does not weaken uniqueness](docs/03-architecture/adr/0006-memory-versus-uniqueness.md)
- [One documentation tree](docs/03-architecture/adr/0005-documentation.md)
