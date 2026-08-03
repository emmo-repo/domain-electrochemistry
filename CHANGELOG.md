# Changelog

All notable changes to this ontology are documented in this file.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning: SemVer adapted for ontologies (see CONTRIBUTING).

## [Unreleased]

## [0.36.0] - 2026-08-03

### Added
- Cell component classes in electrochemistry-reference: `Seal`, `WoundStack` (altLabels JellyRoll, SwissRoll), `SafetyVent`, `CurrentInterruptDevice` (altLabel CID), `InsulatorRing`, `CeramicCoating`.
- Quantity classes in electrochemistry-quantities: `MinimumOperatingTemperature`, `MaximumOperatingTemperature`, `TypicalCapacity`, `DryCoatingThickness`.
- Scheduled (weekly + post-release) CI check that the public w3id.org IRIs resolve, ported from domain-chemical-substance.
- The docs workflow now also redeploys automatically after each successful release (`workflow_run`), so the `versions/` archive picks up the new inferred release asset without a manual dispatch.

### Changed
- Updated the CHAMEO import to 1.0.2 and the chemical-substance import to 0.15.0 (import + all catalogs). Both dependencies import EMMO 1.0.2, matching this ontology.

## [0.35.1] - 2026-07-08

### Fixed
- Pinned chemical-substance dependency to 0.14.1 (import + all catalogs).
- Pinned CHAMEO import to released 1.0.0 — the import was unversioned and the root catalog pointed at a moving branch URL.

### Changed
- `requirements.txt` / `requirements-docs.txt` removed; `pyproject.toml` is the single source of Python dependencies.
- `modules/manufacturing-*.ttl` documented as incubating content for a future domain-manufacturing repository.
- `bump-version` replaced by the shared config-driven tool (adds `--check` and date handling) with tests.
- The inferred ontology (`electrochemistry-inferred.ttl`) is no longer tracked in git — it is a generated build artifact. CI regenerates it and publishes it to gh-pages (`/inferred`, latest) and attaches a freshly reasoned copy to each GitHub Release (per version); the docs workflow backfills the per-version `versions/` archive from Release assets. You no longer generate or commit it by hand.

[Unreleased]: https://github.com/emmo-repo/domain-electrochemistry/compare/v0.36.0...HEAD
[0.36.0]: https://github.com/emmo-repo/domain-electrochemistry/compare/v0.35.1...v0.36.0
[0.35.1]: https://github.com/emmo-repo/domain-electrochemistry/releases/tag/v0.35.1
