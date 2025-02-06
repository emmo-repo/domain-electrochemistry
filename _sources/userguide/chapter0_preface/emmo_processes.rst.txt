Processes in EMMO
=================

In the EMMO ontology, **processes** represent activities or changes that happen over time. Unlike static objects, processes describe events where things transform, interact, or evolve. The ontology provides a structured way to define processes, workflows, and tasks to ensure clarity and consistency across different applications.

Overview of Processes
---------------------
A **Process** in EMMO is defined as "a structured event where at least two different states or actions occur over time." This means a process always involves a transformation, such as mixing chemicals, heating a material, or charging a battery.

Key Features of Processes in EMMO
- **Time-based Evolution**: A process must include at least two distinct stages.
- **Causal Connections**: Processes show cause-and-effect relationships.
- **Step-by-step Structure**: Processes are often broken into **workflows** and **tasks** to describe different levels of detail.

Representing Processes in EMMO
------------------------------
To represent a **Process** in EMMO, follow these steps:

1. **Identify the Process**  
   Define the type of process being represented.

   .. code-block:: json

      {
        "@context": "https://w3id.org/emmo/context",
        "@type": "Process"
      }

2. **Specify Participants**  
   Link the process to objects or entities that take part in it using `hasParticipant`.

   .. code-block:: json

      {
        "@context": "https://w3id.org/emmo/context",
        "@type": "Process",
        "hasParticipant": {
          "@type": "Participant"
        }
      }

3. **Define Process Order**  
   Use `precedes` to indicate the order of events in a sequence.

   .. code-block:: json

      {
        "@context": "https://w3id.org/emmo/context",
        "@type": "Process",
        "precedes": {
          "@type": "NextProcess"
        }
      }

4. **Include the Process in a Workflow**  
   If the process is part of a structured workflow, connect it using `hasTask`.

   .. code-block:: json

      {
        "@context": "https://w3id.org/emmo/context",
        "@type": "Workflow",
        "hasTask": {
          "@type": "Process"
        }
      }

Workflows and Tasks
-------------------
A **workflow** is a set of processes arranged in a specific order to achieve a result. Workflows are made up of **tasks**, which describe smaller steps in a process.

Types of Workflows
~~~~~~~~~~~~~~~~~~~~

Serial Workflow
^^^^^^^^^^^^^^
A **Serial Workflow** consists of tasks that must be completed one after another.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/context",
     "@type": "SerialWorkflow",
     "hasTask": [
       { "@type": "Task", "name": "Step 1" },
       { "@type": "Task", "name": "Step 2" }
     ]
   }

Parallel Workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A **Parallel Workflow** allows multiple tasks to run at the same time.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/context",
     "@type": "ParallelWorkflow",
     "hasTask": [
       { "@type": "Task", "name": "Task A" },
       { "@type": "Task", "name": "Task B" }
     ]
   }

Iterative Workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
An **Iterative Workflow** repeats the same task multiple times.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/context",
     "@type": "IterativeWorkflow",
     "hasTask": {
       "@type": "Task",
       "name": "Repeated Task"
     }
   }

SubProcesses
------------
A **SubProcess** is a process that occurs within another process as a **spatial part** of it. For example, **Breathing** is a subprocess of **Living**. This concept is useful for breaking down complex processes into more detailed parts while maintaining their connection to the larger event.

Representing a SubProcess
~~~~~~~~~~~~~~~~~~~~~~~~~
To define a **SubProcess** in EMMO, use the `hasSubProcess` property to link a process to its subprocess.

**Example:** Defining Breathing as a SubProcess of Living

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/context",
     "@type": "LivingProcess",
     "hasSubProcess": {
       "@type": "Breathing"
     }
   }

Object Properties for Processes
-------------------------------
Processes in EMMO use specific relationships to describe their structure:

- **hasParticipant**: Links a process to an entity that takes part in it.
- **hasInput**: Defines an entity as the input to a process.
- **hasOutput**: Defines an entity as the result of a process.
- **precedes**: Shows the sequence of events in time.
- **hasTask**: Connects a workflow to its tasks.
- **hasSubProcess**: Links a process to a subprocess occurring within it.

**Example:** Defining a process with input, output, and sequence.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/context",
     "@type": "Process",
     "hasInput": { "@type": "RawMaterial" },
     "hasOutput": { "@type": "FinalProduct" },
     "precedes": { "@type": "NextProcess" }
   }

By following these structured guidelines, users can define processes in a clear and logical way, making them easier to use across different applications.
