Energy Density
------------------
The **energy density** refers to the amount of energy stored per unit volume of an electrochemical device.

**Example:** Representing an energy density of 250 Wh/L:

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "EnergyDensity",
     "hasNumericalPart": {
       "@type": "RealData",
       "hasNumberValue": 250
     },
     "hasMeasurementUnit": "emmo:WattHourPerLitre"
   }

