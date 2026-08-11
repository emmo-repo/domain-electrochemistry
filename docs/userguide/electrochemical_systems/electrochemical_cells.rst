Electrochemical Cells
=====================

An **electrochemical cell** is the fundamental unit in which an **electrochemical reaction** occurs. It converts chemical energy into electrical energy (or vice versa) through oxidation and reduction at two electrodes separated by an electrolyte.

An electrochemical cell is conceptually distinct from an **electrochemical device**:

- A **cell** is the **functional unit of reaction**, composed of electrodes, electrolyte, and separator.
- A **device** is a **practical assembly** that contains one or more cells, plus mechanical housing, terminals, casing, or other supporting systems.

.. admonition:: Electrochemical Cell vs. Electrochemical Device

   **ElectrochemicalCell**
   Represents the *active system* where charge transfer and ionic conduction occur. It includes electrodes, electrolyte, and separator, but not external casing or packaging.

   **ElectrochemicalDevice**
   Represents a *complete product* or engineered object, such as a fuel cell stack, an electrolyser, or a supercapacitor. It includes mechanical structures, safety components, and interfaces to the environment.

   In other words, **a device contains one or more cells**, but a cell is the level at which the electrochemistry happens.

Conceptual Structure
--------------------

Every electrochemical cell consists of three core components:

- **Positive Electrode** — the electrode at higher potential during discharge (cathode).
- **Negative Electrode** — the electrode at lower potential during discharge (anode).
- **Electrolyte** — the ionic conductor between the electrodes.

Many cells also include a **Separator**, **Current Collectors**, and **Casing** (when modeled as part of a device).

.. figure:: ../../assets/img/fig/png/ElectrochemicalCell.png
   :align: center
   :alt: Structure of an electrochemical cell
   :width: 80%

   Generic architecture of an electrochemical cell.

Guidelines for Use
------------------

Follow these steps to describe an **ElectrochemicalCell** in the ontology.

1. Identify the Cell
^^^^^^^^^^^^^^^^^^^^

Start with the `ElectrochemicalCell` class or one of its subclasses such as:

- `GalvanicCell` — a spontaneous reaction generating electricity
- `ElectrolyticCell` — a driven reaction consuming electrical energy
- `ElectrochemicalHalfCell` — a single electrode-electrolyte interface (for measurement)
- `ThreeElectrodeElectrochemicalCell` — a laboratory setup with working, counter, and reference electrodes

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ElectrochemicalCell"
   }

2. Define the Main Parts
^^^^^^^^^^^^^^^^^^^^^^^^

Use **domain-specific part relations**, all of which are subproperties of `hasPart`, to describe composition.

- `hasElectrode`
- `hasElectrolyte`
- `hasSeparator`
- `hasCase` (optional, if modeling physical structure)

**Example: generic two-electrode cell**

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ElectrochemicalCell",
     "hasElectrode": [
       { "@type": "PositiveElectrode" },
       { "@type": "NegativeElectrode" }
     ],
     "hasElectrolyte": { "@type": "LiquidElectrolyte" },
     "hasSeparator": { "@type": "Separator" }
   }

3. Define Electrode Composition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each electrode can itself be modeled using `hasCoating`, `hasCurrentCollector`, and related relations.
This maintains hierarchical structure and reasoning consistency.

**Example: lithium-ion cell electrodes**

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ElectrochemicalCell",
     "hasElectrode": [
       {
         "@type": "PositiveElectrode",
         "hasCoating": {
           "@type": "ElectrodeCoating",
           "hasActiveMaterial": { "@type": "LithiumNickelManganeseCobaltOxide811" },
           "hasBinder": { "@type": "PolyvinylideneFluoride" },
           "hasAdditive": { "@type": "CarbonBlack" }
         },
         "hasCurrentCollector": { "@type": ["Aluminium", "Foil"] }
       },
       {
         "@type": "NegativeElectrode",
         "hasCoating": {
           "@type": "ElectrodeCoating",
           "hasActiveMaterial": { "@type": "Graphite" },
           "hasBinder": { "@type": "PolyvinylideneFluoride" },
           "hasAdditive": { "@type": "CarbonBlack" }
         },
         "hasCurrentCollector": { "@type": ["Copper", "Foil"] }
       }
     ],
     "hasElectrolyte": {
       "@type": "OrganicElectrolyte",
       "hasSolvent": { "@type": "EthyleneCarbonate" },
       "hasSolute": { "@type": "LithiumHexafluorophosphate" }
     },
     "hasSeparator": { "@type": "Separator" }
   }


4. Assign Cell Properties
^^^^^^^^^^^^^^^^^^^^^^^^^

Cells have measurable properties describing electrochemical performance and physical configuration.
These are modeled as **quantities** or **conventional properties** via `hasProperty`.

Common examples:

- `NominalVoltage`
- `RatedCapacity`
- `InternalResistance`
- `SeparatorThickness`

**Example: adding cell-level properties**

