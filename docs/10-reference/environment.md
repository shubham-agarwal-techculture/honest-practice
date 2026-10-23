# Environment variables

The names below come from `environment_variable_names()` in `honest_practice.config`. Adding a field without mentioning its name here fails `tests/test_project.py`.

Defaults are the field defaults. Compose overrides `HP_DATABASE_URL` inside containers. See [configuration](../09-operations/configuration.md).

## Process

| Variable | Default | Purpose |
| --- | --- | --- |
| `HP_ENVIRONMENT` | `local` | `local` or `production`. Production is for the Phase 12 profile. |
| `HP_LOG_LEVEL` | `INFO` | `DEBUG`, `INFO`, `WARNING`, or `ERROR`. |

## API

| Variable | Default | Purpose |
| --- | --- | --- |
| `HP_API_HOST` | `0.0.0.0` | Bind address inside the container. |
| `HP_API_PORT` | `8000` | Bind port inside the container. |
| `HP_CORS_ORIGINS` | `["http://localhost:3000"]` | JSON list of browser origins allowed to call the API. |

## Database

| Variable | Default | Purpose |
| --- | --- | --- |
| `HP_DATABASE_URL` | `postgresql+psycopg://honest_practice:honest_practice@localhost:5432/honest_practice` | SQLAlchemy URL. Never logged. |
| `HP_HEALTH_CHECK_DATABASE` | `true` | When true, `/health` runs `SELECT 1`. |

## Cursor SDK

Used from Phase 2. Present now so the gateway has one place to read them.

| Variable | Default | Purpose |
| --- | --- | --- |
| `CURSOR_API_KEY` | empty | Credential the SDK reads. Also accepted as `HP_CURSOR_API_KEY`. Never logged. |
| `HP_CURSOR_API_KEY` | empty | Same value, prefixed form. |
| `HP_CURSOR_MODEL` | `composer-2.5` | Model id passed to the SDK. |
| `HP_CURSOR_RUNTIME` | `local` | `local` or `cloud`. The gateway will set this explicitly and will not assume a default. |
| `HP_AGENT_SANDBOX_DIR` | `/var/lib/honest-practice/sandbox` | Working directory for a local agent, outside this repository. |

## Budgets and editions

Enforced from Phase 2 and Phase 4. The fields exist so those phases do not invent a second configuration object.

| Variable | Default | Purpose |
| --- | --- | --- |
| `HP_BUDGET_PER_RUN_USD` | `1.0` | Soft cap for one run. |
| `HP_BUDGET_PER_DAY_USD` | `5.0` | Soft cap for a calendar day. A manual run past this cap asks for confirmation. |
| `HP_EDITION_PATTERN_COUNT` | `5` | How many unique patterns one edition publishes. |

## Worker

| Variable | Default | Purpose |
| --- | --- | --- |
| `HP_WORKER_HEARTBEAT_SECONDS` | `30` | How often the Phase 0 worker logs that it is idle. Minimum 5, maximum 3600. |

## Frontend build

Not part of `Settings`. The Next.js image reads it when the image is built.

| Variable | Default | Purpose |
| --- | --- | --- |
| `NEXT_PUBLIC_API_URL` | `http://localhost:8000` | URL the browser uses to call the API. |
