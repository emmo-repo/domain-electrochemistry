Electrolytes
============

Description
-----------

An **electrolyte** is the medium that allows ions to move between electrodes in an electrochemical system. It provides **ionic conductivity** while typically remaining electronically insulating. Electrolytes may exist as **liquids**, **solids**, or **gels**, and can be composed of **solvents**, **solutes**, and **functional additives**.

Electrolytes strongly influence the performance, stability, and lifetime of electrochemical devices — making them essential to describe precisely and consistently.

Common electrolyte classes include:

- **ElectrolyteSolution** — liquid mixtures of solvents, solutes, and additives  
- **SolidElectrolyte** — crystalline or amorphous solids that conduct ions  
- **PolymerElectrolyte** — polymer matrices that host ionic conduction  
- **IonicLiquidElectrolyte** — molten salts or room-temperature ionic liquids  

Guidelines for Use
------------------

Follow these steps when representing an electrolyte in the ontology.

1. Identify the Electrolyte Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Begin by defining the appropriate class, depending on the physical state or composition.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ElectrolyteSolution"
   }

Common subclasses include:

- `AqueousElectrolyte`
- `OrganicElectrolyte`
- `PolymerElectrolyte`
- `SolidElectrolyte`

These subclasses provide semantic precision for reasoning and data integration.

2. Define the Composition
^^^^^^^^^^^^^^^^^^^^^^^^^

Electrolytes are mixtures, so use **domain-specific relations** to describe the constituents:

- `hasSolvent` — the main liquid phase (e.g., water, EC, EMC)  
- `hasSolute` — the dissolved ionic compound or salt (e.g., LiPF6, KOH)  
- `hasAdditive` — additional components that modify stability or performance (e.g., FEC, VC)

**Example: aqueous potassium hydroxide electrolyte**

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "AqueousElectrolyte",
     "hasSolvent": { "@type": "Water" },
     "hasSolute": { "@type": "PotassiumHydroxide" }
   }

Each constituent can itself have properties, such as **molecular formula**, **mass fraction**, or **concentration**.


3. Describe Component Properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Attach quantitative or descriptive properties to components using `hasProperty`.

- `AmountConcentration` — molar concentration  
- `MassFraction` — weight proportion  
- `MolecularFormula` — chemical annotation  

**Example: including solute concentration**

.. code-block:: json

   {
     "@type": "AqueousElectrolyte",
     "hasSolvent": { "@type": "Water" },
     "hasSolute": {
       "@type": "PotassiumHydroxide",
       "molecularFormula": "KOH",
       "hasProperty": {
         "@type": "AmountConcentration",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 1000 },
         "hasMeasurementUnit": "MolePerCubicMetre"
       }
     }
   }

The concentration is given in the SI-coherent unit ``MolePerCubicMetre`` (1000 mol/m³ = 1 mol/L) because the ontology does not yet define a mole-per-litre unit.

4. Assign Properties to the Electrolyte
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Beyond component-level data, the **electrolyte as a whole** has measurable bulk properties that characterize performance.

Common examples include:

- `IonicConductivity`
- `DynamicViscosity`
- `Density`
- `RelativePermittivity`

**Example: aqueous KOH electrolyte with conductivity and viscosity**

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "AqueousElectrolyte",
     "hasProperty": [
       {
         "@type": "IonicConductivity",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 12 },
         "hasMeasurementUnit": "SiemensPerMetre"
       },
       {
         "@type": "DynamicViscosity",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 1.0 },
         "hasMeasurementUnit": "MilliPascalSecond"
       }
     ],
     "hasSolvent": { "@type": "Water" },
     "hasSolute": {
       "@type": "PotassiumHydroxide",
       "molecularFormula": "KOH",
       "hasProperty": {
         "@type": "AmountConcentration",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 1000 },
         "hasMeasurementUnit": "MolePerCubicMetre"
       }
     }
   }

5. Represent Other Electrolyte Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Different physical forms require slightly different modeling patterns.  
Below are examples for common types beyond aqueous solutions.

