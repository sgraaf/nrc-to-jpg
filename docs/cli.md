# CLI Reference

This page lists the `--help` for `nrc-to-jpg`.

## nrc-to-jpg

Running `nrc-to-jpg --help` or `python -m nrc_to_jpg --help` shows a list of all of the available options and arguments:

<!-- [[[cog
import cog
from click.testing import CliRunner
from nrc_to_jpg import cli
result = CliRunner().invoke(cli.cli, ["--help"], terminal_width=88)
output = result.output.replace("Usage: cli", "Usage: nrc-to-jpg")
help_text = "\n".join(line.rstrip() for line in output.splitlines()).rstrip()
cog.outl(f"\n```shell\nnrc-to-jpg --help\n{help_text}\n```\n")
]]] -->

```shell
nrc-to-jpg --help
Usage: nrc-to-jpg [OPTIONS]

  Save the NRC front page to a JPG image.

Options:
  -d, --date [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]
                                  The date to save that day's front page of.  [default:
                                  (today)]
  -n, --page-number INTEGER       The page number to save.  [default: 1]
  -o, --output FORMAT-STR         Output file name template. Allowed fields: `day`,
                                  `month`, `page_number`, `year`  [default: NRC-front-
                                  page_{year:04}-{month:02}-{day:02}.jpg]
  -v, --version                   Show the version and exit.
  -h, --help                      Show this message and exit.
```

<!-- [[[end]]] -->
