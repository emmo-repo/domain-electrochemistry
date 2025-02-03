Active Material
---------------

`IRI: https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79d1b273_58cd_4be6_a250_434817f7c261 <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79d1b273_58cd_4be6_a250_434817f7c261>`_

Description 
~~~~~~~~~~~
The **active material**, also known as the **electrochemically active material**, is a key component of an electrochemical system that undergoes an electrochemical reaction (oxidation or reduction) at an electrode. These reactions are responsible for enabling energy storage and release in devices such as batteries.

For example, during the discharging of an electrochemical cell:
- The active material on the **anode** is oxidized, releasing electrons.
- The active material on the **cathode** is reduced, consuming electrons.

Here are some commonly used active materials in electrochemical systems:

.. list-table:: Common Active Materials
   :header-rows: 1

   * - Name
     - Label
     - IRI
   * - Zinc
     - ``Zinc``
     - `IRI: https://w3id.org/emmo/domain/chemical-substance#substance_9bd78e1c_a4dc_41b6_8013_adb51df1ffdc <https://w3id.org/emmo/domain/chemical-substance#substance_9bd78e1c_a4dc_41b6_8013_adb51df1ffdc>`_
   * - Manganese Dioxide
     - ``ManganeseDioxide``
     - `IRI: https://w3id.org/emmo/domain/chemical-substance#substance_dcdbdbed_2e20_40d1_a7a5_5761de7f0618 <https://w3id.org/emmo/domain/chemical-substance#substance_dcdbdbed_2e20_40d1_a7a5_5761de7f0618>`_
   * - Graphite
     - ``Graphite``
     - `IRI: https://w3id.org/emmo/domain/chemical-substance#substance_d53259a7_0d9c_48b9_a6c1_4418169df303 <https://w3id.org/emmo/domain/chemical-substance#substance_d53259a7_0d9c_48b9_a6c1_4418169df303>`_


Guidelines for Use 
~~~~~~~~~~~~~~~~~~

To represent an **Active Material** in the ontology, follow three key steps:

1. **Identify the Material**  
   Determine what the material is by combining terms from the **domain-chemical-substance ontology** with the **ActiveMaterial** class in the electrochemistry domain.

2. **Assign Properties**  
   Define the material's attributes using **annotation properties** (e.g., ``molecularFormula``) and **quantitative properties** (e.g., ``Density``, ``SpecificCapacity``).

3. **Link the Material to a Functional Whole**  
   Use object properties like ``hasActiveMaterial`` to connect the material to an ``Electrode`` or ``ElectrodeCoating``.

Step 1: Identifying the Active Material
"""""""""""""""""""""""""""""""""""""""

Begin by defining the **chemical identity** of the material. This includes assigning it a **class** and a **name** that aligns with established chemical substance ontologies.

**Example:** Defining **Zinc** as an active material:

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": ["ActiveMaterial", "Zinc"]
   }

Step 2: Assigning Properties
""""""""""""""""""""""""""""

Once the material is identified, define its **intrinsic properties** using annotation and quantitative properties.

- **Annotation Properties**:
  - ``molecularFormula``: Defines the chemical composition.

- **Objective Properties**:
  - ``Density``: Specifies the material’s density.
  - ``SpecificCapacity``: Describes the charge storage capacity per unit mass.

**Example:** Adding properties to **Zinc**:

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": ["ActiveMaterial", "Zinc"],
     "molecularFormula": "Zn",
     "hasProperty": [
       {
         "@type": "Density",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumberValue": 7.14
         },
         "hasMeasurementUnit": "emmo:GramPerCubicCentiMetre"
       },
       {
         "@type": "SpecificCapacity",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumberValue": 820
         },
         "hasMeasurementUnit": "emmo:MilliAmpereHourPerGram"
       }
     ]
   }

Step 3: Linking the Active Material to a Functional Whole
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The final step is to **associate the active material with a functional component**, such as an ``Electrode`` or ``ElectrodeCoating``, using the ``hasActiveMaterial`` property.

**Example:** Linking **Zinc** to an **Electrode**:

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "Electrode",
     "hasActiveMaterial": {
       "@type": "Zinc"
     }
   }

**Example:** Linking **Zinc** to an **Electrode Coating**:

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "CoatedElectrode",
     "hasCoating": {
        "@type": "ElectrodeCoating",
        "hasActiveMaterial": {
            "@type": "Zinc"
        }
     }
   }

By following these three steps — **identifying the material, assigning properties, and linking it to a functional structure** — active materials are consistently defined within the ontology, ensuring semantic clarity and interoperability.

.. tip:: Predefined Electrode Classes with Linked Active Materials

   For very common active material types, especially those covered by IEC designations, the ontology provides specific electrode classes where the type of active material is already linked. These predefined classes can save time if you just want to convey the type of active material used in a general way.

   For example, the ``ZincElectrode`` class in the ontology already links the active material ``Zinc`` to the electrode.

   **To represent a generic zinc electrode**:
   
.. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "ZincElectrode"
      }

   For cases where you want to say that your electrode uses a **specific kind of zinc material**, then you can still use the ``hasActiveMaterial`` property in the same way:
   
.. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "ZincElectrode",
        "hasActiveMaterial": {
            "@type": "Zinc",
            "@id": "https://www.example.com/Your_Specific_Zinc_Material_Identifier"
      } 
