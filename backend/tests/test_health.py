"""Tests for the health route and the database probe."""

from fastapi.testclient import TestClient

from honest_practice import __version__
from honest_practice.api.app import create_app
from honest_practice.config import Settings
from honest_practice.db.health import check_database


def test_health_skips_the_database_when_disabled() -> None:
    client = TestClient(create_app(Settings(_env_file=None, health_check_database=False)))

    response = client.get("/health")

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["service"] == "honest-practice"
    assert body["version"] == __version__
    assert body["checks"] == {"api": "ok", "database": "skipped"}


def test_health_is_degraded_when_postgres_is_down() -> None:
    settings = Settings(
        _env_file=None,
        health_check_database=True,
        database_url="postgresql+psycopg://honest_practice:honest_practice@127.0.0.1:1/none",
    )
    client = TestClient(create_app(settings))

    response = client.get("/health")

    assert response.status_code == 503
    body = response.json()
    assert body["status"] == "degraded"
    assert body["checks"]["api"] == "ok"
    assert body["checks"]["database"].startswith("error:")
    assert "honest_practice" not in body["checks"]["database"]


def test_check_database_does_not_include_the_url_on_failure() -> None:
    result = check_database("postgresql+psycopg://honest_practice:secret-password@127.0.0.1:1/none")

    assert result.startswith("error:")
    assert "secret-password" not in result
