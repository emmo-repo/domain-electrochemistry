Electrolyte Solution
--------------------

`IRI: https://w3id.org/emmo/domain/electrochemistry#electrochemistry_fa22874b_76a9_4043_8b8f_6086c88746de <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_fa22874b_76a9_4043_8b8f_6086c88746de>`_

Description
~~~~~~~~~~~
An **electrolyte solution** is a critical component in an electrochemical system that enables **ionic conductivity**, allowing charge to move between electrodes. Electrolyte solutions are typically **mixtures of solvents, solutes, and additives**, and their composition significantly impacts the performance, stability, and lifetime of the electrochemical system.

Guidelines for Use
~~~~~~~~~~~~~~~~~~

To represent an **Electrolyte Solution** in the ontology, follow these five key steps:

Step 1: Identifying the Electrolyte Solution
"""""""""""""""""""""""""""""""""""""""""

Define the electrolyte using the **ElectrolyteSolution** class. If desired, use a suitable subclass such as:
- **AqueousElectrolyte**
- **AcidicElectrolyte**
- **AlkalineElectrolyte**
- **OrganicElectrolyte**

**Example:** Defining a generic **Aqueous Electrolyte**:

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "AqueousElectrolyte"
   }

Step 2: State the Composition of the Electrolyte Solution
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Electrolyte solutions are typically mixtures of multiple components. Use the object properties:
- **hasSolvent** to define the main solvent of the electrolyte.
- **hasSolute** to specify the dissolved ionic species.
- **hasAdditive** to include any stabilizers or functional additives.

**Example:** Defining an **aqueous potassium hydroxide electrolyte**:

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "AqueousElectrolyte",
     "hasSolvent": {
       "@type": "Water"
     },
     "hasSolute": {
       "@type": "PotassiumHydroxide"
     }
   }

Step 3: Assign Properties to the Components
""""""""""""""""""""""""""""""""""""""""""""

Each component of the electrolyte can be described with **annotation and objective properties**.

- **Annotation Properties**:
  - ``molecularFormula``: Defines the chemical composition.

- **Objective Properties**:
  - ``MassFraction``: Defines the proportion of the component in the mixture.
  - ``AmountConcentration``: Specifies the concentration of the solute.

**Example:** Adding properties to **Potassium Hydroxide**:

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "AqueousElectrolyte",
     "hasSolvent": {
       "@type": "Water"
     },
     "hasSolute": {
       "@type": "PotassiumHydroxide",
       "molecularFormula": "KOH",
       "hasProperty": [
         {
           "@type": "AmountConcentration",
           "hasNumericalPart": {
             "@type": "RealData",
             "hasNumericalValue": 1.0
           },
           "hasMeasurementUnit": "emmo:MolePerLitre"
         }
       ]
     }
   }

Step 4: Assign Properties to the Electrolyte Solution
"""""""""""""""""""""""""""""""""""""""""""""""""""""

Beyond the properties of individual components, the electrolyte solution itself has measurable properties:

- **Objective Properties**:
  - ``IonicConductivity``: Represents the ionic transport efficiency.
  - ``Viscosity``: Describes the fluid dynamics.

**Example:** Assigning properties to an **Aqueous Potassium Hydroxide Electrolyte**:

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "AqueousElectrolyte",
     "hasProperty": [
       {
         "@type": "IonicConductivity",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumericalValue": 0.12
         },
         "hasMeasurementUnit": "emmo:SiemensPerCentimetre"
       },
       {
         "@type": "Viscosity",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumericalValue": 1.0
         },
         "hasMeasurementUnit": "emmo:MilliPascalSecond"
       }
     ],
     "hasSolvent": {
       "@type": "Water"
     },
     "hasSolute": {
       "@type": "PotassiumHydroxide",
       "molecularFormula": "KOH",
       "hasProperty": [
         {
           "@type": "AmountConcentration",
           "hasNumericalPart": {
             "@type": "RealData",
             "hasNumericalValue": 1.0
           },
           "hasMeasurementUnit": "emmo:MolePerLitre"
         }
       ]
     }
   }

Step 5: Linking the Electrolyte to a Functional Whole
"""""""""""""""""""""""""""""""""""""""""""""""""""""

The final step is to associate the **Electrolyte Solution** with a functional component, such as a **BatteryCell** or **ElectrochemicalSystem**, using the ``hasElectrolyte`` property.

**Example:** Linking an **Aqueous Potassium Hydroxide Electrolyte** to a **Battery Cell**:

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "BatteryCell",
     "hasElectrolyte": {
       "@type": "AqueousElectrolyte",
       "hasProperty": [
         {
           "@type": "IonicConductivity",
           "hasNumericalPart": {
             "@type": "RealData",
             "hasNumericalValue": 0.12
           },
           "hasMeasurementUnit": "emmo:SiemensPerCentimetre"
         },
         {
           "@type": "Viscosity",
           "hasNumericalPart": {
             "@type": "RealData",
             "hasNumericalValue": 1.0
           },
           "hasMeasurementUnit": "emmo:MilliPascalSecond"
         }
       ],
       "hasSolvent": {
         "@type": "Water"
       },
       "hasSolute": {
         "@type": "PotassiumHydroxide",
         "molecularFormula": "KOH",
         "hasProperty": [
           {
             "@type": "AmountConcentration",
             "hasNumericalPart": {
               "@type": "RealData",
               "hasNumericalValue": 1.0
             },
             "hasMeasurementUnit": "emmo:MolePerLitre"
           }
         ]
       }
     }
   }

