# Changelog

All notable changes to this ontology are documented in this file.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning: SemVer adapted for ontologies (see CONTRIBUTING).

## [Unreleased]

### Added
- `OpenCircuitPotential` (altLabels OCP, RestPotential, ZeroCurrentElectrodePotential): the electrode-level quantity, potential of an electrode relative to a reference when no net current flows, under `ElectrodePotential`. `EquilibriumElectrodePotential` now sits under it: an open-circuit potential at which all interfacial equilibria are also established. Branch classes `AnodicBranchOpenCircuitPotential` and `CathodicBranchOpenCircuitPotential` (disjoint with each other and with the equilibrium potential), `OpenCircuitPotentialHysteresis`, and `TemperatureCoefficientOfTheOpenCircuitPotential` (altLabel EntropicChangeCoefficient), the electrode-level sibling of the IEV cell quantity.
- `EquilibriumCellVoltage` (altLabels EquilibriumCellPotential, ReversibleCellVoltage): the thermodynamic electromotive force, open-circuit voltage with all interfacial equilibria established, equal to minus the reaction Gibbs energy over zF; and `OpenCircuitVoltageHysteresis`.
- `GuestDiffusivity`, a defined class (`Diffusivity and isPropertyFor some ActiveMaterial`) and the polarity-free parent the deprecated `GuestDiffusivityIn…ElectrodeActiveMaterial` classes should have had; `GuestChemicalPotential` under EMMO `ChemicalPotential`, the quantity an open-circuit potential curve encodes.
- BPX-motivated quantities (jsimonclark/BPX application ontology, gap rows): `TransportEfficiency` (inverse MacMullin number, next to Tortuosity and BruggemanCoefficient), `NumberOfElectrodePairs`, `ChargeCarrierInventoryLossFraction` and `ActiveMaterialCapacityLossFraction` (the degradation modes LLI and LAM, as ratios of capacities, chemistry-neutral).
- altLabels `Negatrode` and `Positrode` on `NegativeElectrode` and `PositiveElectrode` (#204).

### Changed
- `OpenCircuitVoltage` is now unambiguously the cell-level quantity of IEV 482-03-32: voltage between the terminals of a cell or battery when no current flows. Its elucidation previously described the electrode-level quantity while its IEV reference, parent (`CellVoltage`) and equivalence with EMMO `SourceVoltage` (IEC 80000-6 item 6-36, formerly electromotive force) were cell-level. altLabels `OCP` and `OpenCircuitPotential` move to the new electrode class; `ElectromotiveForce` and `ZeroCurrentCellPotential` are added. **Migration:** data that typed electrode open-circuit potential curves as `OpenCircuitVoltage` should use `OpenCircuitPotential`; the IRI keeps resolving, the typing is just imprecise until migrated.
- `EquilibriumElectrodePotential` re-parented from `OpenCircuitVoltage` + `ElectrodePotential` to `OpenCircuitPotential`; `skos:related` to `EquilibriumCellVoltage`, `NernstEquation` and `MolarElectrochemicalPotential`.
- `MolarElectrochemicalPotential` is now a subclass of EMMO `ChemicalPotential` with the IUPAC definition (partial molar Gibbs energy of a charged species at a specified electric potential) and a comment on how equilibrium potentials follow from it; `ElectrochemicalPotential` is elucidated as its per-particle counterpart (it carries an energy unit) and no longer cites the molar IUPAC entry.
- The deprecated polarity anchors for open-circuit voltage, entropic change coefficient and guest diffusivity (and its activation energy) now point at `OpenCircuitPotential`, `TemperatureCoefficientOfTheOpenCircuitPotential` and `GuestDiffusivity` in their `isReplacedBy`, defining axioms and scope notes.
- `ChargeCarrierDiffusivityInElectrolyte` elucidation no longer says lithium.

## [0.38.0] - 2026-10-12

### Added
- `ElectrodeToSeparatorGapWidth` quantity class (#178): width of the spacing between an electrode surface and the adjacent separator or ion-exchange membrane; zero for zero-gap designs. Subclass of EMMO `Thickness` and `ElectrochemicalQuantity`.
- `formerLabel` annotation property (sub-property of `skos:hiddenLabel`) carrying prefLabel spellings that were later corrected. The context generator emits its values as extra JSON-LD terms for the same IRI, so data written against an old spelling keeps expanding (#193).
- Redirect stubs for URLs that existed on the published docs site before pages were moved or removed: `pages/electrochemistry.html` (class index, moved in March 2025), `pages/get-started.html`, `pages/getstarted.html`, `pages/faq.html`, `pages/resources.html`, `pages/tools.html`, `userguide/background/index.html`, `userguide/introduction/index.html` (#186).
- Docs guardrails (#188): a term linter that checks every `@type`, property key and `hasMeasurementUnit` value in docs examples against the published context (new violations fail, existing ones are baselined in `tests/docs_term_baseline.txt`); a non-blocking Sphinx warning-count job with a committed baseline; notebooks are never executed at build time (`nbsphinx_execute = 'never'`), removing the build's network dependency on w3id.org.
- Test that every sphinx-design grid-card `:link:` target in the docs sources is a page the build produces (#187).
- `tests/test_deprecations.py`: every deprecated term has `dcterms:isReplacedBy` or an `rdfs:comment` of the form `Deprecated in X.Y.Z:`; defined deprecated classes name their replacement in the intersection and subclass it. Pre-convention deprecations are tolerated through `tests/deprecated_baseline.txt`, which may only shrink (#192).
- `tests/test_docs_index_anchors.py`: every deprecated term keeps its anchor in the generated class index, since term IRIs dereference to that page (#192).
- CONTRIBUTING rule for qualified quantities: a qualifier earns its own class only when it changes what is measured or how the value is determined; compound classes need a defining axiom; tool keys and column names live with the tool (#192).
- Tests: redirect stubs resolve to real pages; every `formerLabel` resolves in the context; no cycler column name (plain `skos:hiddenLabel` or vendor label property) leaks into the context; every domain prefLabel is a context term.

### Changed
- The 28 polarity-qualified anchor quantities (`NegativeElectrodeCoatingThickness`, `PositiveElectrodeActiveMaterialParticleRadius`, ... , the full table is in #192) are deprecated and defined by axioms. Each is now `owl:equivalentClass` of its polarity-free parent intersected with `isPropertyFor some <bearer>`, where the bearer is built from the cell structure (`hasNegativeElectrode` / `hasPositiveElectrode`, `hasCoating`, `hasActiveMaterial`, `hasParticipant`; the electrode and active-material bearers accept the electrode or its coating), plus `owl:deprecated`, `dcterms:isReplacedBy` the parent, a dated comment and a `skos:scopeNote` saying how to state the polarity through the structure. IRIs, prefLabels, parent links and tool keys are unchanged, so existing data keeps classifying and resolving. The 'anchor term' boilerplate is removed from these and from the four electrolyte terms, which keep their classes; 18 classes that had it as their elucidation now have real ones (#192).
- `hasNegativeElectrode` / `hasPositiveElectrode` now range over `NegativeElectrode` / `PositiveElectrode` (was `Electrode`); the two classes are not disjoint (#192).
- The generated class index flags deprecated terms with a warning block linking to their replacement and sorts them after current terms; it no longer hides them, since their IRIs dereference to that page (#192).
- Docs project identity in `conf.py` corrected and `docs/ai_resources` moved to the repository root as `ai_resources/` (#189).
- Import `https://w3id.org/emmo/1.0.2/disciplines/units/siacceptedunits` in `reference/electrochemistry-quantities.ttl`, the module that references those units (#191). EMMO 1.0.2's default chain (emmo, disciplines, sisystem) does not reach this module, so `AmpereHour`, `MilliAmpereHour`, `WattHour`, `KiloWattHour`, `MolePerLitre` and `MilliAmpereHourPerGram` were referenced but never declared and had no context term. The context gains 198 unit terms; nothing is removed. The context now also binds the `emmo` prefix explicitly (the reasoned squash binds none, so rdflib invented `ns1`), which makes the `emmo:AmpereHour`-style CURIEs used throughout the JSON-LD assets expand.

### Removed
- Docs: the `userguide/background/` chapter (20 pages), `userguide/introduction/`, `userguide/_deprecate/`, the `pages/faq`, `pages/get-started`, `pages/tools` and `pages/resources` pages, and `examples/basic` (#189). Their URLs are kept alive by the redirect stubs listed under Added.

### Fixed
- Landing-page and Examples grid cards linked to pages that did not exist (`pages/user-guide.html`, old example paths); repointed (#187, the in-site part of #186).
- Seven misspelled labels (#193, #162): `CarbonDioxideElectrode` (was Cardon), `LithiumNickelManganeseCobaltOxideLithiumManganeseOxideElectrode` (was Mananese), `PositiveElectrodeActivationEnergyOfReaction` (was Postive), `InitialThermodynamicTemperature` (was Initital), `MinimumTemperature` and `MinimumConcentration` (were Miniumum), altLabel `MinimumAcceptedCapacity`. IRIs unchanged; the old prefLabel spellings stay resolvable through `formerLabel`.
- Three `bpxKey` mappings, four annotation values (#194): the positive-electrode stoichiometry keys at SOC0 and SOC100 were swapped (BPX puts the positive electrode at maximum stoichiometry at 0 % SOC); `InitialChargeCarrierConcentrationInElectrolyte` pointed at the pre-1.1 path instead of `State / Initial conditions / Initial electrolyte concentration [mol.m-3]` (BPX 1.1 moved it); `DeviceSurfaceArea` had a duplicated `Parameterisation` segment.
- README Getting Started link pointed at `pages/getstarted.html`, a page renamed to `get-started` in October 2025 and removed in #189; it now points at the user guide.

## [0.37.2] - 2026-08-10

### Changed
- The seven chemistry-specific electrode classes (`LithiumIronPhosphateElectrode`, `LithiumTitanateElectrode`, `LithiumManganeseIronPhosphateElectrode`, `LithiumNickelManganeseCobaltOxideElectrode`, `LithiumManganeseOxideElectrode`, `SiliconGraphiteElectrode`, `LithiumCobaltOxideElectrode`) are un-deprecated and kept as first-class query vocabulary. Each is now a defined class: `owl:equivalentClass` of its parent intersected with `hasActiveMaterial some <chemical-substance class>`, anchored to chemical-substance 0.15.0. A reasoner classifies electrodes from their asserted composition; the classes never need to be asserted directly. Half of the resolution of emmo-repo/domain-battery#74.

## [0.37.1] - 2026-08-10

### Fixed
- Label duplications found in emmo-repo/domain-battery#76. `Record`: the testing-module class is canonical; the quantities-module duplicate is deprecated with `isReplacedBy`, its `Rec#` hidden label and dataset-entry phrasing move to the canonical class. `ElectrodeCoating`: the manufacturing process class is renamed `ElectrodeCoatingProcess` (old name kept as altLabel), leaving the label to the coating layer class. `C`: deprecated as a duplicate of `AmperePerAmpereHour`; `C` becomes an altLabel on `AmperePerAmpereHour` and `CRateUnit`. `R626`: verbatim duplicate deprecated with `isReplacedBy`. `DirectCurrentSignal`: renamed from `DirectCurrent` to resolve the collision with the current kind; elucidation corrected and references repointed. `Powder`, `Electroplating` and the manufacturing-module `Welding` deprecated in favour of their EMMO core counterparts; `UltrasonicWelding` and `LaserWelding` re-parent to EMMO core `Welding`. All deprecated classes subclass their replacements so existing uses still classify.

## [0.37.0] - 2026-08-10

### Added
- Eight quantity classes in electrochemistry-quantities: `CapacityLoss` (altLabel LostCapacity) and `CapacityFadeRate`, both linked to the existing `CapacityFade` phenomenon; `ChargeRecovery` (IEC 61960-3, 3.1), paired with `ChargeRetention`, which also gains links to `ChargeRecovery` and `StateOfHealth`; `EndOfLifeCapacityThreshold`, linked to `ChargeRetention`, `CycleLife` and `CalendarLife`; `MaximumPower` (altLabel PowerCapability), `ChargingTime`, `PowerToEnergyRatio` and `RoundTripEnergyEfficiency` (subclass of `EnergyEfficiency`, linked to `CoulombicEfficiency`). Community-practice terms without a standards definition (`CapacityFadeRate`, `PowerToEnergyRatio`) say so in `skos:note`. A stubbed `CapacityRetention` class was dropped rather than added, since `ChargeRetention` already carries that altLabel and the IEV 482-03-35 reference.

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

[Unreleased]: https://github.com/emmo-repo/domain-electrochemistry/compare/0.38.0...HEAD
[0.38.0]: https://github.com/emmo-repo/domain-electrochemistry/compare/0.37.2...0.38.0
[0.37.2]: https://github.com/emmo-repo/domain-electrochemistry/compare/0.37.1...0.37.2
[0.37.1]: https://github.com/emmo-repo/domain-electrochemistry/compare/0.37.0...0.37.1
[0.37.0]: https://github.com/emmo-repo/domain-electrochemistry/compare/0.36.0...0.37.0
[0.36.0]: https://github.com/emmo-repo/domain-electrochemistry/compare/0.35.0...0.36.0
