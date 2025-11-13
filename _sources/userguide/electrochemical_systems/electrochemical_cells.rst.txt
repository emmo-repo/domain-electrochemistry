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
   Represents a *complete product* or engineered object — such as a coin cell, pouch cell, battery module, fuel cell stack, or supercapacitor. It includes mechanical structures, safety components, and interfaces to the environment.

   In other words, **a device contains one or more cells**, but a cell is the level at which the electrochemistry happens.

Conceptual Structure
--------------------

Every electrochemical cell consists of three core components:

- **Positive Electrode** — the electrode at higher potential during discharge (cathode).  
- **Negative Electrode** — the electrode at lower potential during discharge (anode).  
- **Electrolyte** — the ionic conductor between the electrodes.

Many cells also include a **Separator**, **Current Collectors**, and **Casing** (when modeled as part of a device).

.. figure:: ../../assets/img/fig/png/electrochemical_cell_structure.png
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
- `HalfCell` — a single electrode–electrolyte interface (for measurement)  
- `ReferenceCell` — a standardized potential reference system

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ElectrochemicalCell"
   }

2. Define the Main Parts
^^^^^^^^^^^^^^^^^^^^^^^^

Use **domain-specific part relations**, all of which are subproperties of `emmo:hasPart`, to describe composition.

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

**Example: lithium-ion half-cell electrodes**

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ElectrochemicalCell",
     "hasElectrode": [
       {
         "@type": "PositiveElectrode",
         "hasCoating": {
           "@type": "ElectrodeCoating",
           "hasActiveMaterial": { "@type": "LiNi0.8Mn0.1Co0.1O2" },
           "hasBinder": { "@type": "PVDF" },
           "hasAdditive": { "@type": "CarbonBlack" }
         },
         "hasCurrentCollector": { "@type": "AluminiumFoil" }
       },
       {
         "@type": "NegativeElectrode",
         "hasCoating": {
           "@type": "ElectrodeCoating",
           "hasActiveMaterial": { "@type": "Graphite" },
           "hasBinder": { "@type": "PVDF" },
           "hasAdditive": { "@type": "CarbonBlack" }
         },
         "hasCurrentCollector": { "@type": "CopperFoil" }
       }
     ],
     "hasElectrolyte": {
       "@type": "OrganicElectrolyte",
       "hasSolvent": { "@type": "EthyleneCarbonate" },
       "hasSolute": { "@type": "LiPF6" }
     },
     "hasSeparator": { "@type": "MicroporousPolymerSeparator" }
   }


4. Assign Cell Properties
^^^^^^^^^^^^^^^^^^^^^^^^^

Cells have measurable properties describing electrochemical performance and physical configuration.  
These are modeled as **quantities** or **conventional properties** via `hasProperty`.

Common examples:

- `NominalVoltage`  
- `RatedCapacity`  
- `InternalResistance`  
- `ElectrodeArea`  
- `SeparatorThickness`

**Example: adding cell-level properties**

.. code-block:: json

   {
     "@type": "ElectrochemicalCell",
     "hasProperty": [
       {
         "@type": "NominalVoltage",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 3.7 },
         "hasMeasurementUnit": "emmo:Volt"
       },
       {
         "@type": "RatedCapacity",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 4.8 },
         "hasMeasurementUnit": "emmo:AmpereHour"
       }
     ]
   }


5. Specialized Cell Types
^^^^^^^^^^^^^^^^^^^^^^^^^

Several subclasses are available for specific electrochemical contexts.

| Class | Description | Example |
|--------|--------------|----------|
| `GalvanicCell` | Spontaneous discharge cell | Zinc–manganese dioxide (alkaline) |
| `ElectrolyticCell` | Driven electrolysis | Water electrolysis, metal plating |
| `HalfCell` | Single-electrode test cell | Li/Li⁺ reference or working electrode |
| `ReferenceCell` | Stable potential reference | Ag/AgCl electrode |
| `ThreeElectrodeCell` | Laboratory setup with reference electrode | Common in electrochemical testing |

**Example: three-electrode configuration**

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ThreeElectrodeCell",
     "hasWorkingElectrode": { "@type": "PlatinumElectrode" },
     "hasCounterElectrode": { "@type": "GraphiteElectrode" },
     "hasReferenceElectrode": { "@type": "SilverChlorideElectrode" },
     "hasElectrolyte": { "@type": "AqueousElectrolyte", "hasSolute": { "@type": "PotassiumChloride" } }
   }


Reasoning and Hierarchy
-----------------------

Because all part relations such as `hasElectrode`, `hasElectrolyte`, and `hasSeparator`  
are **subproperties of `emmo:hasPart`**, the ontology supports transitive reasoning:

::
   If Cell hasElectrode Electrode,
   and Electrode hasCoating Coating,
   then Cell hasPart Coating.

This allows queries like “find all cells containing a given material”  
to retrieve results across multiple structural layers.


Best Practices
--------------

- Use **ElectrochemicalCell** for the functional reacting system,  
  and **ElectrochemicalDevice** for encapsulated or engineered units.  
- Always define both electrodes and the electrolyte for completeness.  
- Use **domain-specific subproperties** (`hasElectrode`, `hasElectrolyte`, etc.) instead of `hasPart` directly.  
- For laboratory setups, use `HalfCell` or `ThreeElectrodeCell` depending on the measurement configuration.  
- Attach measurable quantities as `hasProperty` relations.  
- Avoid including mechanical casings, connectors, or packaging elements — those belong to the **device** level.  


Summary
-------

Electrochemical cells represent the **active domain of electrochemistry** —  
the space where electrons, ions, and matter interact through redox reactions.

| Concept | Relation | Example |
|----------|-----------|----------|
| **ElectrochemicalCell** | `hasElectrode`, `hasElectrolyte`, `hasSeparator` | basic two-electrode configuration |
| **GalvanicCell** | subclass of `ElectrochemicalCell` | zinc–manganese dioxide |
| **ElectrolyticCell** | subclass of `ElectrochemicalCell` | water electrolysis cell |
| **HalfCell** | part of a larger setup | lithium half-cell |
| **ThreeElectrodeCell** | `hasWorkingElectrode`, `hasCounterElectrode`, `hasReferenceElectrode` | potentiostatic test cell |

By describing cells using these relations, EMMO enables structured, machine-interpretable representations of electrochemical systems — linking materials, structure, and performance under one consistent semantic framework.
