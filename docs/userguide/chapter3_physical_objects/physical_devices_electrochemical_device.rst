Electrochemical Device
----------------------

`IRI: https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0acd0fc2_1048_4604_8e90_bf4e84bd87df <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0acd0fc2_1048_4604_8e90_bf4e84bd87df>`_

Description
~~~~~~~~~~~
An **Electrochemical Device** is a system composed of electrochemical components that enables energy storage, conversion, or chemical transformation. These devices integrate multiple structural and functional elements to facilitate electrochemical processes efficiently.

Guidelines for Use
~~~~~~~~~~~~~~~~~~

To represent an **Electrochemical Device** in the ontology, follow three key steps:

1. **Identify the Electrochemical Device**  
   Define the component using the **ElectrochemicalDevice** class and specify its type (e.g., Battery, Fuel Cell, Supercapacitor, Electrolyzer).

   
.. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "ElectrochemicalDevice",
        "hasDeviceType": "Battery"
      }

2. **Assign Properties**  
   Specify attributes such as **Nominal Voltage**, **Capacity**, **Operating Temperature**, and **Efficiency**.

   
.. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "ElectrochemicalDevice",
        "hasProperty": [
          {
            "@type": "NominalVoltage",
            "hasNumericalPart": {
              "@type": "RealData",
              "hasNumericalValue": 3.7
            },
            "hasMeasurementUnit": "emmo:Volt"
          },
          {
            "@type": "Capacity",
            "hasNumericalPart": {
              "@type": "RealData",
              "hasNumericalValue": 2000
            },
            "hasMeasurementUnit": "emmo:MilliAmpereHour"
          }
        ]
      }

3. **Link the Device to its Components**  
   Associate the device with its structural components, such as electrodes, separators, electrolytes, current collectors, and cases.

   
.. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "ElectrochemicalDevice",
        "hasElectrode": [
          {
            "@type": "Electrode",
            "hasActiveMaterial": {
              "@type": "LithiumCobaltOxide"
            }
          }
        ],
        "hasSeparator": {
          "@type": "Separator",
          "hasProperty": [
            {
              "@type": "Thickness",
              "hasNumericalPart": {
                "@type": "RealData",
                "hasNumericalValue": 25
              },
              "hasMeasurementUnit": "emmo:Micrometre"
            }
          ]
        },
        "hasElectrolyte": {
          "@type": "ElectrolyteSolution",
          "hasSolvent": {
            "@type": "EthyleneCarbonate"
          },
          "hasSolute": {
            "@type": "LithiumHexafluorophosphate"
          }
        },
        "hasCase": {
          "@type": "Case",
          "hasMaterial": "Aluminum"
        }
      }

By defining **Electrochemical Devices** in terms of their **type, properties, and components**, the ontology provides a structured and interoperable framework for modeling a wide variety of electrochemical energy systems.
