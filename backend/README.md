# honest-practice backend

Python package for the Honest Practice API and worker. The HTTP app, the
background worker, and the domain code live in one package. Import boundaries
between those parts are enforced with `import-linter`. See
[module boundaries](../docs/03-architecture/module-boundaries.md).

## Layout

| Path | Owns |
| --- | --- |
| `src/honest_practice/config.py` | The only place environment variables are defined |
| `api/` | FastAPI application |
| `worker/` | Process that will run scheduled and manual jobs (Phase 5) |
| `core/` | Domain models. Must not perform I/O |
| `db/` | Persistence. Repositories arrive in Phase 1 |
| `agents/` | Cursor SDK gateway. Arrives in Phase 2 |
| `sources/` | Web source adapters. Arrive in Phase 3 |
| `memory/` | Memory providers. Arrive in Phase 4 |
| `uniqueness/` | Duplicate detection. Arrives in Phase 4 |
| `tasks/` | Task types and the pipeline runner. Arrive in Phase 4 |
| `cli/` | The `hp` command. Arrives in Phase 5 |

## Local commands

From the repository root:

```powershell
uv sync --directory backend --group dev
uv run --directory backend pytest
uv run --directory backend ruff check src tests
uv run --directory backend ruff format --check src tests
uv run --directory backend mypy
uv run --directory backend lint-imports
uv run --directory backend uvicorn honest_practice.api.app:app --reload --app-dir backend/src
```

`uvicorn --app-dir` is only needed when the package is not installed. `uv run`
installs it, so this is enough:

```powershell
uv run --directory backend uvicorn honest_practice.api.app:app --reload --port 8000
```

Copy `.env.example` to `.env` at the repository root before starting the API
if you want values other than the defaults. The settings loader reads that
file automatically.
