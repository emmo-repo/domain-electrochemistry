Materials
=========

Materials are the physical substances that make up electrochemical systems. Understanding how to represent materials in the ontology is crucial for:
- Describing experimental setups  
- Ensuring reproducibility  
- Enabling data comparison  
- Supporting material selection  

This section provides an overview for how materials are used in the EMMO universe generally, along with specific examples from the electrochemistry domain. 

Active Material
---------------

`IRI: https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79d1b273_58cd_4be6_a250_434817f7c261 <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79d1b273_58cd_4be6_a250_434817f7c261>`_

**Description**  
The **active material**, also known as the **electrochemically active material**, is a key component of an electrochemical system that undergoes an electrochemical reaction (oxidation or reduction) at an electrode. These reactions are responsible for enabling energy storage and release in devices such as batteries.

For example, during the discharging of an electrochemical cell:
- The active material on the **anode** is oxidized, releasing electrons.
- The active material on the **cathode** is reduced, consuming electrons.

The active material determines the cell's capacity, voltage, and energy density, making it one of the most critical aspects of any electrochemical device.

**Examples of Active Materials**  
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
   * - Lithium Iron Phosphate
     - ``LithiumIronPhosphate``
     - `IRI: https://w3id.org/emmo/domain/chemical-substance#substance_aa8e9cc4_5f66_4307_b1c8_26fac7653a90 <https://w3id.org/emmo/domain/chemical-substance#substance_aa8e9cc4_5f66_4307_b1c8_26fac7653a90>`_

**Usage**  
To describe an active material in the ontology, start by defining its properties. The active material can then be linked to an ``Electrode`` or ``ElectrodeCoating`` object using the property ``hasActiveMaterial``. This property establishes the relationship between the electrode or its coating and the active material responsible for the electrochemical reaction.

**Steps to Describe an Active Material with the Ontology**:  

1. **Define the Active Material**:  
   Specify the properties of the active material itself, such as its chemical composition, physical state, and relevant characteristics. Use ontology properties to describe these attributes.
   Common annotation properties for an active material include:
   - ``molecularFormula``: Defines the chemical formula or composition of the material.

   Common objective properties for an active material include:
   - ``Density``: Specifies the density of the material.
   - ``SpecificCapacity``: Describes the amount of electric charge per unit mass the material can store.

   .. admonition:: Example  
      Here’s an example of how to describe the properties of **Lithium Iron Phosphate**:

      .. code-block:: json
         {
           "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
           "@type": ["ActiveMaterial", "LithiumIronPhosphate"],
           "molecularFormula": "LiFePO4",
           "hasProperty": [
            {
                "@type": "Density",
                "hasNumericalPart": {
                    "@type": "Real",
                    "hasNumericalValue": 3.6
                },
                "hasMeasurementUnit": "emmo:GramPerCubicCentiMetre"
            },
            {
                "@type": "SpecificCapacity",
                "hasNumericalPart": {
                    "@type": "Real",
                    "hasNumericalValue": 150
                },
                "hasMeasurementUnit": "emmo:MilliAmpereHourPerGram"
            }
           ]
         }

2. **Link the Active Material to an Electrode or Coating**:  
   Once the active material is defined, associate it with an ``Electrode`` or ``ElectrodeCoating`` object. Use the ``hasActiveMaterial`` property to establish this relationship.

   .. admonition:: Example  
      Here’s an example of how to link an active material to an electrode or coating:

      - To link **Zinc** to an electrode:
        .. code-block:: json

           {
             "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
             "@type": "Electrode",
             "hasActiveMaterial": {
               "@type": "Zinc"
             }
           }

      - To link **Graphite** to an electrode coating:
        .. code-block:: json

           {
             "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
             "@type": "CoatedElectrode",
             "hasCoating": {
                "@type": "ElectrodeCoating",
                "hasActiveMaterial": {
                    "@type": "Graphite"
                }
             }
           } 


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

**Additional Examples and Resources**
- Templates:
- JSON-LD examples:
- Jupyter notebooks:   

Electrolyte
-----------

Binder
------

Other Materials
---------------

