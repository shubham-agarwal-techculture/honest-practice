# ADR-0002: One package, checked boundaries

- Status: Accepted
- Date: 2026-10-23

## Context

The backend has a domain (patterns, editions, tasks), adapters (database, web sources, the Cursor SDK, memory), and two delivery processes (API and worker). Splitting those into separately published Python packages would make the dependency direction obvious and the day-to-day workflow heavier: more lockfiles, more version bumps, more empty packages to release for a solo project.

Leaving them as one package with no rules makes the dependency direction a suggestion.

## Decision

Ship one package, `honest_practice`, laid out by responsibility under `backend/src/honest_practice/`. Encode the allowed imports as `import-linter` contracts in `backend/pyproject.toml`, and fail CI when a contract breaks.

`core` imports no other subpackage. Adapter packages do not import `api`, `worker`, or `cli`. `api` and `worker` do not import each other.

## Consequences

- A new seam is a new subpackage plus a contract, not a new project.
- The linter sees imports, not runtime calls. A boundary can still be violated by reaching through a string import. Reviewers treat that as the same violation.
- Tests may import any package. The contracts apply to `honest_practice` itself.
- The layout is documented in [module boundaries](../module-boundaries.md). That page and the contracts must move together.
