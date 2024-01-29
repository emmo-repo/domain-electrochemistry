Cyclic Voltammetry Data
=======================

This example, let's describe an instance of some data resulting from a cyclic voltammetry measurement. The JSON-LD description of the material is given below:

.. tab-set::

   .. tab-item:: Raw Data

      .. csv-table:: Example CSV Data
         :header: "Potential v. Li", "I", "Current density"
         :file: /assets/data/example-cyclic-voltammetry.csv
         :widths: 20, 20, 20


   .. tab-item:: JSON

      .. code-block:: json
         :linenos:

         {
            "@context": "https://raw.githubusercontent.com/emmo-repo/domain-electrochemistry/master/context.json",
            "@type": "MeasurementResult",
            "csvw:url": "https://archive.big-map.eu/records/24mdd-z2x02/files/LNO%20CV.csv",
            "dc:title": "Example Cyclic Voltammetry Data",
            "dcat:keyword": ["cyclic voltammetry", "LNO", "battery"],
            "dc:license": "BIG-MAP Archive License",
            "dc:modified": {"@value": "2024-01-29", "@type": "xsd:date"},
            "dc:creator": {
               "@id": "https://orcid.org/0000-0002-9401-1362",
               "schema:name": "Christian Wolke"
            },
            "dc:contributor": {
               "@id": "https://orcid.org/0000-0002-8758-6109",
               "schema:name": "Simon Clark"
            },
            "@reverse": {
               "hasOutput": {
               "@type": "CyclicVoltammetry"
               }
            },
            "csvw:tableSchema": {
               "csvw:columns": [{
                  "csvw:name": "potential",
                  "csvw:titles": "Potential vs. Li",
                  "csvw:propertyUrl": "ElectricPotential",
                  "hasMeasurementUnit": "emmo:MilliVolt",
                  "csvw:datatype": "number",
                  "csvw:required": true
               }, {
                  "csvw:name": "current",
                  "csvw:titles": "I",
                  "csvw:propertyUrl": "ElectricCurrent",
                  "hasMeasurementUnit": "emmo:MilliAmpere",
                  "csvw:datatype": "number"
               }, {
                  "csvw:name": "current density",
                  "csvw:titles": "Current density",
                  "csvw:propertyUrl": "ElectricCurrentDensity",
                  "hasMeasurementUnit": "emmo:MilliAmperePerSquareCentiMetre",
                  "csvw:datatype": "number"
               }],
               "csvw:primaryKey": "potential"
               }
         }

   .. tab-item:: JSON-LD Playground

      .. raw:: html
         
         <div style="position: relative; padding-top: 56.25%; height: 0;">
            <iframe src="https://json-ld.org/playground/#startTab=tab-canonized&json-ld=%7B%22%40context%22%3A%22https%3A%2F%2Fraw.githubusercontent.com%2Femmo-repo%2Fdomain-electrochemistry%2Fmaster%2Fcontext.json%22%2C%22%40type%22%3A%22MeasurementResult%22%2C%22dc%3Atitle%22%3A%22Example%20Cyclic%20Voltammetry%20Data%22%2C%22dcat%3Akeyword%22%3A%5B%22cyclic%20voltammetry%22%2C%22LNO%22%2C%22battery%22%5D%2C%22dc%3Alicense%22%3A%22BIG-MAP%20Archive%20License%22%2C%22dc%3Amodified%22%3A%7B%22%40value%22%3A%222024-01-29%22%2C%22%40type%22%3A%22xsd%3Adate%22%7D%2C%22dc%3Acreator%22%3A%7B%22%40id%22%3A%22https%3A%2F%2Forcid.org%2F0000-0002-9401-1362%22%2C%22schema%3Aname%22%3A%22Christian%20Wolke%22%7D%2C%22dc%3Acontributor%22%3A%7B%22%40id%22%3A%22https%3A%2F%2Forcid.org%2F0000-0002-8758-6109%22%2C%22schema%3Aname%22%3A%22Simon%20Clark%22%7D%2C%22%40reverse%22%3A%7B%22hasOutput%22%3A%7B%22%40type%22%3A%22CyclicVoltammetry%22%7D%7D%2C%22csvw%3AtableSchema%22%3A%7B%22csvw%3Acolumns%22%3A%5B%7B%22csvw%3Aname%22%3A%22potential%22%2C%22csvw%3Atitles%22%3A%22Potential%20vs.%20Li%22%2C%22csvw%3ApropertyUrl%22%3A%22ElectricPotential%22%2C%22hasMeasurementUnit%22%3A%22emmo%3AMilliVolt%22%2C%22csvw%3Adatatype%22%3A%22number%22%2C%22csvw%3Arequired%22%3Atrue%7D%2C%7B%22csvw%3Aname%22%3A%22current%22%2C%22csvw%3Atitles%22%3A%22I%22%2C%22csvw%3ApropertyUrl%22%3A%22ElectricCurrent%22%2C%22hasMeasurementUnit%22%3A%22emmo%3AMilliAmpere%22%2C%22csvw%3Adatatype%22%3A%22number%22%7D%2C%7B%22csvw%3Aname%22%3A%22current%20density%22%2C%22csvw%3Atitles%22%3A%22Current%20density%22%2C%22csvw%3ApropertyUrl%22%3A%22ElectricCurrentDensity%22%2C%22hasMeasurementUnit%22%3A%22emmo%3AMilliAmperePerSquareCentiMetre%22%2C%22csvw%3Adatatype%22%3A%22number%22%7D%5D%2C%22csvw%3AprimaryKey%22%3A%22potential%22%7D%7D" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" frameborder="0" allowfullscreen></iframe>
         </div>

This example highlights a few things:

#. **EMMO distinguishes properties according to how they were determined.** In this example, a ``ConventionalProperty`` is a property whose value is assigned by convention (e.g. from a technical specification sheet, handbook, etc.). EMMO also provides terms for ``MeasuredProperty`` for properties which were actually determined by some measurement and ``ModelledProperty`` for properties that were obtained from some model. 

#. **EMMO has a specific way of expressing quantitative properties.** As shown in the example, a quantitative property has a ``@type`` that describes what kind of property it is, ``hasNumericalPart`` describes the value, and ``hasMeasurementUnit`` defines the unit. Please adhere to this format when expressing quantities in your linked data. 

#. **We can re-use terms from common vocabularies like schema.org.** One of the core principles of linked data is to re-use existing vocabularies when possible. The schema.org vocabulary was developed to support internet search engines and contains terms for things that people often search for (e.g. people, organizations, products, etc.) In this case, we can re-use schema.org terms to describe the manufacturer and product.  

