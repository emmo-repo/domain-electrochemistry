Specific Energy
------------------
The **specific energy** represents the energy stored per unit mass of the device.

**Example:** Representing a specific energy of 180 Wh/kg:

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "SpecificEnergy",
     "hasNumericalPart": {
       "@type": "RealData",
       "hasNumberValue": 180
     },
     "hasMeasurementUnit": "emmo:WattHourPerKilogram"
   }
