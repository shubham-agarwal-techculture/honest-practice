"""FastAPI application factory.

``app`` at module level is what uvicorn imports. Tests call ``create_app``
with an explicit ``Settings`` instance so they do not depend on the
developer's environment.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from honest_practice import __version__
from honest_practice.api.health import router as health_router
from honest_practice.config import Settings, get_settings
from honest_practice.logging import configure_logging


def create_app(settings: Settings | None = None) -> FastAPI:
    """Build the API application.

    Args:
        settings: Process configuration. When omitted, the cached settings
            loaded from the environment are used.

    Returns:
        An application with CORS and the health router mounted.
    """
    resolved = settings if settings is not None else get_settings()
    configure_logging(resolved)

    application = FastAPI(
        title="Honest Practice",
        version=__version__,
        summary="Daily DSA and system design practice.",
    )
    application.state.settings = resolved
    application.add_middleware(
        CORSMiddleware,
        allow_origins=resolved.cors_origins,
        allow_credentials=False,
        allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
        allow_headers=["*"],
    )
    application.include_router(health_router)
    return application


app = create_app()
