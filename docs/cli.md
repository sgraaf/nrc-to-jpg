# CLI Reference

This page lists the `--help` for `nrc-to-jpg` and all its commands.

## nrc-to-jpg

Running `nrc-to-jpg --help` or `python -m nrc_to_jpg --help` shows a list of all of the available options and commands:

<!-- [[[cog
import cog
from nrc_to_jpg import cli
from click.testing import CliRunner
result = CliRunner().invoke(cli.cli, ["--help"], terminal_width=88)
help = result.output.replace("Usage: cli", "Usage: nrc-to-jpg")
cog.outl(f"\n```sh\nnrc-to-jpg --help\n{help.rstrip()}\n```\n")
for command in cli.cli.commands.keys():
    result = CliRunner().invoke(cli.cli, [command, "--help"], terminal_width=88)
    help = result.output.replace("Usage: cli ", "Usage: nrc-to-jpg ")
    cog.outl(f"## nrc-to-jpg {command}\n\n```sh\nnrc-to-jpg {command} --help\n{help.rstrip()}\n```\n")
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

## nrc-to-jpg repeat

```sh
nrc-to-jpg repeat --help
Usage: nrc-to-jpg repeat [OPTIONS] INPUT

  Repeat the input.

Options:
  -r, --reverse  Reverse the input.
  -h, --help     Show this message and exit.
```

<!-- [[[end]]] -->
