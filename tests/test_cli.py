import datetime as dt
from importlib import import_module, metadata
from pathlib import Path

import pytest
from click.testing import CliRunner

from nrc_to_jpg.cli import cli
from nrc_to_jpg.constants import DEFAULT_OUTPUT_FILE, DEFAULT_OUTPUT_FILE_TEMPLATE

from .utils import run_command_in_shell


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture
def tmp_cwd(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Change the current working directory to a temporary directory."""
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_main_module() -> None:
    """Exercise (most of) the code in the `__main__` module."""
    import_module("nrc_to_jpg.__main__")


def test_run_as_module() -> None:
    """Is the script runnable as a Python module?"""
    result = run_command_in_shell("python -m nrc_to_jpg --help")
    assert result.exit_code == 0


def test_run_as_executable() -> None:
    """Is the script installed (as a `console_script`) and runnable as an executable?"""
    result = run_command_in_shell("nrc-to-jpg --help")
    assert result.exit_code == 0


def test_version_runner(runner: CliRunner) -> None:
    """Does `--version` display the correct version?"""
    version = metadata.version("nrc-to-jpg")
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"cli, version {version}\n"


@pytest.mark.usefixtures("tmp_cwd")
def test_default(runner: CliRunner) -> None:
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert DEFAULT_OUTPUT_FILE.is_file()


@pytest.mark.usefixtures("tmp_cwd")
def test_date(runner: CliRunner) -> None:
    date_ = dt.date(2001, 9, 12)
    result = runner.invoke(cli, ["--date", date_.isoformat()])
    assert result.exit_code == 0
    assert Path(
        DEFAULT_OUTPUT_FILE_TEMPLATE.format(
            year=date_.year, month=date_.month, day=date_.day
        )
    ).is_file()


@pytest.mark.usefixtures("tmp_cwd")
def test_sunday(runner: CliRunner) -> None:
    date_ = dt.date(2024, 6, 9)
    result = runner.invoke(cli, ["--date", date_.isoformat()])
    assert result.exit_code == 1
    assert result.output.startswith("You are trying to get the newspaper for a Sunday.")


@pytest.mark.usefixtures("tmp_cwd")
def test_page_number(runner: CliRunner) -> None:
    page_number = 2
    result = runner.invoke(cli, ["--page-number", str(page_number)])
    assert result.exit_code == 0
    assert DEFAULT_OUTPUT_FILE.is_file()


@pytest.mark.usefixtures("tmp_cwd")
def test_odd_non_first_page_number(runner: CliRunner) -> None:
    page_number = 3
    result = runner.invoke(cli, ["--page-number", str(page_number)])
    assert result.exit_code == 0
    assert not DEFAULT_OUTPUT_FILE.is_file()
    assert result.output == f"Could not find page {page_number}.\n"


@pytest.mark.usefixtures("tmp_cwd")
def test_output_template(runner: CliRunner) -> None:
    output_template = "NRC.jpg"
    result = runner.invoke(cli, ["--output", output_template])
    assert result.exit_code == 0
    assert Path(output_template).is_file()


@pytest.mark.usefixtures("tmp_cwd")
def test_output_template_with_invalid_field(runner: CliRunner) -> None:
    output_template = "NRC_{invalid}.jpg"
    result = runner.invoke(cli, ["--output", output_template])
    assert result.exit_code == 2
    assert "Error: Invalid value for '-o' / '--output': " in result.output
