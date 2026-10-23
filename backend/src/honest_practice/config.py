"""Process settings, loaded once from the environment.

This module is the only place an environment variable is given a name.
Later phases add fields here instead of calling ``os.environ`` themselves.
Each field's description is the text the environment reference is written
from, and a test fails if a field is missing from that document.

Variables use the ``HP_`` prefix. ``CURSOR_API_KEY`` is the exception: the
Cursor SDK reads that name itself, so the settings model accepts it without
the prefix as well.
"""

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import AliasChoices, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# Names that must never appear in logs. Matched against field names, not values.
_REDACTED_FIELDS = frozenset({"database_url", "cursor_api_key"})


def _env_files() -> tuple[Path, ...]:
    """Return dotenv files that exist, repository root first.

    ``config.py`` lives at ``backend/src/honest_practice/config.py``, so the
    repository root is three parents up and the backend directory is two.
    Docker injects variables directly and ships neither file, which is fine:
    an empty result means "environment only".
    """
    here = Path(__file__).resolve()
    candidates = (here.parents[3] / ".env", here.parents[2] / ".env")
    return tuple(path for path in candidates if path.is_file())


class Settings(BaseSettings):
    """Validated configuration for one API or worker process.

    Attributes:
        environment: ``local`` enables reload-friendly defaults. ``production``
            is what the Phase 12 compose profile sets.
        log_level: Standard library level name, for example ``INFO``.
        api_host: Interface the API binds to inside the container.
        api_port: Port the API binds to inside the container.
        cors_origins: Browser origins allowed to call the API. JSON list.
        database_url: SQLAlchemy URL. The password in it is never logged.
        health_check_database: When true, ``/health`` runs ``SELECT 1`` and
            reports ``degraded`` if Postgres is unreachable.
        cursor_api_key: Credential for the Cursor SDK. Absent until Phase 2
            needs it. Read from ``CURSOR_API_KEY`` or ``HP_CURSOR_API_KEY``.
        cursor_model: Model id passed to the SDK. ``composer-2.5`` is the
            current default; Phase 2 may override it per run.
        cursor_runtime: ``local`` runs the agent on this machine. ``cloud``
            is reserved for a later decision and is rejected by the gateway
            until that decision is recorded.
        agent_sandbox_dir: Working directory given to a local Cursor agent.
            Kept separate from the repository so a run cannot edit this app.
        budget_per_run_usd: Soft cap for one task run. Phase 2 enforces it.
        budget_per_day_usd: Soft cap across a calendar day. A manual run that
            would cross it must be confirmed.
        edition_pattern_count: How many unique patterns one edition publishes.
        worker_heartbeat_seconds: How often the Phase 0 worker logs that it
            is alive. Phase 5 replaces the idle loop with a job queue.
    """

    model_config = SettingsConfigDict(
        env_prefix="HP_",
        env_file=_env_files(),
        extra="ignore",
    )

    environment: Literal["local", "production"] = "local"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"
    api_host: str = "0.0.0.0"
    api_port: int = Field(default=8000, ge=1, le=65535)
    cors_origins: list[str] = Field(default_factory=lambda: ["http://localhost:3000"])
    database_url: str = (
        "postgresql+psycopg://honest_practice:honest_practice@localhost:5432/honest_practice"
    )
    health_check_database: bool = True
    cursor_api_key: SecretStr | None = Field(
        default=None,
        validation_alias=AliasChoices("CURSOR_API_KEY", "HP_CURSOR_API_KEY"),
    )
    cursor_model: str = "composer-2.5"
    cursor_runtime: Literal["local", "cloud"] = "local"
    agent_sandbox_dir: str = "/var/lib/honest-practice/sandbox"
    budget_per_run_usd: float = Field(default=1.0, ge=0)
    budget_per_day_usd: float = Field(default=5.0, ge=0)
    edition_pattern_count: int = Field(default=5, ge=1, le=20)
    worker_heartbeat_seconds: int = Field(default=30, ge=5, le=3600)

    def for_log(self) -> dict[str, str]:
        """Return field values safe to write to a log line.

        Secret fields are replaced with ``set`` or ``unset``. Everything else
        is the display value. Callers should log this mapping instead of
        ``repr(settings)``.
        """
        visible: dict[str, str] = {}
        for name in type(self).model_fields:
            value = getattr(self, name)
            if name in _REDACTED_FIELDS:
                visible[name] = "set" if value else "unset"
                continue
            if isinstance(value, list):
                visible[name] = ",".join(value)
            else:
                visible[name] = str(value)
        return visible


def environment_variable_names() -> dict[str, tuple[str, ...]]:
    """Map each settings field to the environment variable names that set it.

    Fields with an explicit alias use that alias. Every other field uses the
    ``HP_`` prefix plus the upper-case field name. The environment reference
    and its test both call this, so a new field cannot ship without a name.

    Returns:
        Field name to one or more environment variable names.
    """
    names: dict[str, tuple[str, ...]] = {}
    for field_name, field in Settings.model_fields.items():
        alias = field.validation_alias
        if isinstance(alias, AliasChoices):
            choices = alias.choices
            names[field_name] = tuple(str(choice) for choice in choices)
        else:
            names[field_name] = (f"HP_{field_name.upper()}",)
    return names


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the process settings, constructing them on first use.

    Tests that change the environment must call ``get_settings.cache_clear()``
    before the next read. Request handlers should prefer the instance stored
    on ``app.state.settings``, which does not consult this cache.
    """
    return Settings()
