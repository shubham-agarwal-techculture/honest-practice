"""Tests for settings loading and the environment-variable catalogue."""

from honest_practice.config import Settings, environment_variable_names, get_settings


def test_defaults_match_local_development() -> None:
    settings = Settings(_env_file=None)

    assert settings.environment == "local"
    assert settings.api_port == 8000
    assert settings.edition_pattern_count == 5
    assert settings.cursor_model == "composer-2.5"
    assert settings.cursor_api_key is None
    assert settings.health_check_database is True


def test_cursor_api_key_accepts_the_sdk_name(monkeypatch) -> None:
    monkeypatch.setenv("CURSOR_API_KEY", "cursor_test_key")
    settings = Settings(_env_file=None)

    assert settings.cursor_api_key is not None
    assert settings.cursor_api_key.get_secret_value() == "cursor_test_key"


def test_hp_prefix_overrides_a_field(monkeypatch) -> None:
    monkeypatch.setenv("HP_EDITION_PATTERN_COUNT", "7")
    monkeypatch.setenv("HP_ENVIRONMENT", "production")
    settings = Settings(_env_file=None)

    assert settings.edition_pattern_count == 7
    assert settings.environment == "production"


def test_for_log_hides_secrets(monkeypatch) -> None:
    monkeypatch.setenv("CURSOR_API_KEY", "cursor_test_key")
    settings = Settings(_env_file=None)
    logged = settings.for_log()

    assert logged["cursor_api_key"] == "set"
    assert "cursor_test_key" not in " ".join(logged.values())
    assert "honest_practice:" not in logged["database_url"]
    assert logged["database_url"] == "set"


def test_unset_secret_is_labelled(monkeypatch) -> None:
    monkeypatch.delenv("CURSOR_API_KEY", raising=False)
    monkeypatch.delenv("HP_CURSOR_API_KEY", raising=False)
    logged = Settings(_env_file=None).for_log()

    assert logged["cursor_api_key"] == "unset"


def test_every_field_has_an_environment_name() -> None:
    names = environment_variable_names()

    assert set(names) == set(Settings.model_fields)
    assert names["cursor_api_key"] == ("CURSOR_API_KEY", "HP_CURSOR_API_KEY")
    assert names["database_url"] == ("HP_DATABASE_URL",)


def test_get_settings_reads_the_prefixed_variable(monkeypatch) -> None:
    get_settings.cache_clear()
    monkeypatch.setenv("HP_LOG_LEVEL", "ERROR")
    try:
        assert get_settings().log_level == "ERROR"
    finally:
        get_settings.cache_clear()
