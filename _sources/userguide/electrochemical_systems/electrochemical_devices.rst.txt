Electrochemical Devices
=======================

An **electrochemical device** is an engineered system designed to **perform a function** based on one or more electrochemical cells. While an **ElectrochemicalCell** represents the *active domain* of reactions — where ions and electrons move — an **ElectrochemicalDevice** represents the *assembled, functional product* that can store, deliver, or convert energy.

.. admonition:: Electrochemical Device vs. Electrochemical Cell

   **ElectrochemicalCell**  
   The *reactive unit* where oxidation and reduction occur. Includes electrodes, electrolyte, separator, and other internal components.

   **ElectrochemicalDevice**  
   The *functional system* that contains one or more cells, along with housing, terminals, connectors, safety elements, and packaging. It represents something you can *use* or *handle* in practice — such as a button cell, pouch cell, or battery pack.

   In short:  
   - A **cell** describes *how electrochemistry happens*.  
   - A **device** describes *how that cell is packaged, connected, and used*.

Common subclasses include:

- **BatteryCell** — a self-contained rechargeable or primary energy storage unit  
- **BatteryPack** — multiple cells connected in series or parallel  
- **Supercapacitor**, **FuelCell**, **Electrolyzer**, **FlowBattery**, etc. — systems built for specific applications

.. figure:: ../../assets/img/fig/png/electrochemical_device_structure.png
   :align: center
   :alt: Structure of an electrochemical device
   :width: 80%

   An electrochemical device contains one or more cells plus mechanical and electrical subsystems.

Guidelines for Use
------------------

Follow these steps to describe an **ElectrochemicalDevice** in the ontology.

1. Identify the Device Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Start with the `ElectrochemicalDevice` class or one of its more specific subclasses, depending on function.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ElectrochemicalDevice"
   }

Subclasses include:

- `BatteryCell`  
- `BatteryPack`  
- `Supercapacitor`  
- `FuelCell`  
- `Electrolyzer`  
- `FlowBattery`  

2. Define Contained Cells
^^^^^^^^^^^^^^^^^^^^^^^^^

Use the property `hasCell` (a subproperty of `emmo:hasPart`) to connect the device to its internal cells.

**Example: device containing one electrochemical cell**

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "BatteryCell",
     "hasCell": {
       "@type": "ElectrochemicalCell",
       "hasElectrode": [
         { "@type": "PositiveElectrode" },
         { "@type": "NegativeElectrode" }
       ],
       "hasElectrolyte": { "@type": "LiquidElectrolyte" },
       "hasSeparator": { "@type": "Separator" }
     }
   }

For multi-cell configurations (packs, stacks, modules), `hasCell` can connect to a list of cell instances, allowing topological descriptions such as *series* or *parallel* connections.

3. Describe Mechanical and Electrical Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Devices include additional structural and functional elements that do not belong to the cell itself.

- `hasCase` — the enclosure or packaging (e.g., pouch, can, shell)  
- `hasTerminal` — the electrical connection points (positive/negative tabs, leads)  
- `hasSafetyComponent` — fuses, vents, valves, or protection circuits  
- `hasSensor` — temperature, voltage, or pressure sensors  
- `hasElectronicController` — management or regulation electronics  

**Example: pouch battery device**

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "BatteryCell",
     "hasCell": { "@type": "ElectrochemicalCell" },
     "hasCase": { "@type": "PouchCase" },
     "hasTerminal": [
       { "@type": "PositiveTerminal" },
       { "@type": "NegativeTerminal" }
     ]
   }

4. Assign Device Properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Device-level properties capture overall performance, geometry, and application-relevant characteristics.

Common examples:

- `NominalVoltage`  
- `RatedCapacity`  
- `SpecificEnergy`  
- `SpecificPower`  
- `CycleLife`  
- `Mass` or `Volume`

**Example: defining device properties**

.. code-block:: json

   {
     "@type": "BatteryCell",
     "hasProperty": [
       {
         "@type": "NominalVoltage",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 3.7 },
         "hasMeasurementUnit": "emmo:Volt"
       },
       {
         "@type": "RatedCapacity",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 4.8 },
         "hasMeasurementUnit": "emmo:AmpereHour"
       },
       {
         "@type": "SpecificEnergy",
         "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 250 },
         "hasMeasurementUnit": "emmo:WattHourPerKilogram"
       }
     ]
   }

