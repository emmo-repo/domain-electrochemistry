Electrodes
==========

An **electrode** is the component of an electrochemical system where oxidation and reduction reactions occur.  
Electrodes act as interfaces between electronic and ionic conductors — storing, releasing, or transferring charge during operation.

In the ontology, electrodes are represented as **physical objects** that can be decomposed into functional and structural subparts such as coatings, current collectors, and materials.

Common electrode types include:

- **Anode** — oxidation occurs here (negative during discharge).  
- **Cathode** — reduction occurs here (positive during discharge).  
- **Reference Electrode** — provides a stable reference potential in measurement cells.

Conceptual Structure
--------------------

An electrode typically consists of:

- **Current Collector** — conducts electrons to/from the external circuit.  
- **Coating** — the functional layer that includes:
  - **Active Material** — participates in electrochemical reactions.  
  - **Binder** — provides mechanical integrity.  
  - **Conductive Additive** — enhances electronic conductivity.  

.. figure:: ../../assets/img/fig/png/electrode_structure.png
   :align: center
   :alt: Structure of an electrode
   :width: 80%

   Example structure of a coated electrode.

Guidelines for Use
------------------

Follow these steps when describing an electrode:

1. Identify the Electrode
^^^^^^^^^^^^^^^^^^^^^^^^^

Start by selecting the appropriate class, such as `Electrode`, `Anode`, or `Cathode`.  
If the electrode has one or more coatings, use the subclasses `SingleCoatedElectrode` or `DoubleCoatedElectrode`.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "Electrode"
   }

2. Assign Properties
^^^^^^^^^^^^^^^^^^^^

Attach measurable or conventional properties using `hasProperty`.  
Common examples include **thickness**, **porosity**, **mass loading**, or **specific capacity**.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "Electrode",
     "hasProperty": [
       {
         "@type": "Thickness",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumberValue": 50
         },
         "hasMeasurementUnit": "emmo:MicroMetre"
       }
     ]
   }

3. Define Structural Composition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Link the electrode to its subparts using **domain-specific relations** such as:

- `hasCoating`
- `hasCurrentCollector`
- `hasActiveMaterial`
- `hasBinder`
- `hasAdditive`

These are **subproperties of `hasPart`**, which allows reasoning systems to automatically infer part–whole hierarchies.

Representation Patterns
-----------------------

Single Coated Electrode
^^^^^^^^^^^^^^^^^^^^^^^

A `SingleCoatedElectrode` has one functional coating on its current collector.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "SingleCoatedElectrode",
     "hasCoating": {
       "@type": "ElectrodeCoating",
       "hasActiveMaterial": { "@type": "LiFePO4" },
       "hasBinder": { "@type": "PVDF" },
       "hasAdditive": { "@type": "CarbonBlack" }
     },
     "hasCurrentCollector": { "@type": "AluminiumFoil" },
     "hasProperty": [
       {
         "@type": "Thickness",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 75 },
         "hasMeasurementUnit": "emmo:MicroMetre"
       }
     ]
   }

This example describes a lithium iron phosphate (LFP) cathode with a single coating applied to an aluminum current collector.

Double Coated Electrode
^^^^^^^^^^^^^^^^^^^^^^^

A `DoubleCoatedElectrode` has two coatings applied on opposite sides of the same current collector — a common configuration in both laboratory and commercial electrodes.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "DoubleCoatedElectrode",
     "hasCoating": [
       {
         "@type": "BaseCoating",
         "hasActiveMaterial": { "@type": "LiNi0.8Mn0.1Co0.1O2" },
         "hasBinder": { "@type": "PVDF" },
         "hasAdditive": { "@type": "CarbonBlack" }
       },
       {
         "@type": "TopCoating",
         "hasActiveMaterial": { "@type": "LiMn2O4" },
         "hasBinder": { "@type": "PVDF" },
         "hasAdditive": { "@type": "CarbonBlack" }
       }
     ],
     "hasCurrentCollector": { "@type": "AluminiumFoil" },
     "hasProperty": [
       {
         "@type": "Thickness",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 150 },
         "hasMeasurementUnit": "emmo:MicroMetre"
       }
     ]
   }

Here, the two coatings can represent different active materials or formulations applied to each side of the foil.  
This pattern can also be extended for gradient or layered electrodes.

Reasoning Implications
----------------------

Because `hasCoating`, `hasCurrentCollector`, `hasActiveMaterial`, etc. are all **subproperties of `hasPart`**, reasoning engines can infer relationships such as:

::
   If Electrode hasCoating Coating,
   and Coating hasActiveMaterial Material,
   then Electrode hasPart Material.

This enables queries like “find all electrodes that contain a given active material,” regardless of how deeply it is nested in the structure.

Best Practices
--------------

- Use `Anode` and `Cathode` when polarity or reaction direction is known; use `Electrode` when not.  
- When modeling coatings, prefer `SingleCoatedElectrode` or `DoubleCoatedElectrode` subclasses for clarity.  
- Include `hasCurrentCollector` even for self-supporting electrodes to maintain consistency.  
- Use `hasCoating` to encapsulate active, binder, and additive materials.  
- Represent measurable properties like thickness or porosity through `hasProperty`.  
- If describing manufacturing variants, you may define coating subclasses (e.g., `BaseCoating`, `TopCoating`) for specific architectures.

Summary
-------

Electrodes link **chemical composition**, **geometric structure**, and **functional role** within electrochemical systems.  
The ontology captures this hierarchy through well-defined relations and specialized subclasses.

| Concept | Relation | Example |
|----------|-----------|----------|
| **Electrode** | `hasCoating` | functional layer of active material |
| **SingleCoatedElectrode** | `hasCoating` | one coating on current collector |
| **DoubleCoatedElectrode** | `hasCoating` | coatings on both sides |
| **ElectrodeCoating** | `hasActiveMaterial`, `hasBinder`, `hasAdditive` | describes internal composition |
| **Electrode** | `hasCurrentCollector` | connects to substrate foil |

This structure allows for rich, reusable, and machine-interpretable descriptions of electrode architectures across different experimental, modeling, and manufacturing contexts.
