"""Smoke tests for the nrc-to-jpg app.

These tests verify that the most critical functionality of the app works.
They are designed to catch major breakage and ensure basic operations succeed.
"""

import shutil
import subprocess
import sys


def test_import() -> None:
    """Test importing the package."""
    import nrc_to_jpg  # noqa: F401, PLC0415


def test_run_as_module() -> None:
    """Test running the app as a module."""
    result = subprocess.run(
        [sys.executable, "-m", "nrc_to_jpg", "--help"],
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0


def test_run_as_executable() -> None:
    """Test running the app as an executable (i.e. as a `console_script`)."""
    executable = shutil.which("nrc-to-jpg")
    assert executable is not None

    result = subprocess.run(  # noqa: S603
        [executable, "--help"],
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0
