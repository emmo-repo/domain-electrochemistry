Nominal Voltage
------------------
The **nominal voltage** is the standard operating voltage of an electrochemical cell under typical conditions.

**Example:** Representing a nominal voltage of 3.7V:

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "NominalVoltage",
     "hasNumericalPart": {
       "@type": "RealData",
       "hasNumberValue": 3.7
     },
     "hasMeasurementUnit": "emmo:Volt"
   }

