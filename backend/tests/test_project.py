"""Tests that keep the package version and the docs catalogue honest."""

import tomllib
from pathlib import Path

from honest_practice import __version__
from honest_practice.config import environment_variable_names

_REPO_ROOT = Path(__file__).resolve().parents[2]
_BACKEND_ROOT = Path(__file__).resolve().parents[1]


def test_package_version_matches_pyproject() -> None:
    pyproject = tomllib.loads((_BACKEND_ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    assert pyproject["project"]["version"] == __version__


def test_environment_reference_names_every_variable() -> None:
    document = (_REPO_ROOT / "docs" / "10-reference" / "environment.md").read_text(encoding="utf-8")

    for variables in environment_variable_names().values():
        for variable in variables:
            assert f"`{variable}`" in document, variable
