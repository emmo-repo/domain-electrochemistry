Discharging
-----------

`IRI: https://w3id.org/emmo/domain/electrochemistry#electrochemistry_06d8e1ee_924a_4915_998d_33a69f41dadc <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_06d8e1ee_924a_4915_998d_33a69f41dadc>`_

Description 
~~~~~~~~~~~

Here are some commonly used discharging processes in electrochemical systems:

.. list-table:: Types of Discharging Processes
   :header-rows: 1

   * - Name
     - Label
     - IRI
   * - Constant Current Discharging
     - ``ConstantCurrentDischarging``
     - `IRI: https://w3id.org/emmo/domain/electrochemistry#electrochemistry_53fe3f58_0802_41cf_af69_4784fc42cc30 <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_53fe3f58_0802_41cf_af69_4784fc42cc30>`_
   * - Constant Voltage Discharging
     - ``ConstantVoltageDischarging``
     - `IRI: https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9865e4f9_756d_4d94_a6fd_4102ab795f9e <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9865e4f9_756d_4d94_a6fd_4102ab795f9e>`_
   * - Constant Power Discharging
     - ``ConstantPowerDischarging``
     - `IRI: TBD <TBD>`_


Guidelines for Use 
~~~~~~~~~~~~~~~~~~

To represent a **Discharging** process in the ontology, follow three key steps:

Step 1. Identify the Process
""""""""""""""""""""""""""""

.. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "ConstantCurrentDischarging"
      } 


Step 2. Assign Properties 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ConstantCurrentDischarging",
     "hasProperty": [
       {
         "@type": "DischargingCurrent",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumberValue": 22.5
         },
         "hasMeasurementUnit": "emmo:Ampere"
       },
       {
         "@type": "UpperVoltageLimit",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumberValue": 4.2
         },
         "hasMeasurementUnit": "emmo:Volt"
       },
       {
         "@type": "LowerVoltageLimit",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumberValue": 3
         },
         "hasMeasurementUnit": "emmo:Volt"
       }
     ]
   }


Step 3. Link the Process to a Device 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ConstantCurrentDischarging",
     "hasProperty": [
       {
         "@type": "DischargingCurrent",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumberValue": 22.5
         },
         "hasMeasurementUnit": "emmo:Ampere"
       },
       {
         "@type": "UpperVoltageLimit",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumberValue": 4.2
         },
         "hasMeasurementUnit": "emmo:Volt"
       },
       {
         "@type": "LowerVoltageLimit",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumberValue": 3
         },
         "hasMeasurementUnit": "emmo:Volt"
       }
     ],
     "hasParticipant": [
       {
         "@type": "ElectrochemicalDevice"
       }
     ]
   }



Step 4. Link the Process to Equipment 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ConstantCurrentDischarging",
     "hasProperty": [
       {
         "@type": "DischargingCurrent",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumberValue": 22.5
         },
         "hasMeasurementUnit": "emmo:Ampere"
       },
       {
         "@type": "UpperVoltageLimit",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumberValue": 4.2
         },
         "hasMeasurementUnit": "emmo:Volt"
       },
       {
         "@type": "LowerVoltageLimit",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumberValue": 3
         },
         "hasMeasurementUnit": "emmo:Volt"
       }
     ],
     "hasParticipant": {
         "@type": "ElectrochemicalDevice"
       },
     "hasTemporaryParticipant": {
         "@type": "Potentiostat"
       }
   }


Step 4. Link the Process to Other Processes (if needed)  
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ConstantCurrentDischarging",
     "hasProperty": [
       {
         "@type": "DischargingCurrent",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumberValue": 22.5
         },
         "hasMeasurementUnit": "emmo:Ampere"
       },
       {
         "@type": "UpperVoltageLimit",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumberValue": 4.2
         },
         "hasMeasurementUnit": "emmo:Volt"
       },
       {
         "@type": "LowerVoltageLimit",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumberValue": 3
         },
         "hasMeasurementUnit": "emmo:Volt"
       }
     ],
     "hasParticipant": {
         "@type": "ElectrochemicalDevice"
       },
     "hasTemporaryParticipant": {
         "@type": "Potentiostat"
       },
     "hasSubProcess": {
         "@type": "VoltageMeasurement"
         "hasOutput": {
            "@type": "VoltageData"
       }
   }
