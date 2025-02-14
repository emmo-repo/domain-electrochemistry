Parquet Files
=============

Parquet files encode tabular data in a binary format optimized for data compression and rapid access. 


Step 1: Describe Bibliographic and Governance metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start the JSON-LD description with the context and type, and add bibliographic and governance metadata as in [LINK TO METADATA SECTION]. 

.. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "Dataset",
        "@id": "https://doi.org/10.5281/zenodo.13318553", 
        "dc:title": "Lithium Ion Battery Test Dataset",
        ...

      }


Step 2: Describe technical and domain metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Continue with technical and domain metadata as in [LINK TO METADATA SECTION]. 

.. code-block:: json

      {
      "schema:contentSize": "4.87 MB",
      "schema:encodingFormat": "application/octet-stream"
      "@reverse": {
            "hasOutput": {"@type": "CyclicVoltammetry"}
        }

      }

Step 2: Describe the file contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We also use the *"csvw:tableSchema"* attributes of the CSVW vocabulary to annotate Parquet files. We describe each column in the same way as CSV files [LINK TO CSV]: 

.. code-block:: json

      {
        "csvw:tableSchema": {
            "csvw:primaryKey": "time",
            "csvw:columns": [{
                "csvw:name": "potential",
                "csvw:titles": "Potential vs. Li",
                "csvw:propertyUrl": "ElectricPotential",
                "hasMeasurementUnit": "emmo:MilliVolt",
                "csvw:datatype": "xsd:float",
                "csvw:required": true
            }, {
                "csvw:name": "current",
                "csvw:titles": "I",
                "csvw:propertyUrl": "ElectricCurrent",
                "hasMeasurementUnit": "emmo:MilliAmpere",
                "csvw:datatype": "xsd:float"
            }, {
                "csvw:name": "time",
                "csvw:titles": "t [s]",
                "csvw:propertyUrl": "Duration",
                "hasMeasurementUnit": "emmo:Second",
                "csvw:datatype": "xsd:float"
            }],
            
            }

      }

Thats it, you have now to place metadata and file description together in a single JSON-LD and you complete your file description.