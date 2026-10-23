"""Idle worker loop used until the scheduler arrives in Phase 5.

The process exits only on ``SIGINT`` or ``SIGTERM``. Docker sends
``SIGTERM`` on ``compose stop``, and the loop returns so the interpreter
can shut down without a timeout kill.
"""

import logging
import signal
import threading
import types

from honest_practice.config import get_settings
from honest_practice.logging import configure_logging

logger = logging.getLogger(__name__)


def main() -> None:
    """Log readiness, then sleep until the process is asked to stop.

    The heartbeat exists so an operator can see the worker is the Phase 0
    placeholder and not a stuck scheduler. The interval comes from
    ``HP_WORKER_HEARTBEAT_SECONDS``.
    """
    settings = get_settings()
    configure_logging(settings)
    stop = threading.Event()

    def _request_stop(signum: int, _frame: types.FrameType | None) -> None:
        logger.info("worker stopping signal=%s", signum)
        stop.set()

    signal.signal(signal.SIGINT, _request_stop)
    signal.signal(signal.SIGTERM, _request_stop)
    logger.info("worker ready (idle until phase 5) %s", settings.for_log())
    while not stop.is_set():
        stop.wait(settings.worker_heartbeat_seconds)
        if not stop.is_set():
            logger.info("worker heartbeat")
    logger.info("worker stopped")
