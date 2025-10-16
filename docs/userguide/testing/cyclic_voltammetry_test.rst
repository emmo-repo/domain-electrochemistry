Cyclic Voltammetry (CV) Test
============================

A **Cyclic Voltammetry Test** measures current response while sweeping potential at a
controlled rate. It is used to study **redox reactions**, **electrochemical stability windows**, and **kinetics**.

Ontology Alignment
------------------
- Class: ``CyclicVoltammetryTest``
- Subclass of: ``ElectrochemicalTest``
- Related processes: ``PotentialSweepProcess``

Example
-------
.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "CyclicVoltammetryTest",
     "hasTestObject": { "@type": "ThreeElectrodeCell" },
     "hasProcedure": {
       "@type": "PotentialSweepProcess",
       "hasProperty": {
         "@type": "ScanRate",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 10 },
         "hasMeasurementUnit": "emmo:MilliVoltPerSecond"
       }
     },
     "hasResult": {
       "@type": "Dataset",
       "name": "CV_Scan.csv",
       "encodingFormat": "text/csv"
     }
   }
