Electrode
---------

`IRI: https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0f007072_a8dd_4798_b865_1bf9363be627 <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0f007072_a8dd_4798_b865_1bf9363be627>`_

Description
~~~~~~~~~~~
An **electrode** is a key component in an electrochemical system where oxidation and reduction reactions occur. Electrodes store and release charge during operation and are composed of active materials, conductive additives, and binders.

Common types of electrodes include:
- **Anode** (negative electrode during discharge)
- **Cathode** (positive electrode during discharge)

Guidelines for Use
~~~~~~~~~~~~~~~~~~

1. **Identify the Electrode**  
   .. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "Electrode"
      }

2. **Assign Properties**  
   .. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "Electrode",
        "hasProperty": [
          {
            "@type": "Thickness",
            "hasNumericalPart": {
              "@type": "RealData",
              "hasNumericalValue": 50
            },
            "hasMeasurementUnit": "emmo:MicroMetre"
          }
        ]
      }

3. **Link the Electrode to a Functional Whole or Other Components**  
   .. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "ElectrochemicalDevice",
        "hasElectrode": {
          "@type": "Electrode",
          "hasProperty": [
            {
              "@type": "Thickness",
              "hasNumericalPart": {
                "@type": "RealData",
                "hasNumericalValue": 50
              },
              "hasMeasurementUnit": "emmo:MicroMetre"
            }
          ],
          "hasActiveMaterial": {
            "@type": "Zinc"
          }
        }
      }
