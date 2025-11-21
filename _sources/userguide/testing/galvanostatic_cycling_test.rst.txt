Galvanostatic Charge–Discharge Test
===================================

A **Galvanostatic Charge–Discharge Test** is a fundamental electrochemical test in which a constant
current is applied to charge and discharge a cell.  
It provides direct measures of **capacity**, **efficiency**, and **degradation** over cycles.

Ontology Alignment
------------------
- Class: ``GalvanostaticChargeDischargeTest``
- Subclass of: ``ElectrochemicalTest``
- Related processes: ``ChargingProcess``, ``DischargingProcess``, ``RestProcess``

Guidelines for Use
------------------
To represent this test:

1. Use ``GalvanostaticChargeDischargeTest`` as the main class.  
2. Define the ``hasProcedure`` workflow as a sequence of charge, rest, and discharge tasks.  
3. Add test conditions (``C_Rate``, ``CutoffVoltage``, ``AmbientTemperature``).  
4. Define results such as ``DischargeCapacity`` or ``CoulombicEfficiency``.

Example
-------
.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "GalvanostaticChargeDischargeTest",
     "hasTestObject": { "@type": "BatteryCell" },
     "hasProcedure": {
       "@type": "Workflow",
       "hasTask": [
         { "@type": "ChargingProcess" },
         { "@type": "RestProcess" },
         { "@type": "DischargingProcess" }
       ]
     },
     "hasProperty": [
       {
         "@type": "C_Rate",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 1.0 },
         "hasMeasurementUnit": "emmo:UnitOne"
       },
       {
         "@type": "AmbientTemperature",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 25 },
         "hasMeasurementUnit": "emmo:DegreeCelsius"
       }
     ],
     "hasResult": [
       {
         "@type": "DischargeCapacity",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 4.8 },
         "hasMeasurementUnit": "emmo:AmpereHour"
       }
     ]
   }

Related Patterns
----------------
- :doc:`discharge_test`
- :doc:`cycling_test`
