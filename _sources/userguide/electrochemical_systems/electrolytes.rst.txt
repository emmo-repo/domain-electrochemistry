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

.. figure:: ../../assets/img/fig/png/electrolyte_types.png
   :align: center
   :alt: Electrolyte types
   :width: 75%

   Overview of major electrolyte types and their compositions.

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
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 1.0 },
         "hasMeasurementUnit": "emmo:MolePerLitre"
       }
     }
   }


4. Assign Properties to the Electrolyte
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Beyond component-level data, the **electrolyte as a whole** has measurable bulk properties that characterize performance.

Common examples include:

- `IonicConductivity`  
- `Viscosity`  
- `Density`  
- `DielectricConstant`  

**Example: aqueous KOH electrolyte with conductivity and viscosity**

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "AqueousElectrolyte",
     "hasProperty": [
       {
         "@type": "IonicConductivity",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 0.12 },
         "hasMeasurementUnit": "emmo:SiemensPerCentimetre"
       },
       {
         "@type": "Viscosity",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 1.0 },
         "hasMeasurementUnit": "emmo:MilliPascalSecond"
       }
     ],
     "hasSolvent": { "@type": "Water" },
     "hasSolute": {
       "@type": "PotassiumHydroxide",
       "molecularFormula": "KOH",
       "hasProperty": {
         "@type": "AmountConcentration",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 1.0 },
         "hasMeasurementUnit": "emmo:MolePerLitre"
       }
     }
   }

5. Represent Other Electrolyte Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Different physical forms require slightly different modeling patterns.  
Below are examples for common types beyond aqueous solutions.

Solid Electrolyte
"""""""""""""""""

Solid electrolytes are typically crystalline or glassy ionic conductors, often modeled as individual materials rather than mixtures.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "SolidElectrolyte",
     "hasConstituent": { "@type": "LithiumPhosphorusOxynitride" },
     "hasProperty": [
       {
         "@type": "IonicConductivity",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 1.5e-4 },
         "hasMeasurementUnit": "emmo:SiemensPerCentimetre"
       }
     ]
   }

Polymer Electrolyte
"""""""""""""""""""

Polymer electrolytes consist of a polymer matrix and a dissolved salt, optionally with additives.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "PolymerElectrolyte",
     "hasPolymerMatrix": { "@type": "PolyEthyleneOxide" },
     "hasSolute": { "@type": "LithiumTriflate" },
     "hasAdditive": { "@type": "SilicaNanoparticle" },
     "hasProperty": {
       "@type": "IonicConductivity",
       "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 8e-5 },
       "hasMeasurementUnit": "emmo:SiemensPerCentimetre"
     }
   }

Ionic Liquid Electrolyte
""""""""""""""""""""""""

Ionic liquids can be modeled as self-contained ionic systems where the solvent and solute are indistinguishable.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "IonicLiquidElectrolyte",
     "hasConstituent": { "@type": "1-Ethyl-3-MethylimidazoliumTetrafluoroborate" },
     "hasProperty": {
       "@type": "Viscosity",
       "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 35 },
       "hasMeasurementUnit": "emmo:MilliPascalSecond"
     }
   }



Reasoning and Relations
-----------------------

Because relations like `hasSolvent`, `hasSolute`, and `hasAdditive` are **subproperties of `hasConstituent`**,  
reasoning engines can automatically infer composition relationships such as:

::
   If Electrolyte hasSolvent Water,
   then Electrolyte hasConstituent Water.

This allows generic queries for `hasConstituent` to retrieve all relevant parts, regardless of their specific role.

Likewise, defining `IonicConductivity` or `Viscosity` as subclasses of `Property` enables unit and dimensional validation — ensuring, for example, that only compatible units are used.

Best Practices
--------------

- Always include at least one **solvent** and one **solute** for liquid electrolytes.  
- Use **quantitative properties** for concentrations, conductivities, or viscosities.  
- Avoid duplicating roles: a compound should appear once as `hasSolute`, `hasSolvent`, or `hasAdditive`.  
- Use **non-SI units** (e.g., `MolePerLitre`, `MilliPascalSecond`) where standard in the field but still formally defined in EMMO.  
- For polymer or solid electrolytes, prefer `hasConstituent` or domain-specific relations (`hasPolymerMatrix`, `hasSalt`) over solvent/solute roles.  
- Reference materials (like “LiPF6” or “Water”) using ontology terms that include external links (e.g., Wikidata, PubChem) for interoperability.  


Summary
-------

Electrolytes are **ion-conducting media** whose structure and composition determine electrochemical performance.  
The ontology provides a modular way to represent electrolytes of any kind — liquid, solid, or polymeric — and to connect their materials and properties logically.

| Concept | Relation | Example |
|----------|-----------|----------|
| **ElectrolyteSolution** | `hasSolvent`, `hasSolute`, `hasAdditive` | water–KOH solution |
| **SolidElectrolyte** | `hasConstituent` | LiPON film |
| **PolymerElectrolyte** | `hasPolymerMatrix`, `hasSolute` | PEO–LiTFSI |
| **Electrolyte** | `hasProperty` | ionic conductivity, viscosity |
| **Relations** | `hasConstituent` (superproperty) | enables reasoning across types |

By following these conventions, you can describe electrolytes in a consistent, machine-readable way that supports data linking, querying, and reasoning across electrochemical domains.
