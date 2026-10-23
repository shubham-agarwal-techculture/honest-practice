"""Database connectivity check used by ``/health``.

A fresh engine is created for each call and disposed immediately. The API
does not keep a pool in Phase 0, because nothing else talks to Postgres yet.
Phase 1 replaces this with the application's session factory.
"""

import logging

from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL, make_url

logger = logging.getLogger(__name__)

# A down database must fail the probe quickly. Three seconds is enough for a
# local Postgres to accept a connection.
_CONNECT_TIMEOUT_SECONDS = "3"


def check_database(database_url: str) -> str:
    """Run ``SELECT 1`` and report the outcome without raising.

    Connection failure is a normal result here, not an exception for the
    caller. The returned string never includes the URL, because the URL
    contains the database password.

    Args:
        database_url: SQLAlchemy URL, including the driver, for example
            ``postgresql+psycopg://user:pass@host:5432/dbname``.

    Returns:
        ``ok`` when the query succeeds, otherwise ``error:`` plus the
        exception class name.
    """
    engine = create_engine(_with_connect_timeout(database_url), pool_pre_ping=True)
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except Exception as exc:
        logger.warning("database health check failed: %s", type(exc).__name__)
        return f"error:{type(exc).__name__}"
    else:
        return "ok"
    finally:
        engine.dispose()


def _with_connect_timeout(database_url: str) -> URL:
    """Return ``database_url`` with a libpq connect timeout.

    psycopg reads ``connect_timeout`` from the URL query string. Setting it
    here keeps the caller's configured URL unchanged in logs and in settings.

    Args:
        database_url: Original SQLAlchemy URL.

    Returns:
        The same URL with ``connect_timeout`` set.
    """
    parsed = make_url(database_url)
    query = dict(parsed.query)
    query["connect_timeout"] = _CONNECT_TIMEOUT_SECONDS
    return parsed.set(query=query)
