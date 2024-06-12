<!-- start docs-include-index -->

# nrc-to-jpg

[![PyPI](https://img.shields.io/pypi/v/nrc-to-jpg)](https://img.shields.io/pypi/v/nrc-to-jpg)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/nrc-to-jpg)](https://pypi.org/project/nrc-to-jpg/)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sgraaf/nrc-to-jpg/main.svg)](https://results.pre-commit.ci/latest/github/sgraaf/nrc-to-jpg/main)
[![Test](https://github.com/sgraaf/nrc-to-jpg/actions/workflows/test.yml/badge.svg)](https://github.com/sgraaf/nrc-to-jpg/actions/workflows/test.yml)
[![Documentation Status](https://readthedocs.org/projects/nrc-to-jpg/badge/?version=latest)](https://nrc-to-jpg.readthedocs.io/en/latest/?badge=latest)
[![PyPI - License](https://img.shields.io/pypi/l/nrc-to-jpg)](https://img.shields.io/pypi/l/nrc-to-jpg)

Save the NRC front page to a JPG image.

<!-- end docs-include-index -->

## Installation

<!-- start docs-include-installation -->

nrc-to-jpg is available on [PyPI](https://pypi.org/project/nrc-to-jpg/). Install with [pipx](https://pypa.github.io/pipx/) or your package manager of choice:

```sh
pipx install nrc-to-jpg
```

<!-- end docs-include-installation -->

## Documentation

Check out the [nrc-to-jpg documentation](https://nrc-to-jpg.readthedocs.io/en/stable/) for the [User's Guide](https://nrc-to-jpg.readthedocs.io/en/stable/usage.html) and [CLI Reference](https://nrc-to-jpg.readthedocs.io/en/stable/cli.html).

## Usage

<!-- start docs-include-usage -->

Running `nrc-to-jpg --help` or `python -m nrc_to_jpg --help` shows a list of all of the available options and commands:

<!-- [[[cog
import cog
from nrc_to_jpg import cli
from click.testing import CliRunner
runner = CliRunner()
result = runner.invoke(cli.cli, ["--help"], terminal_width=88)
help = result.output.replace("Usage: cli", "Usage: nrc-to-jpg")
cog.outl(f"\n```sh\nnrc-to-jpg --help\n{help.rstrip()}\n```\n")
]]] -->

```sh
nrc-to-jpg --help
Usage: nrc-to-jpg [OPTIONS] COMMAND [ARGS]...

  Save the NRC front page to a JPG image.

Options:
  -v, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  repeat  Repeat the input.
```

<!-- [[[end]]] -->

<!-- end docs-include-usage -->
