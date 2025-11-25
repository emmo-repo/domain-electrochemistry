Electrochemical Testing
=======================

Description
-----------

Electrochemical testing links theory and practice — it is how we **measure**, **characterize**, and **validate** the behavior of materials, cells, and devices. In the ontology, testing is represented as a type of **Process** in which **measurements** are made on an **electrochemical system** under defined **conditions**.

Testing processes can include simple measurements like open-circuit voltage or complex workflows like galvanostatic cycling, impedance spectroscopy, or GITT (galvanostatic intermittent titration technique).

.. figure:: ../../assets/img/fig/png/electrochemical_testing_workflow.png
   :align: center
   :alt: Schematic of electrochemical testing process
   :width: 80%

   Electrochemical testing as a structured process with inputs, conditions, and results.

Core concepts
-------------

An **ElectrochemicalTest** in the ontology has three main components:

1. **The Test Object** — what is being tested (e.g., an `Electrode`, `ElectrochemicalCell`, or `ElectrochemicalDevice`)  
2. **The Procedure** — the controlled process or sequence of actions applied  
3. **The Result** — the observed or recorded data

These are connected using the relations:

- `hasTestObject` — the physical or virtual object being tested  
- `hasProcedure` — the test protocol, recipe, or workflow  
- `hasResult` — the data or property outcomes of the test  

Guidelines for Use
------------------

1. Identify the Test Process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use `ElectrochemicalTest` or a more specific subclass to represent the testing activity.

Common subclasses include:

- `BatteryTest` — for full cells or devices  
- `HalfCellTest` — for electrodes vs. reference  
- `ElectrochemicalImpedanceSpectroscopy`  
- `GalvanostaticChargeDischargeTest`  
- `GITTTest`, `HPPC`, `CVTest`, etc.

**Example: define a generic electrochemical test**

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ElectrochemicalTest"
   }


2. Define the Test Object
^^^^^^^^^^^^^^^^^^^^^^^^^

The `hasTestObject` relation links the test to what is being measured.  
This can be any physical or modeled system, such as a material, electrode, or full cell.

**Example: testing a battery cell**

.. code-block:: json

   {
     "@type": "BatteryTest",
     "hasTestObject": { "@type": "BatteryCell" }
   }

**Example: testing a material**

.. code-block:: json

   {
     "@type": "HalfCellTest",
     "hasTestObject": {
       "@type": "NegativeElectrode",
       "hasActiveMaterial": { "@type": "Graphite" }
     }
   }


3. Define the Procedure or Protocol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each test follows a defined **procedure** — a set of steps, conditions, and controls that govern how the test is executed.  
This can be represented using a `Workflow` or `Procedure` object linked via `hasProcedure`.

Procedures often include sub-processes such as `ChargingProcess`, `DischargingProcess`, or `RestProcess`.

**Example: a simple charge–discharge workflow**

.. code-block:: json

   {
     "@type": "BatteryTest",
     "hasProcedure": {
       "@type": "Workflow",
       "hasTask": [
         { "@type": "ChargingProcess" },
         { "@type": "DischargingProcess" }
       ]
     }
   }

For more complex test programs (e.g., HPPC, GITT), this can be expanded to describe each step explicitly or reference an external procedure document.


4. Define Test Conditions
^^^^^^^^^^^^^^^^^^^^^^^^^

Each test is carried out under specific environmental and operational conditions, modeled as **properties of the test process** or **contextual entities**.

Common examples include:

- `AmbientTemperature`
- `AppliedCurrent`
- `CycleNumber`
- `CutoffVoltage`
- `CRate`

**Example: defining test conditions**

.. code-block:: json

   {
     "@type": "BatteryTest",
     "hasProperty": [
       {
         "@type": "AmbientTemperature",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 25 },
         "hasMeasurementUnit": "emmo:DegreeCelsius"
       },
       {
         "@type": "AppliedCurrent",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 0.5 },
         "hasMeasurementUnit": "emmo:Ampere"
       }
     ]
   }


5. Record the Test Result
^^^^^^^^^^^^^^^^^^^^^^^^^

The `hasResult` relation links the test to the data produced.  
Results can be represented at different levels of abstraction:

- As **properties** (e.g., capacity, voltage, resistance)  
- As **datasets** (linked to files or data resources)  
- As **statistical summaries** or **time series**

**Example: test with result properties**

.. code-block:: json

   {
     "@type": "BatteryTest",
     "hasTestObject": { "@type": "BatteryCell" },
     "hasResult": [
       {
         "@type": "DischargeCapacity",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 4.8 },
         "hasMeasurementUnit": "emmo:AmpereHour"
       },
       {
         "@type": "CoulombicEfficiency",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 0.995 },
         "hasMeasurementUnit": "emmo:UnitOne"
       }
     ]
   }

**Example: test result as dataset**

.. code-block:: json

   {
     "@type": "BatteryTest",
     "hasResult": {
       "@type": "Dataset",
       "name": "Cycle_001.csv",
       "encodingFormat": "text/csv",
       "contentUrl": "https://example.org/data/BatteryTest_Cycle_001.csv"
     }
   }


Connecting Tests to Data and Models
-----------------------------------

Each test can be linked to datasets or analysis models to form a **complete digital record**.

Relations include:

- `hasDataset` — connects to the raw or processed measurement data  
- `hasAnalysis` — connects to computational post-processing or modeling results  
- `hasDerivedProperty` — connects to extracted features (e.g., diffusion coefficient, pseudo-OCV)

**Example: linking test to derived analysis**

.. code-block:: json

   {
     "@type": "BatteryTest",
     "hasResult": {
       "@type": "Dataset",
       "name": "GITT_Data.csv"
     },
     "hasAnalysis": {
       "@type": "DiffusionCoefficientEstimation",
       "hasDerivedProperty": {
         "@type": "DiffusionCoefficient",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 3e-12 },
         "hasMeasurementUnit": "emmo:SquareMetrePerSecond"
       }
     }
   }


Best Practices
--------------

- Always specify what is being tested (`hasTestObject`) and what was measured (`hasResult`).  
- Distinguish **test conditions** (inputs) from **results** (outputs).  
- For recurring procedures, reference or define a reusable **workflow** rather than embedding all steps inline.  
- When including datasets, use `contentUrl` or DOIs for findability and FAIR compliance.  
- Link derived data or model analyses to the originating test via `hasAnalysis` or `isDerivedFrom`.  
- Use standard physical units defined in EMMO and SI for all quantities.  
- Mark vendor- or convention-based data as `ConventionalProperty`; measured data as `MeasuredProperty`.  


Summary
-------

An **ElectrochemicalTest** captures the **experimental process** through which electrochemical data are generated.  
It connects the **object under test**, the **procedure**, and the **results** into a coherent, machine-readable structure.

| Concept | Relation | Example |
|----------|-----------|----------|
| **ElectrochemicalTest** | `hasTestObject`, `hasResult` | battery test |
| **Procedure / Workflow** | `hasTask`, `hasSubProcess` | charge/discharge sequence |
| **Test Conditions** | `hasProperty` | ambient temperature, current |
| **Test Result** | `hasResult`, `hasDataset` | discharge capacity, CSV file |
| **Derived Analysis** | `hasAnalysis`, `hasDerivedProperty` | diffusion coefficient from GITT |

By following these conventions, electrochemical tests become **interoperable**, **traceable**, and **semantically rich**, enabling automated workflows, reproducibility, and data-driven insights across the electrochemical domain.


.. toctree::
   :maxdepth: 2

   discharging_test
   electrochemical_impedance_spectroscopy_test
   cyclic_voltammetry_test
   galvanostatic_cycling_test
