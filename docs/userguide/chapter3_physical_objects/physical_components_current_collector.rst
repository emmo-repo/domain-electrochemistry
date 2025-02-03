Current Collector
-----------------

`IRI: https://w3id.org/emmo/domain/electrochemistry#electrochemistry_212af058_3bbb_419f_a9c6_90ba9ebb3706 <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_212af058_3bbb_419f_a9c6_90ba9ebb3706>`_

Description
~~~~~~~~~~~
A **current collector** is a conductive component in an electrochemical cell that facilitates the transfer of electrons between the external circuit and the electrode material. Current collectors do not participate in the electrochemical reaction but play a crucial role in minimizing resistance and ensuring efficient electron flow.

Guidelines for Use
~~~~~~~~~~~~~~~~~~

To represent a **Current Collector** in the ontology, follow three key steps:

1. **Identify the Current Collector**  
   .. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": ["CurrentCollector", "Copper", "Foil"]
      }

2. **Assign Properties**  
   .. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "CurrentCollector",
        "hasProperty": [
          {
            "@type": "Thickness",
            "hasNumericalPart": {
              "@type": "RealData",
              "hasNumericalValue": 10
            },
            "hasMeasurementUnit": "emmo:MicroMetre"
          }
        ]
      }

3. **Link the Current Collector to a Functional Whole**  
   .. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "Electrode",
        "hasCurrentCollector": {
          "@type": "CurrentCollector"
        }
      }
