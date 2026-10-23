"""Liveness and readiness for the API process.

``/health`` is the only route in Phase 0. A supervisor treats HTTP 200 as
ready and HTTP 503 as not ready. The body always names which check failed
so a human can tell a down database from a down process.
"""

from typing import Literal

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from honest_practice import __version__
from honest_practice.config import Settings
from honest_practice.db.health import check_database

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    """Body returned by ``GET /health``.

    Attributes:
        status: ``ok`` when every enabled check passed, otherwise ``degraded``.
        service: Fixed product name, so a proxy can confirm it hit this app.
        version: Backend version, matching ``pyproject.toml``.
        checks: One entry per check. The value is ``ok``, ``skipped``, or
            ``error:<ExceptionName>``.
    """

    status: Literal["ok", "degraded"]
    service: str
    version: str
    checks: dict[str, str]


def build_health(settings: Settings) -> HealthResponse:
    """Run the enabled checks and fold them into one response.

    The database check is skipped when ``health_check_database`` is false.
    Unit tests use that so they do not need Postgres. Docker leaves it on.

    Args:
        settings: Decides whether the database is contacted, and how.

    Returns:
        A response whose ``status`` is ``degraded`` if any check value starts
        with ``error:``.
    """
    checks: dict[str, str] = {"api": "ok"}
    if settings.health_check_database:
        checks["database"] = check_database(settings.database_url)
    else:
        checks["database"] = "skipped"
    status: Literal["ok", "degraded"] = (
        "degraded" if any(value.startswith("error:") for value in checks.values()) else "ok"
    )
    return HealthResponse(
        status=status,
        service="honest-practice",
        version=__version__,
        checks=checks,
    )


@router.get("/health", response_model=HealthResponse)
def health(request: Request) -> JSONResponse:
    """Report whether this process can serve traffic.

    Args:
        request: Supplies ``app.state.settings``, set by ``create_app``.

    Returns:
        HTTP 200 when the status is ``ok``, and HTTP 503 when it is
        ``degraded``. The body shape is the same in both cases.
    """
    settings: Settings = request.app.state.settings
    body = build_health(settings)
    status_code = 200 if body.status == "ok" else 503
    return JSONResponse(status_code=status_code, content=body.model_dump())
