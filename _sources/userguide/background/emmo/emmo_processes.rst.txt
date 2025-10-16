Processes in EMMO
=================

In the EMMO ontology, **processes** represent *happenings in time* — the activities, transformations, and interactions that change the state of things. Unlike static objects, which persist through time, processes describe events in which entities participate and evolve.  

EMMO provides a structured way to describe these processes — from physical phenomena (like diffusion) to laboratory procedures (like mixing or charging a cell) — ensuring that temporal relationships, participants, and causal links are captured consistently.

Overview of Processes
---------------------

A **Process** in EMMO is defined as:

> *A structured event in which at least two distinct states or actions occur over time.*

This means a process always involves **change** — whether of material state, configuration, or property value.

Examples:

- **ChargingProcess** — electrons and ions move, changing the chemical state of electrodes.  
- **MixingProcess** — substances combine to form a homogeneous phase.  
- **MeasurementProcess** — an instrument records the value of a property.  

Key features of processes in EMMO:

- **Time-based evolution** – processes have a temporal extent and involve a sequence of states or events.  
- **Causal structure** – they describe transformations and interactions with explicit cause–effect relationships.  
- **Holistic composition** – complex processes can be broken into subprocesses or arranged into workflows, forming a hierarchy of events.

Representing Processes
----------------------

When representing a process in EMMO, it helps to think in terms of **who** or **what** participates, **what goes in**, **what comes out**, and **how it is connected** to other processes.

1. **Identify the process type**

   Begin by defining the specific process class.

   .. code-block:: json

      {
        "@context": "https://w3id.org/emmo/context",
        "@type": "Process"
      }

2. **Specify participants**

   Link the process to objects or entities that take part in it using ``hasParticipant``.

   .. code-block:: json

      {
        "@type": "MixingProcess",
        "hasParticipant": [
          { "@type": "LiquidSolvent" },
          { "@type": "Solute" }
        ]
      }

3. **Define inputs and outputs**

   Every process can have entities that enter or leave its boundaries.

   - ``hasInput`` connects entities that exist before the process.
   - ``hasOutput`` connects entities that exist after the process.

   .. code-block:: json

      {
        "@type": "ChargingProcess",
        "hasInput": { "@type": "DischargedBatteryCell" },
        "hasOutput": { "@type": "ChargedBatteryCell" }
      }

4. **Establish order in time**

   Use ``precedes`` or ``follows`` to specify temporal sequence.

   .. code-block:: json

      {
        "@type": "MixingProcess",
        "precedes": { "@type": "HeatingProcess" }
      }

5. **Include the process in a workflow**

   If a process is part of a broader procedure, connect it with ``hasTask`` or ``hasSubProcess`` (depending on whether it is a workflow or a nested subprocess; see below).

   .. code-block:: json

      {
        "@type": "Workflow",
        "hasTask": { "@type": "ElectrochemicalTestProcess" }
      }

Mereology of Processes
----------------------

Just as physical objects can be broken down into parts, **processes can be broken down into subprocesses**. This is called *temporal mereology* — describing wholes and parts in time.

- ``hasSubProcess`` expresses that one process occurs **within** another as a constituent event.
- ``isSubProcessOf`` is its inverse.

This structure allows reasoning such as:

::
   If A hasSubProcess B and B hasSubProcess C, then A hasSubProcess C.

Example — defining subprocesses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "@type": "BatteryTestProcess",
     "hasSubProcess": [
       { "@type": "ChargingProcess" },
       { "@type": "DischargingProcess" }
     ]
   }

Here, *ChargingProcess* and *DischargingProcess* are subprocesses of a broader *BatteryTestProcess*.  
Reasoning will infer that all inputs and outputs of the subprocesses contribute to the overall test.

Workflows and Tasks
-------------------

A **workflow** is a special kind of process that represents an *organized sequence* of tasks performed to achieve a goal. Workflows define *how* processes are executed rather than *what* physical change they describe.

Workflows are typically composed of **tasks** using the ``hasTask`` relation. Each task is itself a process — either simple or complex.

Types of workflows
~~~~~~~~~~~~~~~~~~

**Serial Workflow**

