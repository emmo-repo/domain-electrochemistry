# Changelog

All notable changes to this ontology are documented in this file.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning: SemVer adapted for ontologies (see CONTRIBUTING).

## [Unreleased]

### Added
- `ElectrodeToSeparatorGapWidth` quantity class (#178): width of the spacing between an electrode surface and the adjacent separator or ion-exchange membrane; zero for zero-gap designs. Subclass of EMMO `Distance` and `ElectrochemicalQuantity`.
- `formerLabel` annotation property (sub-property of `skos:hiddenLabel`) carrying prefLabel spellings that were later corrected. The context generator emits its values as extra JSON-LD terms for the same IRI, so data written against an old spelling keeps expanding (#193).
- Redirect stubs for URLs that existed on the published docs site before pages were moved or removed: `pages/electrochemistry.html` (class index, moved in March 2025), `pages/get-started.html`, `pages/getstarted.html`, `pages/faq.html`, `pages/resources.html`, `pages/tools.html` (#186).
- Tests: redirect stubs resolve to real pages; every `formerLabel` resolves in the context; no cycler column name (plain `skos:hiddenLabel` or vendor label property) leaks into the context; every domain prefLabel is a context term.

### Changed
- Import `https://w3id.org/emmo/1.0.2/disciplines/units/siacceptedunits` in `electrochemistry-dependencies.ttl` (#191). EMMO 1.0.2's default chain (emmo, disciplines, sisystem) does not reach this module, so `AmpereHour`, `MilliAmpereHour`, `WattHour`, `KiloWattHour`, `MolePerLitre` and `MilliAmpereHourPerGram` were referenced but never declared and had no context term. The context gains 198 unit terms; nothing is removed.

### Fixed
- Seven misspelled labels (#193, #162): `CarbonDioxideElectrode` (was Cardon), `LithiumNickelManganeseCobaltOxideLithiumManganeseOxideElectrode` (was Mananese), `PositiveElectrodeActivationEnergyOfReaction` (was Postive), `InitialThermodynamicTemperature` (was Initital), `MinimumTemperature` and `MinimumConcentration` (were Miniumum), altLabel `MinimumAcceptedCapacity`. IRIs unchanged; the old prefLabel spellings stay resolvable through `formerLabel`.
- Three `bpxKey` values (#194): the positive-electrode stoichiometry keys at SOC0 and SOC100 were swapped (BPX puts the positive electrode at maximum stoichiometry at 0 % SOC); `InitialChargeCarrierConcentrationInElectrolyte` pointed at the BPX 0.x path instead of `State / Initial conditions / Initial electrolyte concentration [mol.m-3]`; `DeviceSurfaceArea` had a duplicated `Parameterisation` segment.
- README link to `pages/getstarted.html`, which never existed, now points at the user guide.

## [0.37.2] - 2026-08-10

### Changed
- The seven chemistry-specific electrode classes (`LithiumIronPhosphateElectrode`, `LithiumTitanateElectrode`, `LithiumManganeseIronPhosphateElectrode`, `LithiumNickelManganeseCobaltOxideElectrode`, `LithiumManganeseOxideElectrode`, `SiliconGraphiteElectrode`, `LithiumCobaltOxideElectrode`) are un-deprecated and kept as first-class query vocabulary. Each is now a defined class: `owl:equivalentClass` of its parent intersected with `hasActiveMaterial some <chemical-substance class>`, anchored to chemical-substance 0.15.0. A reasoner classifies electrodes from their asserted composition; the classes never need to be asserted directly. Half of the resolution of emmo-repo/domain-battery#74.

## [0.37.1] - 2026-08-10

### Fixed
- Label duplications found in emmo-repo/domain-battery#76. `Record`: the testing-module class is canonical; the quantities-module duplicate is deprecated with `isReplacedBy`, its `Rec#` hidden label and dataset-entry phrasing move to the canonical class. `ElectrodeCoating`: the manufacturing process class is renamed `ElectrodeCoatingProcess` (old name kept as altLabel), leaving the label to the coating layer class. `C`: deprecated as a duplicate of `AmperePerAmpereHour`; `C` becomes an altLabel on `AmperePerAmpereHour` and `CRateUnit`. `R626`: verbatim duplicate deprecated with `isReplacedBy`. `DirectCurrentSignal`: renamed from `DirectCurrent` to resolve the collision with the current kind; elucidation corrected and references repointed. `Powder`, `Electroplating` and the manufacturing-module `Welding` deprecated in favour of their EMMO core counterparts; `UltrasonicWelding` and `LaserWelding` re-parent to EMMO core `Welding`. All deprecated classes subclass their replacements so existing uses still classify.

## [0.37.0] - 2026-08-10

### Added
- Nine quantity classes in electrochemistry-quantities: `CapacityLoss` (altLabel LostCapacity) and `CapacityFadeRate`, both linked to the existing `CapacityFade` phenomenon; `ChargeRecovery` (IEC 61960-3, 3.1), paired with `ChargeRetention`, which also gains links to `ChargeRecovery` and `StateOfHealth`; `EndOfLifeCapacityThreshold`, linked to `ChargeRetention`, `CycleLife` and `CalendarLife`; `MaximumPower` (altLabel PowerCapability), `ChargingTime`, `PowerToEnergyRatio` and `RoundTripEnergyEfficiency` (subclass of `EnergyEfficiency`, linked to `CoulombicEfficiency`). Community-practice terms without a standards definition (`CapacityFadeRate`, `PowerToEnergyRatio`) say so in `skos:note`. A stubbed `CapacityRetention` class was dropped rather than added, since `ChargeRetention` already carries that altLabel and the IEV 482-03-35 reference.

## [0.36.0] - 2026-08-03

### Added
- Cell component classes in electrochemistry-reference: `Seal`, `WoundStack` (altLabels JellyRoll, SwissRoll), `SafetyVent`, `CurrentInterruptDevice` (altLabel CID), `InsulatorRing`, `CeramicCoating`.
- Quantity classes in electrochemistry-quantities: `MinimumOperatingTemperature`, `MaximumOperatingTemperature`, `TypicalCapacity`, `DryCoatingThickness`.
- Scheduled (weekly + post-release) CI check that the public w3id.org IRIs resolve, ported from domain-chemical-substance.
- The docs workflow now also redeploys automatically after each successful release (`workflow_run`), so the `versions/` archive picks up the new inferred release asset without a manual dispatch.

### Changed
- Updated the CHAMEO import to 1.0.2 and the chemical-substance import to 0.15.0 (import + all catalogs). Both dependencies import EMMO 1.0.2, matching this ontology.
- Disentangled coulombic and faradaic efficiency (#179). The IRI carrying the IEV 114-03-07 definition (fraction of charge driving the desired reaction) is now labelled `FaradaicEfficiency`; the IRI carrying the IEV 482-05-39 battery definition (discharge-to-charge ratio) is now labelled `CoulombicEfficiency` (altLabel ChargeEfficiency). `InitialCoulombicEfficiency` re-parented accordingly. IRI semantics unchanged — labels and one subClassOf only; consumers that pinned battery coulombic efficiency to the faradaic IRI should re-point.
- Annotated `HalfCellDevice` and `ThreeElectrodeCellDevice`.

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
