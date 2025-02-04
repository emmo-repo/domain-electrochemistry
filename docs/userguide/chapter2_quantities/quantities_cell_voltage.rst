Cell Voltage
------------------
The **cell voltage** is the potential difference between the anode and cathode at a given state of operation.

**Example:** Representing a cell voltage of 3.2 V:

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "CellVoltage",
     "hasNumericalPart": {
       "@type": "RealData",
       "hasNumberValue": 3.2
     },
     "hasMeasurementUnit": "emmo:Volt"
   }
