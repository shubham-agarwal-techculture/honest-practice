"""Logging setup shared by the API and the worker.

Format is one line per event: time, level, logger name, message. Secrets are
kept out of messages by logging ``Settings.for_log()`` rather than the
settings object itself.
"""

import logging

from honest_practice.config import Settings


def configure_logging(settings: Settings) -> None:
    """Install a stderr handler at the configured level.

    Calling this twice replaces the previous handler instead of stacking a
    second copy. Uvicorn adds its own handlers when it starts, so the API
    process still shows access logs.

    Args:
        settings: Provides ``log_level``.
    """
    root = logging.getLogger()
    root.setLevel(settings.log_level)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s"))
    root.handlers = [handler]