.. code-block:: json

   {
     "@type": "ElectrochemicalCell",
     "hasProperty": [
       {
         "@type": "NominalVoltage",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 3.7 },
         "hasMeasurementUnit": "Volt"
       },
       {
         "@type": "InternalResistance",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 0.025 },
         "hasMeasurementUnit": "Ohm"
       }
     ]
   }


5. Specialized Cell Types
^^^^^^^^^^^^^^^^^^^^^^^^^

Several subclasses are available for specific electrochemical contexts.

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Class
     - Description
     - Example
   * - `GalvanicCell`
     - Spontaneous discharge cell
     - Zinc-manganese dioxide (alkaline)
   * - `ElectrolyticCell`
     - Driven electrolysis
     - Water electrolysis, metal plating
   * - `ElectrochemicalHalfCell`
     - Single-electrode test cell
     - Li/Li⁺ working electrode setup
   * - `ThreeElectrodeElectrochemicalCell`
     - Laboratory setup with reference electrode
     - Common in electrochemical testing

**Example: three-electrode configuration**

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ThreeElectrodeElectrochemicalCell",
     "hasWorkingElectrode": { "@type": "PlatinumElectrode" },
     "hasCounterElectrode": { "@type": "GraphiteElectrode" },
     "hasReferenceElectrode": { "@type": "SilverChlorideElectrode" },
     "hasElectrolyte": { "@type": "AqueousElectrolyte", "hasSolute": { "@type": "PotassiumChloride" } }
   }


Electrochemical Devices
-----------------------

An **ElectrochemicalDevice** is the engineered product built around one or more cells. This ontology defines general device classes for electrochemistry:

- `FuelCell` — converts chemical fuel and oxidant into electricity
- `Electrolyser` — uses electricity to drive a chemical conversion
- `Supercapacitor` — stores energy in electrochemical double layers

Battery-specific device classes (battery cells, modules, and packs) are defined in `domain-battery <https://github.com/emmo-repo/domain-battery>`__, which builds on this ontology.

Describe a device's makeup with the same part relations used for cells, and link it to the process it performs with `hasParticipant`, `hasInput`, and `hasOutput`.

**Example: supercapacitor with device-level property**

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "Supercapacitor",
     "hasElectrode": [
       { "@type": "Electrode" },
       { "@type": "Electrode" }
     ],
     "hasElectrolyte": { "@type": "OrganicElectrolyte" },
     "hasCase": { "@type": "PouchCase" },
     "hasProperty": {
       "@type": "SpecificPower",
       "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 10000 },
       "hasMeasurementUnit": "WattPerKilogram"
     }
   }

**Example: electrolyser and the electrolysis process it performs**

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "Electrolysis",
     "hasParticipant": { "@type": "Electrolyser" },
     "hasInput": { "@type": "Water" },
     "hasOutput": [
       { "@type": "Hydrogen" },
       { "@type": "Oxygen" }
     ]
   }


Reasoning and Hierarchy
-----------------------

Part relations such as `hasElectrode`, `hasElectrolyte`, and `hasSeparator` are **subproperties of `hasPart`**, so a reasoner infers the general relation from the specific one:

.. code-block:: text

   If Cell hasElectrode Electrode,
   then Cell hasPart Electrode.

A query for `hasPart` therefore also retrieves parts stated with the domain-specific relations, without you having to enumerate them.

Best Practices
--------------

- Use **ElectrochemicalCell** for the functional reacting system,
  and **ElectrochemicalDevice** for encapsulated or engineered units.
- Always define both electrodes and the electrolyte for completeness.
- Use **domain-specific subproperties** (`hasElectrode`, `hasElectrolyte`, etc.) instead of `hasPart` directly.
- For laboratory setups, use `ElectrochemicalHalfCell` or `ThreeElectrodeElectrochemicalCell` depending on the measurement configuration.
- Attach measurable quantities as `hasProperty` relations.
- Avoid including mechanical casings, connectors, or packaging elements at the cell level — those belong to the **device** level.


Summary
-------

Electrochemical cells represent the **active domain of electrochemistry** —
the space where electrons, ions, and matter interact through redox reactions.

.. list-table::
   :header-rows: 1
   :widths: 34 38 28

   * - Concept
     - Relation
     - Example
   * - **ElectrochemicalCell**
     - `hasElectrode`, `hasElectrolyte`, `hasSeparator`
     - basic two-electrode configuration
   * - **GalvanicCell**
     - subclass of `ElectrochemicalCell`
     - zinc-manganese dioxide
   * - **ElectrolyticCell**
     - subclass of `ElectrochemicalCell`
     - water electrolysis cell
   * - **ThreeElectrodeElectrochemicalCell**
     - `hasWorkingElectrode`, `hasCounterElectrode`, `hasReferenceElectrode`
     - potentiostatic test cell
   * - **ElectrochemicalDevice**
     - `hasCase`, `hasProperty`
     - fuel cell, electrolyser, supercapacitor

By describing cells using these relations, the ontology enables structured, machine-interpretable representations of electrochemical systems — linking materials, structure, and performance under one consistent semantic framework.
