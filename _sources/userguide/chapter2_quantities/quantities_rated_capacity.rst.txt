Rated Capacity
------------------
The **rated capacity** is the total charge a battery is designed to store and deliver under specified conditions.

**Example:** Representing a rated capacity of 2000 mAh:

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "RatedCapacity",
     "hasNumericalPart": {
       "@type": "RealData",
       "hasNumberValue": 2000
     },
     "hasMeasurementUnit": "emmo:MilliAmpereHour"
   }
