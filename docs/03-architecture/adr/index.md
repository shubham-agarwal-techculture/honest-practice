# Decisions

An architecture decision record is a short note of a choice and the reason for it. We keep them so a later change can see what it is undoing.

Records are numbered and are not edited to match a new decision. A replacement gets a new number and marks the old one superseded.

| Record | Status | Choice |
| --- | --- | --- |
| [0001](0001-stack.md) | Accepted | Python API, Next.js UI, Postgres with pgvector |
| [0002](0002-package-boundaries.md) | Accepted | One Python package, boundaries checked by import-linter |
| [0003](0003-postgres-queue.md) | Accepted | Queue and schedules in Postgres, no Redis |
| [0004](0004-openapi-client.md) | Accepted | TypeScript client generated from the OpenAPI schema |
| [0005](0005-documentation.md) | Accepted | One Markdown tree, three ways to read it |
| [0006](0006-memory-versus-uniqueness.md) | Accepted | Memory changes context. Uniqueness always uses full history |