Tasks are performed in a specific order.

.. code-block:: json

   {
     "@type": "SerialWorkflow",
     "hasTask": [
       { "@type": "PrepareElectrodeProcess" },
       { "@type": "AssembleCellProcess" },
       { "@type": "ChargeDischargeTestProcess" }
     ]
   }

**Parallel Workflow**

Multiple tasks occur simultaneously.

.. code-block:: json

   {
     "@type": "ParallelWorkflow",
     "hasTask": [
       { "@type": "ElectrolytePreparationProcess" },
       { "@type": "CathodePreparationProcess" }
     ]
   }

**Iterative Workflow**

A task is repeated until a condition is satisfied.

.. code-block:: json

   {
     "@type": "IterativeWorkflow",
     "hasTask": { "@type": "CycleTestProcess" }
   }

Workflows vs. SubProcesses
--------------------------

It’s useful to distinguish between *subprocesses* and *tasks*:

| Concept | Relation | Description |
|----------|-----------|-------------|
| **SubProcess** | ``hasSubProcess`` | A process that happens *within* another process as part of its temporal or physical unfolding. Example: a **Heating** subprocess inside a **SinteringProcess**. |
| **Task** | ``hasTask`` | A discrete unit of work within a workflow, representing *a step to be performed*. Example: “Mix precursor” as a task in a **SynthesisWorkflow**. |

In short:  
- ``hasSubProcess`` models *temporal nesting*.  
- ``hasTask`` models *procedural organization*.

Object Properties for Processes
-------------------------------

EMMO defines several key relations for describing processes and their interconnections:

+-------------------+----------------------------------------------------------+
| **Property**      | **Description**                                          |
+===================+==========================================================+
| ``hasParticipant``| Links a process to entities that take part in it.        |
+-------------------+----------------------------------------------------------+
| ``hasInput``      | Links a process to entities that are consumed or modified|
|                   | at the start.                                            |
+-------------------+----------------------------------------------------------+
| ``hasOutput``     | Links a process to entities that are produced or changed |
|                   | as a result.                                             |
+-------------------+----------------------------------------------------------+
| ``precedes`` / ``follows`` | Expresses temporal ordering between processes.  |
+-------------------+----------------------------------------------------------+
| ``hasSubProcess`` | Relates a process to subprocesses that occur within it.  |
+-------------------+----------------------------------------------------------+
| ``hasTask``       | Relates a workflow to its tasks (process steps).         |
+-------------------+----------------------------------------------------------+

Example — a complete process description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "@type": "BatteryFormationProcess",
     "hasInput": { "@type": "AssembledBatteryCell" },
     "hasOutput": { "@type": "FormedBatteryCell" },
     "hasSubProcess": [
       { "@type": "ChargingProcess" },
       { "@type": "RestProcess" },
       { "@type": "DischargingProcess" }
     ]
   }

This expresses that the *BatteryFormationProcess* consists of multiple subprocesses and transforms an *AssembledBatteryCell* into a *FormedBatteryCell*.

Best Practices
--------------

- Use ``hasSubProcess`` to model *physical or temporal composition* of processes.  
- Use ``hasTask`` to model *workflow or procedural composition*.  
- Always define ``hasInput`` and ``hasOutput`` when modeling transformations.  
- Use ``hasParticipant`` for any other entities involved (tools, environments, catalysts).  
- Use ``precedes`` and ``follows`` to represent experimental or computational sequence.  
- Combine processes hierarchically to represent real-world operations — from fundamental phenomena to full experimental workflows.

Summary
-------

Processes in EMMO describe *how things happen*. They capture time, causality, and transformation with the same logical rigor that ``hasPart`` brings to spatial composition.

- ``Process`` — a temporally extended event involving change.  
- ``hasInput`` / ``hasOutput`` — define transformations.  
- ``hasParticipant`` — link to involved entities.  
- ``hasSubProcess`` — express nested temporal composition.  
- ``hasTask`` — organize processes in workflows.  

By modeling processes this way, users can connect physical phenomena, laboratory steps, and computational workflows under a single, interoperable framework — linking *what happens*, *to whom*, and *in what order*.
