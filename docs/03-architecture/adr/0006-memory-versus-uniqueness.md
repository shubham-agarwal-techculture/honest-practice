# ADR-0006: Memory changes context, not uniqueness

- Status: Accepted
- Date: 2026-10-23

## Context

A task can run with memory on or off. On means the agent may see earlier patterns, notes, and study progress. Off means it sees the sources for this run and the task instructions, and nothing from the archive.

The same product promises that a new edition does not repeat a pattern you already have. If "memory off" also meant "do not look at history when deciding what is new", a fresh-start run could republish last month's pattern under a new title. That would make the toggle a way to break the promise.

## Decision

Memory policy chooses the context builder:

- `none` passes no archive context.
- `history_summary` passes a compressed list of past titles, topics, and study progress.
- `vector_retrieval` passes related past patterns and notes.

Uniqueness always runs against the full history of that pattern kind: exact slug, then embedding similarity, then an LLM judge only for the borderline band. The memory setting is not an input to that check.

A manual run may override memory for that run. The override is stored on the run. It is not stored back onto the task, and it does not skip uniqueness.

Phase 4 implements the check. This record exists now so the setting is not designed as a single "use history" flag that means both things.

## Consequences

- "Fresh start" is about the agent's reading, not about amnesia in the archive.
- Uniqueness has to be cheap enough to run on every generation, including dry runs. The LLM judge is limited to the borderline band for that reason.
- The run ledger records the memory policy that was actually used, so a past edition can be explained.
- A bug that wires memory policy into the uniqueness query is a violation of this decision, not a feature.
