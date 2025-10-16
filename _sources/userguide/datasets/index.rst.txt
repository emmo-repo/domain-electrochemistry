Datasets
========

Datasets are how measurements, simulations, and analysis results become **linked data**. In the ontology, a dataset represents a collection of **data points** or **files** that describe or result from a process, test, or computation.

This section explains how to describe datasets, connect them to experiments, and make them machine-interpretable using EMMO and `schema.org` patterns.

1. What a Dataset Represents
----------------------------

A dataset can represent many kinds of information:

- Measurement data from an **ElectrochemicalTest**  
  (e.g., current, voltage, temperature vs. time)
- Simulation outputs  
  (e.g., potential distributions, reaction rates)
- Process monitoring logs  
  (e.g., pressure, temperature profiles)
- Derived analysis data  
  (e.g., fitted impedance spectra or extracted diffusion coefficients)

In EMMO and its domain ontologies, datasets are modeled using the class:

``schema:Dataset``

and connected to the relevant test or process via:

- ``hasInput`` — for data consumed by a process  
- ``hasOutput`` or ``hasResult`` — for data produced by a process or test  

2. Minimal Dataset Structure
----------------------------

At minimum, each dataset should define:

+----------------------+------------------------------+----------------------+
| Property             | Description                  | Example              |
+======================+==============================+======================+
| ``@type``            | Dataset type                 | ``schema:Dataset``   |
+----------------------+------------------------------+----------------------+
| ``name``             | Human-readable label         | ``"EIS_Spectrum.csv"`` |
+----------------------+------------------------------+----------------------+
| ``encodingFormat``   | MIME type                    | ``"text/csv"``       |
+----------------------+------------------------------+----------------------+
| ``distribution``     | File or download link        | ``DataDownload``     |
+----------------------+------------------------------+----------------------+
| ``variableMeasured`` | Variables or columns         | ``["Time / s", "Voltage / V"]`` |
+----------------------+------------------------------+----------------------+

**Example: Minimal Dataset**

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "schema:Dataset",
     "name": "Galvanostatic_Cycle_01.csv",
     "encodingFormat": "text/csv",
     "variableMeasured": ["Time / s", "Voltage / V", "Current / A"],
     "distribution": {
       "@type": "schema:DataDownload",
       "contentUrl": "https://zenodo.org/record/1234567/files/Cycle_01.csv",
       "encodingFormat": "text/csv"
     }
   }

3. Linking Datasets to Tests or Processes
-----------------------------------------

Datasets usually describe the results of a process or test.  
You can connect them using ``hasResult`` (for outputs) or ``hasInput`` (for input data).

**Example: Dataset linked to a test**

.. code-block:: json

   {
     "@type": "GalvanostaticChargeDischargeTest",
     "hasTestObject": { "@type": "BatteryCell" },
     "hasResult": {
       "@type": "schema:Dataset",
       "name": "Cycle_01.csv",
       "encodingFormat": "text/csv",
       "variableMeasured": ["Time / s", "Voltage / V", "Current / A"]
     }
   }

4. Describing Variables in More Detail
--------------------------------------

Variables can be described not only by their names, but also by semantic meaning and units, using ``schema:variableMeasured`` entries linked to EMMO quantities.

**Example: Semantic variable description**

.. code-block:: json

   {
     "@type": "schema:PropertyValue",
     "name": "Voltage / V",
     "propertyID": "emmo:Voltage",
     "unitText": "V"
   }

or embedded in the dataset:

.. code-block:: json

   {
     "@type": "schema:Dataset",
     "variableMeasured": [
       {
         "@type": "schema:PropertyValue",
         "name": "Voltage / V",
         "propertyID": "emmo:Voltage",
         "unitText": "V"
       },
       {
         "@type": "schema:PropertyValue",
         "name": "Current / A",
         "propertyID": "emmo:Current",
         "unitText": "A"
       }
     ]
   }

This allows automatic mapping between dataset columns and ontology-defined quantities.

5. Connecting Metadata and Provenance
-------------------------------------

A dataset can include rich metadata to describe its origin, authorship, and licensing.

.. code-block:: json

   {
     "@type": "schema:Dataset",
     "name": "INR21700_HighRate_Test",
     "creator": [
       { "@type": "schema:Person", "name": "Dr. Jane Smith" },
       {
         "@type": "schema:Organization",
         "name": "SINTEF Industry",
         "url": "https://www.sintef.no"
       }
     ],
     "dateCreated": "2025-10-01",
     "license": "https://spdx.org/licenses/CC-BY-4.0",
     "hasResult": {
       "@type": "schema:DataDownload",
       "contentUrl": "https://zenodo.org/records/12345/files/data.csv"
     }
   }

You can also link datasets to:

- **Instruments** (via ``wasGeneratedBy`` or ``hasEquipment``)
- **Projects or experiments** (via ``isPartOf``)
- **Public repositories** (via ``contentUrl`` or ``identifier`` for DOIs)

6. Grouping Datasets and Derived Data
-------------------------------------

