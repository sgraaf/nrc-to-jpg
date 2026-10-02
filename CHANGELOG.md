# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Calendar Versioning](https://calver.org/).

The **first number** of the version is the year.
The **second number** is incremented with each release, starting at 1 for each year.
The **third number** is for emergencies when we need to start branches for older releases.

## [Unreleased](https://github.com/sgraaf/nrc-to-jpg/compare/2026.1.0...HEAD)

## [2026.1.0](https://github.com/sgraaf/nrc-to-jpg/compare/2024.6.0...2026.1.0) - 2026-10-02

### Added

- Support for Python 3.13 and 3.14.

### Changed

- Python 3.11 or newer is now required.
- The default output file name template is now `NRC-front-page_{year:04}-{month:02}-{day:02}.jpg` (was `NRC_front_page_{year:04}-{month:02}-{day:02}.jpg`).
- The HTTP client is now `httpx2` (was `httpx`).
- The `--help` output now shows `(today)` as the default of `--date`, instead of the date on which the help text was generated.
- The allowed output file name template fields are now listed in alphabetical order, both in `--help` and in error messages.
- The development status is now "Production/Stable" (was "Beta").

### Removed

- Support for Python 3.8, 3.9 and 3.10.
- The `nrc_to_jpg.__version__` attribute. Use `importlib.metadata.version("nrc-to-jpg")` instead.

### Fixed

- `--page-number` now matches pages by their first single page number, so the correct page is saved when the newspaper contains spreads.
- The truncated help text of the `--page-number` option.

## [2024.6.0](https://github.com/sgraaf/nrc-to-jpg/releases/tag/2024.6.0) - 2024-06-12

### Added

- Initial release of nrc-to-jpg.