Solid Electrolyte
"""""""""""""""""

Solid electrolytes are typically crystalline or glassy ionic conductors, often modeled as individual materials rather than mixtures. When the ontology has no named class for a specific compound (here LiPON), type it as a `ChemicalCompound` and identify it with `molecularFormula`.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "SolidElectrolyte",
     "hasConstituent": {
       "@type": "ChemicalCompound",
       "molecularFormula": "Li2.9PO3.3N0.46"
     },
     "hasProperty": [
       {
         "@type": "IonicConductivity",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 0.015 },
         "hasMeasurementUnit": "SiemensPerMetre"
       }
     ]
   }

Polymer Electrolyte
"""""""""""""""""""

Polymer electrolytes consist of a polymer matrix and a dissolved salt, optionally with additives. The matrix is a constituent; the salt keeps its solute role.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "PolymerElectrolyte",
     "hasConstituent": { "@type": "PolyethyleneGlycol" },
     "hasSolute": { "@type": "LithiumTriflate" },
     "hasProperty": {
       "@type": "IonicConductivity",
       "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 0.008 },
       "hasMeasurementUnit": "SiemensPerMetre"
     }
   }

Ionic Liquid Electrolyte
""""""""""""""""""""""""

Ionic liquids can be modeled as self-contained ionic systems where the solvent and solute are indistinguishable.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "IonicLiquidElectrolyte",
     "hasConstituent": {
       "@type": "ChemicalCompound",
       "molecularFormula": "C6H11BF4N2"
     },
     "hasProperty": {
       "@type": "DynamicViscosity",
       "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 35 },
       "hasMeasurementUnit": "MilliPascalSecond"
     }
   }

The constituent here is 1-ethyl-3-methylimidazolium tetrafluoroborate, identified by molecular formula since the ontology has no named class for it.



Reasoning and Relations
-----------------------

Because relations like `hasSolvent`, `hasSolute`, and `hasAdditive` are **subproperties of `hasConstituent`**,
reasoning engines can automatically infer composition relationships such as:

.. code-block:: text

   If Electrolyte hasSolvent Water,
   then Electrolyte hasConstituent Water.

This allows generic queries for `hasConstituent` to retrieve all relevant parts, regardless of their specific role.

Likewise, defining `IonicConductivity` or `DynamicViscosity` as subclasses of `Property` enables unit and dimensional validation — ensuring, for example, that only compatible units are used.

Best Practices
--------------

- Always include at least one **solvent** and one **solute** for liquid electrolytes.
- Use **quantitative properties** for concentrations, conductivities, or viscosities.
- Avoid duplicating roles: a compound should appear once as `hasSolute`, `hasSolvent`, or `hasAdditive`.
- Reference units by their bare context label (`SiemensPerMetre`, `MilliPascalSecond`). When the field-standard unit is not in the ontology (mole per litre, for instance), convert the value to an available unit like `MolePerCubicMetre`.
- For polymer or solid electrolytes, prefer `hasConstituent` over solvent/solute roles when the roles do not apply.
- Reference materials (like "LiPF6" or "Water") using ontology terms that include external links (e.g., Wikidata, PubChem) for interoperability; fall back to `ChemicalCompound` plus `molecularFormula` for compounds the ontology does not name.


Summary
-------

Electrolytes are **ion-conducting media** whose structure and composition determine electrochemical performance.  
The ontology provides a modular way to represent electrolytes of any kind — liquid, solid, or polymeric — and to connect their materials and properties logically.

.. list-table::
   :header-rows: 1
   :widths: 30 40 30

   * - Concept
     - Relation
     - Example
   * - **ElectrolyteSolution**
     - `hasSolvent`, `hasSolute`, `hasAdditive`
     - water-KOH solution
   * - **SolidElectrolyte**
     - `hasConstituent`
     - LiPON film
   * - **PolymerElectrolyte**
     - `hasConstituent`, `hasSolute`
     - polymer matrix with lithium triflate
   * - **Electrolyte**
     - `hasProperty`
     - ionic conductivity, viscosity
   * - **Relations**
     - `hasConstituent` (superproperty)
     - enables reasoning across types

By following these conventions, you can describe electrolytes in a consistent, machine-readable way that supports data linking, querying, and reasoning across electrochemical domains.