Sometimes one test produces several datasets (e.g., raw current–voltage data and post-processed impedance fits).  
These can be grouped using ``hasPart`` or linked via ``isDerivedFrom``.

**Example: Linking raw and processed data**

.. code-block:: json

   {
     "@type": "schema:Dataset",
     "name": "EIS_FittedParameters.json",
     "encodingFormat": "application/json",
     "isDerivedFrom": {
       "@type": "schema:Dataset",
       "name": "EIS_Spectrum.csv",
       "encodingFormat": "text/csv"
     }
   }

7. Expressing Tabular Data Structure
------------------------------------

For structured tabular data, you can describe the schema using the **CSV on the Web (CSVW)** model.

**Example: CSVW schema embedded in JSON-LD**

.. code-block:: json

   {
     "@context": "http://www.w3.org/ns/csvw",
     "@type": "Table",
     "url": "Cycle_01.csv",
     "tableSchema": {
       "columns": [
         { "name": "Time / s", "datatype": "number", "propertyUrl": "emmo:Time" },
         { "name": "Voltage / V", "datatype": "number", "propertyUrl": "emmo:Voltage" },
         { "name": "Current / A", "datatype": "number", "propertyUrl": "emmo:Current" }
       ]
     }
   }

This approach enables fully machine-readable, column-level annotation.

8. Datasets as Input and Output
-------------------------------

Datasets aren’t only *results* — they can also serve as *inputs* for modeling or analysis processes.

**Example: Dataset as input**

.. code-block:: json

   {
     "@type": "ParameterEstimationProcess",
     "hasInput": {
       "@type": "schema:Dataset",
       "name": "HPPC_Data.csv"
     },
     "hasOutput": {
       "@type": "schema:Dataset",
       "name": "FittedParameters.json"
     }
   }

This provides a clear provenance trail: which data were used, how they were processed, and what results were produced.

9. Recommended Best Practices
-----------------------------

- Always specify a **unique identifier** (DOI, URI, or GitHub URL).  
- Include both **human-readable metadata** and **machine-readable variable definitions**.  
- Reference EMMO quantities in ``variableMeasured`` to link to physical meaning.  
- Use ``isDerivedFrom`` for processed datasets to maintain provenance.  
- Prefer standard MIME types (``text/csv``, ``application/json``, etc.).  
- Store units in column headers (e.g., ``Voltage / V``) or in associated metadata.

10. Example: Complete Dataset Description
-----------------------------------------

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "schema:Dataset",
     "@id": "https://doi.org/10.5281/zenodo.1234567",
     "name": "Galvanostatic Cycling Data for Zn-Air Cell",
     "description": "Charge-discharge cycling data recorded at 25°C with 1 M KOH electrolyte.",
     "encodingFormat": "text/csv",
     "variableMeasured": [
       { "@type": "schema:PropertyValue", "name": "Time / s", "propertyID": "emmo:Time" },
       { "@type": "schema:PropertyValue", "name": "Voltage / V", "propertyID": "emmo:Voltage" },
       { "@type": "schema:PropertyValue", "name": "Current / A", "propertyID": "emmo:Current" }
     ],
     "creator": { "@type": "schema:Person", "name": "Dr. Jane Smith" },
     "license": "https://spdx.org/licenses/CC-BY-4.0",
     "hasResult": {
       "@type": "ElectrochemicalTest",
       "hasTestObject": { "@type": "ZincAirCell" }
     },
     "distribution": {
       "@type": "schema:DataDownload",
       "contentUrl": "https://zenodo.org/records/1234567/files/ZnAir_Cycling.csv",
       "encodingFormat": "text/csv"
     }
   }


11. Summary
-----------

+----------------------------+---------------------------------------+--------------------------------------------+
| **Concept**                | **Role**                              | **Ontological Representation**             |
+============================+=======================================+============================================+
| Dataset                   | Collection of structured data         | ``schema:Dataset``                         |
+----------------------------+---------------------------------------+--------------------------------------------+
| DataDownload              | File access information               | ``schema:DataDownload``                    |
+----------------------------+---------------------------------------+--------------------------------------------+
| VariableMeasured           | Defines dataset columns               | ``schema:PropertyValue`` linked to EMMO    |
+----------------------------+---------------------------------------+--------------------------------------------+
| hasInput / hasResult       | Link between processes and datasets   | Provenance connections                     |
+----------------------------+---------------------------------------+--------------------------------------------+
| isDerivedFrom              | Connects processed to raw data        | Enables traceability                       |
+----------------------------+---------------------------------------+--------------------------------------------+
| CSVW Table                 | Tabular metadata                      | Machine-readable schema definition         |
+----------------------------+---------------------------------------+--------------------------------------------+


**Key takeaway**

A **Dataset** in EMMO is not just a file — it’s a *semantic description of what that file represents* and *how it connects* to physical, experimental, and computational reality.  
Properly described datasets allow machines (and people) to *find, interpret, and reuse* your data with confidence.
