Discharge Test
==============

A **Discharge Test** measures the energy and capacity released when an electrochemical cell
is discharged under controlled conditions. It forms a subset of the galvanostatic
charge–discharge family of tests.

Ontology Alignment
------------------
- Class: ``DischargeTest``
- Subclass of: ``ElectrochemicalTest``
- Associated process: ``DischargingProcess``

Example
-------
.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "DischargeTest",
     "hasTestObject": { "@type": "BatteryCell" },
     "hasProcedure": {
       "@type": "DischargingProcess",
       "hasProperty": {
         "@type": "AppliedCurrent",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 0.5 },
         "hasMeasurementUnit": "emmo:Ampere"
       }
     },
     "hasResult": {
       "@type": "DischargeCapacity",
       "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 4.8 },
       "hasMeasurementUnit": "emmo:AmpereHour"
     }
   }
