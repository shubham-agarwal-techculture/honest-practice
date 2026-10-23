# Honest Practice

A desk for daily practice. Each day the system publishes five new DSA patterns and five new system design patterns, drawn from public writing on the web, and it refuses to publish a pattern it has already given you. You can read any earlier edition, ask an assistant about a pattern, and define further tasks of the same kind.

This repository is at Phase 0. The API answers `/health`, a worker process stays running, and this page is the map of the documentation that the later phases fill in.

## Read this first

- [Quickstart](00-start-here/quickstart.md) if you want it running on your machine.
- [Reading map](00-start-here/reading-map.md) if you want to know which document answers which question.
- [Decisions](03-architecture/adr/index.md) if you want to know why the stack looks like this.

## What is running today

| Piece | What it does now |
| --- | --- |
| API | `GET /health` reports the process and, when asked, Postgres |
| Worker | Stays alive and logs a heartbeat. The scheduler arrives in Phase 5 |
| Web | One page, "The desk is clear.", plus the API status |
| Docs | This site. One Markdown tree, also rendered inside the app in Phase 8 |

## Status of these docs

Pages that describe behaviour which exists are written as reference. Pages that describe behaviour from a later phase are outlines: they say what the page will decide, and they say which phase writes it. An outline is not a promise that the feature already works.
