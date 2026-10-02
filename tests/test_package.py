import shutil
import subprocess
import sys
import tomllib
from importlib import import_module
from importlib.metadata import version
from pathlib import Path

import pytest


def test_package_is_installed():
    import_module("python_template")
    config = Path(__file__).resolve().parents[1] / "pyproject.toml"
    project = tomllib.loads(config.read_text(encoding="utf-8"))["project"]
    assert version(project["name"]) == project["version"]


@pytest.mark.parametrize("entrypoint", ["module", "console"])
def test_installed_entrypoints(entrypoint):
    if entrypoint == "module":
        command = [sys.executable, "-m", "python_template"]
    else:
        executable = shutil.which("python-template")
        assert executable is not None
        command = [executable]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    assert result.stdout == "Hello, Python!\n"
    assert result.stderr == ""
