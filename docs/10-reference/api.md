# HTTP API

Phase 0 exposes one route. FastAPI also serves its own schema UI at `/docs` and the schema at `/openapi.json`. Those are framework routes, not product routes, and Phase 6 will decide which of them stay available in production.

## `GET /health`

Reports whether the process can serve traffic.

HTTP 200 when every enabled check passed. HTTP 503 when any check failed. The body shape is the same in both cases.

```json
{
  "status": "ok",
  "service": "honest-practice",
  "version": "0.1.0",
  "checks": {
    "api": "ok",
    "database": "ok"
  }
}
```

| Field | Values |
| --- | --- |
| `status` | `ok` or `degraded` |
| `service` | Always `honest-practice` |
| `version` | The backend version in `pyproject.toml` |
| `checks.api` | `ok` when this function ran |
| `checks.database` | `ok`, `skipped`, or `error:` plus an exception class name |

`checks.database` is `skipped` when `HP_HEALTH_CHECK_DATABASE` is false. The error value does not include the database URL.

CORS allows the origins in `HP_CORS_ORIGINS`. The Phase 0 page calls this route from the browser.
