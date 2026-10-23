"""Duplicate detection.

Phase 4 adds the three-stage checker: exact slug, embedding similarity,
then an LLM judge for the borderline band. This package must not import
the API, the worker, or the CLI.
"""
