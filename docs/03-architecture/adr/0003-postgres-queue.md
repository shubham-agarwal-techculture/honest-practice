# ADR-0003: Postgres is the queue

- Status: Accepted
- Date: 2026-10-23

## Context

Scheduled tasks and manual runs need a queue with retries, and a scheduler that reads those schedules. Adding Redis would give a familiar queue and a second service to back up, secure, and explain. The system already requires Postgres. Runs are not high-frequency: a handful of editions a day, plus crawls and the occasional manual trigger.

The product also requires that anything the scheduler can run, a person can run by hand. That is a property of the trigger path, not of the queue technology. It is recorded here so Phase 5 does not grow a second implementation for manual runs.

## Decision

- Procrastinate, which stores jobs in Postgres, is the queue.
- APScheduler reads task rows and asks one `TriggerService` to enqueue a job.
- The API, the CLI, and the web UI call that same service. A run records its trigger: `schedule`, `manual_ui`, `manual_cli`, `api`, or `retry`.
- No Redis in local Compose and none in the production profile.

Phase 5 builds this. Phase 0 only keeps a worker process alive so the Compose service exists.

## Consequences

- One database to back up. Job state is in the same backup as editions.
- Throughput is bounded by Postgres. That is acceptable at this volume. A later record can revisit it if a crawl fan-out proves otherwise.
- The worker must be running for a manual trigger to finish. The API enqueues. It does not do the work inline.
- Schedules and jobs share a failure domain with the database. If Postgres is down, nothing runs, and `/health` says so.
