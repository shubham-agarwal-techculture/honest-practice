"""Persistence.

Phase 0 checks that Postgres answers ``SELECT 1``. Tables, Alembic
migrations, and repositories arrive in Phase 1. This package must not
import the API, the worker, or the CLI.
"""
