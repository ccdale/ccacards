import tomllib
from pathlib import Path

from ccacards import __appname__, __version__, getAppname, getVersion
import ccacards


def _project_metadata() -> tuple[str, str]:
    with (Path(__file__).resolve().parents[1] / "pyproject.toml").open("rb") as handle:
        project = tomllib.load(handle)["project"]
    return project["name"], project["version"]


def test_version():
    expected_name, expected_version = _project_metadata()
    assert __version__ == expected_version
    assert getVersion() == expected_version
    assert __appname__ == expected_name
    assert getAppname() == expected_name


def test_metadata_fallback_when_pyproject_missing(monkeypatch):
    monkeypatch.setattr(ccacards, "_find_pyproject", lambda _start: None)
    assert ccacards.getAppname() == "ccacards"
    assert ccacards.getVersion() == "0.0.0"


def test_metadata_fallback_when_toml_load_fails(monkeypatch):
    pyproject = Path(__file__).resolve().parents[1] / "pyproject.toml"

    def _raise(_handle):
        raise ValueError("bad toml")

    monkeypatch.setattr(ccacards, "_find_pyproject", lambda _start: pyproject)
    monkeypatch.setattr(ccacards.tomllib, "load", _raise)
    assert ccacards.getAppname() == "ccacards"
    assert ccacards.getVersion() == "0.0.0"
