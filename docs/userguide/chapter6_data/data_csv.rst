CSV Files
=========

CSV files encode tabular data as text. The rows are separated by commas or a similar punctuation mark (colons, semicolons), and the first row labels the attributes.

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Continue with technical and domain metadata as in [LINK TO METADATA SECTION]. 

.. code-block:: json

      {
      "schema:contentSize": "138 kB",
      "schema:encodingFormat": "text/csv"
      "@reverse": {
            "hasOutput": {"@type": "CyclicVoltammetry"}
        }

      }


Step 3: Describe the file contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the *"csvw:tableSchema"* attributes of the CSVW vocabulary to annotate CSV file attributes. Describe each column with: 

* *"csvw:name"*: arbitrary name we assign to the column to refer to it within the JSON-LD file.
* *"csvw:title"*: label of the column as it appear in the first row of the file.
* *"csvw:propertyUrl"*: the class name of the quantity the column represents. Remember that class names are linked to unique identifiers in the @context field.
* *"hasMeasurementUnit"*: the class name of the units of the quantity.
* *"csvw:datatype"*: describes the facets of a data type, and ususally expects the data types described by the `XML schema <https://www.w3.org/TR/xmlschema11-2/>`_ , for instance, "string", "integer", "float", "boolean", "decimal", etc.  As a reminder, the "xsd:" prefix is the usual string we use to make explicit that what follows the prefix is defined in the XML schema. 
* *"csvw:required"*: boolean specifying whether the column must be part of the file, either because it is the primary key (see below) or becuase it is required by the application. For instance, in Cyclic Voltammetry we must encode at least voltages and currents for the dataset to be complete, and we might optionally include secondary measurements such as current density, temperature, rotating speed of an electrode, etc.

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

Note that in addition to the columns, we should also specify a *"csvw:primaryKey"*, i.e. which of the column(s) available in the file are unique for each row, and thus can be used to uniquely identify (or index) each row.


Step 4: Describe the file dialect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The CSV file dialect is the specific formatting rules of how the data is written in the file, such as the delimiter, the character set used for encoding, line terminator, etc. These attributes provide file processors with clues on how to parse the file.  

.. code-block:: json

    {
    "dialect": {
        "delimiter": ",",
        "quoteChar": "\"",
        "encoding": "utf-8",
        "header": true
        }
    }


Thats it, you have now to place metadata and file description together in a single JSON-LD and you complete your file description.