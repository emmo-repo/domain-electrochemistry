Separator
---------

`IRI: https://w3id.org/emmo/domain/electrochemistry#electrochemistry_331e6cca_f260_4bf8_af55_35304fe1bbe0 <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_331e6cca_f260_4bf8_af55_35304fe1bbe0>`_

Description
~~~~~~~~~~~
A **separator** is a porous membrane that electrically insulates the anode and cathode while allowing ionic conductivity. It prevents short circuits while enabling ion transport.

Guidelines for Use
~~~~~~~~~~~~~~~~~~

1. **Identify the Separator**  
   
.. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "Separator"
      }

2. **Assign Properties**  
   
.. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "Separator",
        "hasProperty": [
          {
            "@type": "Thickness",
            "hasNumericalPart": {
              "@type": "RealData",
              "hasNumericalValue": 20
            },
            "hasMeasurementUnit": "emmo:MicroMetre"
          }
        ]
      }

3. **Link the Separator to a Functional Whole**  
   
.. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "ElectrochemicalDevice",
        "hasSeparator": {
          "@type": "Separator",
          "hasProperty": [
            {
              "@type": "Thickness",
              "hasNumericalPart": {
                "@type": "RealData",
                "hasNumericalValue": 20
              },
              "hasMeasurementUnit": "emmo:MicroMetre"
            }
          ]
        }
      }
