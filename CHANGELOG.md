# Changelog

All notable changes to this ontology are documented in this file.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning: SemVer adapted for ontologies (see CONTRIBUTING).

## [Unreleased]

## [0.35.1] - 2026-07-08

### Fixed
- Pinned chemical-substance dependency to 0.14.1 (import + all catalogs).
- Pinned CHAMEO import to released 1.0.0 — the import was unversioned and the root catalog pointed at a moving branch URL.

### Changed
- `requirements.txt` / `requirements-docs.txt` removed; `pyproject.toml` is the single source of Python dependencies.
- `modules/manufacturing-*.ttl` documented as incubating content for a future domain-manufacturing repository.
- `bump-version` replaced by the shared config-driven tool (adds `--check` and date handling) with tests.

[Unreleased]: https://github.com/emmo-repo/domain-electrochemistry/compare/v0.35.1...HEAD
[0.35.1]: https://github.com/emmo-repo/domain-electrochemistry/releases/tag/v0.35.1
