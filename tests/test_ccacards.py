import tomllib
from pathlib import Path

from ccacards import __appname__, __version__, getAppname, getVersion


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
