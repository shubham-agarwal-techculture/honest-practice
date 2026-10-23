# ADR-0004: Generate the TypeScript client from OpenAPI

- Status: Accepted
- Date: 2026-10-23

## Context

The frontend and the backend are different languages. Hand-written types drift. The health response is small enough to write by hand, and Phase 0 does that, in `@honest-practice/api-client`. The API that follows (editions, tasks, runs, jobs) is not.

FastAPI already publishes an OpenAPI schema.

## Decision

Phase 6 generates `frontend/api-client` from that schema with `openapi-typescript`. CI checks the schema, regenerates the client, and fails if the committed file differs.

Until Phase 6, the hand-written health type is allowed. New endpoints do not get hand-written twins. They wait for the generator, or they arrive in the same change as the generator.

## Consequences

- The schema is a product artifact. Renaming a field is a frontend change, and the diff shows it.
- Generation runs in CI, so a missing Python extra or a changed tool version fails in the open.
- The client package stays free of UI code. The web app imports types and, later, request functions. It does not re-declare responses.