These quantitative properties make it possible to query or compare devices using semantic reasoning or SHACL validation.

5. Model Subsystems and Hierarchies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Devices can contain **subsystems**, allowing recursive representation from component → module → pack → system.

| Device level | Typical relation | Example |
|---------------|------------------|----------|
| **BatteryCell** | `hasCell` | Contains one cell |
| **BatteryModule** | `hasComponent` | Contains multiple cells with interconnections |
| **BatteryPack** | `hasSubSystem` | Contains multiple modules plus electronics |
| **EnergyStorageSystem** | `hasSubSystem` | Contains a battery pack and inverter |

**Example: hierarchical pack structure**

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "BatteryPack",
     "hasSubSystem": {
       "@type": "BatteryModule",
       "hasComponent": [
         { "@type": "BatteryCell" },
         { "@type": "BatteryCell" }
       ]
     },
     "hasElectronicController": { "@type": "BatteryManagementSystem" }
   }

Specialized Device Classes
--------------------------

FuelCell
^^^^^^^^

Converts chemical fuel and oxidant into electricity.  

.. code-block:: json

   {
     "@type": "FuelCell",
     "hasCell": { "@type": "ElectrochemicalCell" },
     "hasReactant": { "@type": "Hydrogen" },
     "hasOxidant": { "@type": "Oxygen" },
     "hasElectrolyte": { "@type": "PolymerElectrolyte" }
   }

Electrolyzer
^^^^^^^^^^^^

Performs the reverse of a fuel cell, using electricity to split compounds.

.. code-block:: json

   {
     "@type": "Electrolyzer",
     "hasCell": { "@type": "ElectrochemicalCell" },
     "hasInput": { "@type": "Water" },
     "hasOutput": { "@type": "Hydrogen" }
   }

Supercapacitor
^^^^^^^^^^^^^^

Stores energy through double-layer capacitance or pseudocapacitance.

.. code-block:: json

   {
     "@type": "Supercapacitor",
     "hasElectrode": [
       { "@type": "ActivatedCarbonElectrode" },
       { "@type": "ActivatedCarbonElectrode" }
     ],
     "hasElectrolyte": { "@type": "OrganicElectrolyte" },
     "hasProperty": {
       "@type": "SpecificPower",
       "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 10000 },
       "hasMeasurementUnit": "emmo:WattPerKilogram"
     }
   }


Reasoning and Hierarchical Relations
------------------------------------

Because all composition relations (`hasCell`, `hasComponent`, `hasSubSystem`, etc.)  
are subproperties of `emmo:hasPart`, reasoning engines can infer containment across levels.

::
   If a BatteryPack hasSubSystem BatteryModule,
   and BatteryModule hasComponent BatteryCell,
   then BatteryPack hasPart BatteryCell.

This makes high-level queries (e.g., “find all materials used in this pack”) automatically reach down to cell-level data.

Best Practices
--------------

- Use **ElectrochemicalDevice** (or its subclasses) for *functional products*, not raw electrochemical systems.  
- Connect internal cells using `hasCell` and mechanical/electrical parts using their respective relations.  
- Keep device-level and cell-level properties distinct — e.g., energy density at the device level vs. electrode capacity at the cell level.  
- Use the same `hasProperty` pattern for all quantitative characteristics.  
- For multi-cell systems, clearly model hierarchy (pack → module → cell).  
- If modeling data from datasheets, mark such values as `ConventionalProperty` when not directly measured.  


Summary
-------

An **ElectrochemicalDevice** is a functional system that contains one or more **ElectrochemicalCells**,  
along with supporting mechanical, electrical, and safety components.

| Concept | Relation | Example |
|----------|-----------|----------|
| **ElectrochemicalDevice** | `hasCell`, `hasCase`, `hasTerminal` | pouch cell with aluminum laminate case |
| **BatteryPack** | `hasSubSystem` | pack with modules and BMS |
| **FuelCell** | `hasReactant`, `hasOxidant`, `hasElectrolyte` | H₂–O₂ fuel cell |
| **Supercapacitor** | `hasElectrode`, `hasElectrolyte` | activated carbon capacitor |
| **Relations** | `hasPart`, `hasSubSystem`, `hasComponent` | transitive structure supports reasoning |

By modeling devices this way, you can describe entire electrochemical systems —  
from single cells to full battery packs — with a consistent, interoperable ontology that links structure, materials, and performance.
