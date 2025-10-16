Case
----

`IRI: https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1aec4cc0_82d5_4042_a657_ed7fe291c3d8 <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1aec4cc0_82d5_4042_a657_ed7fe291c3d8>`_

Description
~~~~~~~~~~~
A **case** is the outer shell of an electrochemical cell, providing structural integrity and protecting internal components from environmental exposure.

Guidelines for Use
~~~~~~~~~~~~~~~~~~

1. **Identify the Case**  
   
.. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "R2032"
      }

2. **Assign Properties**  
   
.. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "Case",
        "hasProperty": [
          {
            "@type": "Diameter",
            "hasNumericalPart": {
              "@type": "RealData",
              "hasNumericalValue": 20
            },
            "hasMeasurementUnit": "emmo:MilliMetre"
          }
        ]
      }

3. **Link the Case to a Functional Whole**  
   
.. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "ElectrochemicalDevice",
        "hasCase": {
          "@type": "Case",
          "hasProperty": [
            {
              "@type": "Diameter",
              "hasNumericalPart": {
                "@type": "RealData",
                "hasNumericalValue": 20
              },
              "hasMeasurementUnit": "emmo:MilliMetre"
            }
          ]
        }
      }
