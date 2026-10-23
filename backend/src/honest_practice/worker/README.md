"""Background worker.

Phase 0 is an idle process with a heartbeat. Phase 5 adds the scheduler,
the job queue, ``TriggerService``, and the job registry. Run it with
``python -m honest_practice.worker``.
"""
