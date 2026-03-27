import tomllib
from pathlib import Path

import platformdirs


def _find_pyproject(start: Path) -> Path | None:
    """Find pyproject.toml by searching upward from the package location."""
    for parent in (start, *start.parents):
        candidate = parent / "pyproject.toml"
        if candidate.is_file():
            return candidate
    return None


def _load_project_metadata() -> dict[str, str]:
    """Read project name/version from pyproject.toml with safe defaults."""
    default_meta = {"name": "ccacards", "version": "0.0.0"}
    pyproject = _find_pyproject(Path(__file__).resolve().parent)
    if pyproject is None:
        return default_meta
    try:
        with pyproject.open("rb") as handle:
            data = tomllib.load(handle)
        project = data.get("project", {})
        return {
            "name": str(project.get("name", default_meta["name"])),
            "version": str(project.get("version", default_meta["version"])),
        }
    except Exception:
        return default_meta


def getAppname() -> str:
    """Return application name from pyproject.toml."""
    return _load_project_metadata()["name"]


def getVersion() -> str:
    """Return package version from pyproject.toml."""
    return _load_project_metadata()["version"]


__appname__ = getAppname()
__version__ = getVersion()

__carddir__ = platformdirs.user_data_dir(__appname__)
