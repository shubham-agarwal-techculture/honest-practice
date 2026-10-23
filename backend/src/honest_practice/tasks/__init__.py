"""Task types and the pipeline runner.

Phase 4 adds ``pattern_edition`` and the checkpointed pipeline. Phase 9 adds
``custom_research``. This package must not import the API or the worker.
The worker will call into this package; the dependency points that way.
"""
