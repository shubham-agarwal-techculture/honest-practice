# Configuration

Process configuration is the `Settings` class in `backend/src/honest_practice/config.py`. If a value is not a field there, the process does not read it. The names and the descriptions are listed in the [environment reference](../10-reference/environment.md). A test fails when a field is missing from that page.

## Where values come from

1. Environment variables.
2. A `.env` file at the repository root, or `backend/.env` if you keep one there. The repository-root file wins when both exist, because it is listed first. Docker images do not contain either file.
3. The defaults on the field.

Copy `.env.example` to `.env` to start from the defaults in a file you can edit. `.env` is gitignored.

Compose sets `HP_DATABASE_URL` itself for the API and the worker, so those containers talk to the `postgres` service even if your `.env` points at `localhost`.

## Names

Most variables use the prefix `HP_`. The Cursor SDK looks for `CURSOR_API_KEY`, so that name is accepted as well as `HP_CURSOR_API_KEY`.

`HP_CORS_ORIGINS` is a JSON list, for example `["http://localhost:3000"]`.

## Secrets in logs

`database_url` and `cursor_api_key` are redacted. `Settings.for_log()` prints `set` or `unset` for them and never the value. The worker logs that mapping at startup. Do not log `settings` itself.

## Changing a default

Add or edit the field, document the variable in the environment reference, and mention the reason in the field's docstring. The docstring is the explanation a caller of `get_settings()` sees. The reference is the explanation an operator sees.
