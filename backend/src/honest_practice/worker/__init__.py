"""Background process.

Phase 0 keeps a process alive and logs a heartbeat, so Docker Compose has a
worker service to attach the scheduler to. Phase 5 replaces the idle loop
with APScheduler and the Procrastinate queue. The worker must not import
the API package.
"""
