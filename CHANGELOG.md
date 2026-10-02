# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project adheres to [Calendar Versioning](https://calver.org/).

The **first number** of the version is the year.
The **second number** is incremented with each release, starting at 1 for each year.
The **third number** is for emergencies when we need to start branches for older releases.

## [2026.1.0](https://github.com/sgraaf/nrc-to-jpg/compare/2024.6.0...2026.1.0) (2026-10-02)

### Breaking changes

- Dropped support for Python 3.8, 3.9 and 3.10; Python 3.11 or newer is now required
- Changed the default output file name template from `NRC_front_page_{year:04}-{month:02}-{day:02}.jpg` to `NRC-front-page_{year:04}-{month:02}-{day:02}.jpg`
- Removed `nrc_to_jpg.__version__`; use `importlib.metadata.version("nrc-to-jpg")` instead

### Added

- Official support for Python 3.13 and 3.14

### Changed

- Switched the HTTP client from `httpx` to `httpx2`
- The `--date` option now shows `(today)` as its default in `--help`, instead of the date on which the help text was generated
- Allowed output file name template fields are now listed in alphabetical order (in `--help` and in error messages)
- Marked the project as "Production/Stable"

### Fixed

- `--page-number` now matches pages by their (first) single page number, so that the correct page is saved when the paper contains spreads
- Fixed the truncated help text of the `--page-number` option

## 2024.6.0 (2024-06-12)

### Changes

- Initial release of nrc-to-jpg
