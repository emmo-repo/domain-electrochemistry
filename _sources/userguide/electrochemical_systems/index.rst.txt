Describing Electrochemical Systems
==================================

This chapter introduces how to describe real electrochemical systems — from individual materials to complete devices — using the Electrochemistry Domain Ontology.

Rather than focusing on definitions, this section shows *how to build descriptions* of things using ontology classes and relationships. Whether you are describing a single electrode, a test cell, or a complete battery, the same principles apply:

1. Identify **what kind of thing** you are describing (e.g., an electrode, electrolyte, or cell).  
2. Define **its parts or composition** using `hasPart` and its subproperties.  
3. Assign **relevant properties** such as mass, thickness, or potential.  
4. Link it to **processes or measurements** that involve it.

By following these simple patterns, you can describe almost any electrochemical entity in a clear, machine-readable way.

Core Patterns for Describing Systems
------------------------------------

1. Start from the whole
^^^^^^^^^^^^^^^^^^^^^^^

An electrochemical system can be represented as a *PhysicalObject*. An electrochemical cell, an electrode, or a material are all subclasses of `PhysicalObject`.

Use *parthood* relations to connect the whole to its parts. Parthood relations include general terms like `hasPart`, `hasConstituent`, `hasComponent`, as well as domain-specific relations like `hasElectrode`, `hasElectrolyte`, etc.

.. topic:: Example — Simple device with electrodes, electrolyte, and separator
   :class: example

   .. code-block:: json
      :caption: JSON-LD
      :name: ex-device-basic
      :linenos:

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "ElectrochemicalDevice",
        "hasPositiveElectrode": { "@type": "Electrode" },
        "hasNegativeElectrode": { "@type": "Electrode" },
        "hasElectrolyte": { "@type": "LiquidElectrolyte" },
        "hasSeparator": { "@type": "Separator" }
      }

Here, `hasElectrode`, `hasElectrolyte`, and `hasSeparator` are **domain-specific subproperties** of `hasPart`, providing semantic precision while remaining interoperable.

.. admonition:: ElectrochemicalCell vs. ElectrochemicalDevice
   :class: tip

   These two classes often cause confusion because they both describe “things that do electrochemistry” — but they have different scopes:

   - **ElectrochemicalCell** represents the **physical system** in which electrochemical reactions occur.  
     It focuses on the internal structure — electrodes, electrolyte, separator, and their physical configuration.

   - **ElectrochemicalDevice** represents a **functional or engineered system** designed to perform an electrochemical task or deliver a service.  
     It may *contain one or more cells* and additional components like control electronics, sensors, housing, or power management units. 

   In short:   
   
   - Use **ElectrochemicalCell** when describing the **reactive unit** that comprises two electrodes in contact with an electrolyte.   

   - Use **ElectrochemicalDevice** when describing the **complete system** that uses one or more cells - together with the case, terminals and other support hardware - to perform a function.


2. Describe each part in more detail
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each part can itself be decomposed into smaller parts or described by its material composition.

.. topic:: Example — Electrode with coating and current collector
   :class: example

   .. code-block:: json
      :caption: JSON-LD
      :name: ex-electrode-structure
      :linenos:

      {
          "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
          "@type": "PositiveElectrode",
          "hasCoating": {
              "@type": "ElectrodeCoating",
              "hasActiveMaterial": { "@type": "LithiumIronPhosphate"},
              "hasBinder":         { "@type": "PolyvinylideneFluoride"},
              "hasAdditive":       { "@type": "CarbonBlack"}
          },
          "hasCurrentCollector": { "@type": ["Aluminum", "Foil"]}
      }


3. Add properties and quantities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each object can have measurable or defined properties (mass, thickness, composition, etc.).  
Attach these using `hasProperty`.

.. topic:: Example — Assigning a mass to an electrode

   Each object can have measurable or defined properties.

   .. code-block:: json
      :caption: JSON-LD
      :name: ex-mass-positive-electrode
      :linenos:

      {
        "@type": "PositiveElectrode",
        "hasProperty": {
          "@type": "Mass",
          "hasNumericalPart": { "@type": "RealData", "hasNumberValue": 1.25 },
          "hasMeasurementUnit": "emmo:Gram"
        }
      }

You can also distinguish whether the value is **measured**, **modelled**, or **conventional** by using subclasses such as:
- `MeasuredProperty`
- `ModelledProperty`
- `ConventionalProperty`

4. Link to processes and measurements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Objects can participate in electrochemical processes or measurements.  
Use `hasParticipant`, `hasInput`, and `hasOutput` to describe their role in a process.

.. topic:: Example — Cell undergoing charging
   :class: example

   .. code-block:: json
      :caption: JSON-LD
      :name: ex-charging-process
      :linenos:

      {
        "@type": "ChargingProcess",
        "hasInput": { "@id": "ex:DischargedCell" },
        "hasOutput": { "@id": "ex:ChargedCell" },
        "hasParticipant": [
          { "@id": "ex:PositiveElectrode" },
          { "@id": "ex:NegativeElectrode" },
          { "@id": "ex:Electrolyte" }
        ]
      }

This pattern links the physical system (`ElectrochemicalCell`) to the activity (`ChargingProcess`) that changes its state.

Example: Putting It All Together
--------------------------------

Here is a minimal but complete description of an **electrochemical device** built using the ontology:

.. topic:: Example — End-to-end electrochemical device description
   :class: example

   .. code-block:: json
      :caption: JSON-LD
      :name: ex-electrochemical-device-complete
      :linenos:

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "ElectrochemicalDevice",
        "hasPositiveElectrode": {
            "@type": "Electrode",
            "hasCoating": [
              {
                "@type": "ElectrodeCoating",
                "hasActiveMaterial": { "@type": "LithiumIronPhosphate"},
                "hasBinder":         { "@type": "PolyvinylideneFluoride"},
                "hasAdditive":       { "@type": "CarbonBlack"}
              },
            "hasCurrentCollector": { "@type": ["Aluminum", "Foil"]}
            ]
          },
        "hasNegativeElectrode": {
            "@type": "NegativeElectrode",
            "hasCoating": { 
                "@type": "ElectrodeCoating",
                "hasActiveMaterial": { "@type": "Graphite"},
              },
            "hasCurrentCollector": { "@type": ["Copper", "Foil"]}
          },
        "hasElectrolyte": { "@type": "LiquidElectrolyte" },
        "hasSeparator": { "@type": "MicroporousPolymerSeparator" },
        "hasProperty": [
          {
            "@type": "NominalVoltage",
            "hasNumericalPart": { "hasNumberValue": 3.6 },
            "hasMeasurementUnit": "emmo:Volt"
          },
          {
            "@type": "NominalCapacity",
            "hasNumericalPart": { "hasNumberValue": 1.2 },
            "hasMeasurementUnit": "emmo:AmpereHour"
          }
        ]
      }

This structure is modular, readable, and machine-interpretable — enabling you to query, validate, and link the data across experiments, simulations, and repositories.

Best Practices
--------------

- Use **domain-specific subproperties** like `hasElectrode`, `hasElectrolyte`, and `hasSeparator` where available.  
- For composition, prefer `hasConstituent` (for mixtures) or `hasComponent` (for assemblies).  
- Keep each level of description meaningful: cell → electrode → coating → material.  
- Always attach quantitative values using `hasProperty` with `hasNumericalPart` and `hasMeasurementUnit`.  
- Use unique IRIs (or dataset-local identifiers) for each distinct physical instance.

.. toctree::
   :maxdepth: 2

   materials
   electrodes
   electrolytes
   electrochemical_cells
   electrochemical_devices
