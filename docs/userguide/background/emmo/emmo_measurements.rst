Measurements in EMMO
====================

In science and engineering, measurement connects the physical world to data. When we measure something — like the **mass** of a sample or the **voltage** of a cell — we perform a process that produces a numerical value. In EMMO, this connection is modeled explicitly through three linked entities:

1. **The measurement process** — the *act* of measuring something.  
2. **The measurement result** — the *data* produced by the process.  
3. **The property of the object** — the *characteristic* that was measured.

This distinction makes it possible to describe not just *what was measured*, but also *how* it was measured and *under what conditions* — essential for traceability, reproducibility, and FAIR data.

Overview of Measurement Concepts
--------------------------------

| Concept | Description | Example |
|----------|--------------|----------|
| **MeasurementProcess** | The activity or experiment that produces a value. | Weighing a sample. |
| **MeasurementResult** | The recorded output of that process. | 1.403 kg ± 0.002 kg. |
| **Property** | The feature of the object that was measured. | The sample’s mass. |

Together, these form a causal chain:

::
   MeasurementProcess → produces → MeasurementResult → quantifies → Property → belongsTo → Object

Example: Measuring the mass of a sample
---------------------------------------

Let’s walk through how to model a simple measurement: “You place a sample on a balance and record its mass as 1.403 kg.”

Step 1 — Define the object being measured
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The object of interest is an individual of type ``PhysicalObject`` (or a more specific subclass like ``MaterialSample``).

.. code-block:: json

   {
     "@id": "ex:Sample_A",
     "@type": "PhysicalObject"
   }

Step 2 — Represent the measurement process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **act of weighing** is a process — it happens in time, involves participants, and produces an outcome. We can model it as an instance of ``MeasurementProcess``.

.. code-block:: json

   {
     "@id": "ex:Weighing_1",
     "@type": "MeasurementProcess",
     "hasParticipant": { "@id": "ex:Sample_A" },
     "hasInput": { "@id": "ex:Sample_A" },
     "hasOutput": { "@id": "ex:MassResult_1" },
     "emmo:hasMeasurementDevice": { "@type": "Balance" }
   }

Here:
- The process has the **sample** as its participant and input.  
- The **output** is a ``MeasurementResult``.  
- The process also specifies a **device** (balance).

Step 3 — Represent the measurement result
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A measurement produces data — a recorded observation with a numeric value and unit. In EMMO, this is expressed using a ``MeasurementResult`` that *quantifies* a ``Property`` of the measured object.

.. code-block:: json

   {
     "@id": "ex:MassResult_1",
     "@type": "MeasurementResult",
     "quantifies": {
       "@id": "ex:MassProperty_1",
       "@type": "Mass",
       "emmo:hasMeasuredObject": { "@id": "ex:Sample_A" }
     },
     "hasNumericalPart": {
       "@type": "emmo:RealData",
       "hasNumberValue": 1.403
     },
     "hasMeasurementUnit": "emmo:Kilogram",
     "emmo:hasMeasurementUncertainty": {
       "@type": "emmo:RealData",
       "hasNumberValue": 0.002
     }
   }

This representation keeps the result separate from the property it quantifies, preserving the distinction between *observation* and *truth about the world*.

Step 4 — Assign the measured property to the object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finally, the property (e.g., mass) can be **associated with the object** through ``hasProperty``. You can express this directly or link it back to the measurement that produced it.

.. code-block:: json

   {
     "@id": "ex:Sample_A",
     "@type": "PhysicalObject",
     "hasProperty": {
       "@id": "ex:MassProperty_1",
       "@type": ["Mass", "MeasuredProperty"],
       "hasNumericalPart": {
         "@type": "emmo:RealData",
         "hasNumberValue": 1.403
       },
       "hasMeasurementUnit": "emmo:Kilogram",
       "emmo:isResultOf": { "@id": "ex:Weighing_1" }
     }
   }

This pattern captures the full chain from process to result to property. It also allows the same object to have multiple mass properties — for example, if measured under different conditions or by different methods.

Alternative Representations
---------------------------

Depending on your modeling needs, you can link measurements and results in two main ways:

1. **Through the result** (explicit):  
   The ``MeasurementResult`` quantifies the ``Property``.  
   Best when you want to preserve provenance and traceability.

2. **Direct property assignment** (simplified):  
   Attach the measured property directly to the object with
   ``MeasuredProperty`` typing.  
   Best for compact data serialization when provenance is implicit.

Compact example:

.. code-block:: json

   {
     "@type": "PhysicalObject",
     "hasProperty": {
       "@type": ["Mass", "MeasuredProperty"],
       "hasNumericalPart": {
         "@type": "emmo:RealData",
         "hasNumberValue": 1.403
       },
       "hasMeasurementUnit": "emmo:Kilogram"
     }
   }

Measurement Participants
------------------------

In addition to the object being measured, measurements typically involve:

- **Devices** (e.g., balance, voltmeter, spectrometer) → ``hasMeasurementDevice``  
- **Operators or software** → ``hasAgent``  
- **Conditions** (e.g., temperature, humidity) → ``hasCondition`` or   ``hasCharacterisationEnvironmentProperty``  

Example:

.. code-block:: json

   {
     "@type": "MeasurementProcess",
     "hasParticipant": [
       { "@type": "MaterialSample" },
       { "@type": "Operator" }
     ],
     "emmo:hasMeasurementDevice": { "@type": "Balance" },
     "emmo:hasMeasurementCondition": {
       "@type": "CharacterisationEnvironmentProperty",
       "schema:name": "AmbientTemperature",
       "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 22 },
       "hasMeasurementUnit": "emmo:DegreeCelsius"
     }
   }

Linking to Workflows
--------------------

Measurements are often steps within broader **experimental or testing workflows**. In that case, simply include the measurement process within a ``Workflow`` using ``hasTask`` or ``hasSubProcess``:

.. code-block:: json

   {
     "@type": "BatteryTestWorkflow",
     "hasTask": [
       { "@type": "MeasurementProcess", "@id": "ex:MassMeasurement_1" },
       { "@type": "MeasurementProcess", "@id": "ex:OCVMeasurement_1" }
     ]
   }

Best Practices
--------------

- Treat **measurement** as a process, not as a property value.  
- Always distinguish between the **property** being measured and the **result**.  
- Use ``hasInput`` and ``hasOutput`` to trace data lineage.  
- Use ``hasParticipant`` for all entities involved (sample, device, operator).  
- If possible, record **uncertainty**, **instrument**, and **conditions**.  
- Use ``MeasuredProperty`` typing when assigning results directly to an object.  
- When integrating multiple measurements, link each result explicitly to its process for provenance.

Summary
-------

| Concept | Description | Typical Relation |
|----------|--------------|------------------|
| **MeasurementProcess** | The act of observing or quantifying a property. | ``hasInput``, ``hasOutput``, ``hasParticipant`` |
| **MeasurementResult** | The recorded data produced by the process. | ``quantifies`` a ``Property`` |
| **Property / Quantity** | The feature of the object that was measured. | Linked to the object via ``hasProperty`` |
| **PhysicalObject** | The entity being measured. | ``hasProperty`` or ``isParticipantIn`` |

In EMMO, these entities connect to form a complete, logically consistent chain linking the *physical world*, the *measurement event*, and the *data it produces*.