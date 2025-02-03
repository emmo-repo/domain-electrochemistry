==============================
Quantities in Electrochemistry
==============================

In the EMMO ontology, **quantities** are used to represent measurable properties of electrochemical systems. These quantities provide critical information about the performance, efficiency, and behavior of electrochemical devices.

By defining electrochemical quantities in terms of their **type, properties, and measurement units**, the ontology provides a structured and interoperable framework for describing performance characteristics in electrochemical systems.

Quantities are defined using the following structure:

1. **Type**: Identifies the type of quantity (e.g., `CellVoltage`, `SpecificCapacity`).
2. **Numerical Value**: Specifies the value of the quantity.
3. **Measurement Unit**: Indicates the unit of the quantity (e.g., volts, ampere-hours per gram).

**Example**: Representing a **CellVoltage** quantity:

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "CellVoltage",
     "hasNumericalPart": {
       "@type": "RealData",
       "hasNumberValue": 3.7
     },
     "hasMeasurementUnit": "emmo:Volt"
   }

In this example:
- The `@type` specifies the quantity as `CellVoltage`.
- The `hasNumericalPart` contains the value `3.7`.
- The `hasMeasurementUnit` references the ontology term for `Volt`.

This basic structure is consistent across all quantity definitions, providing a flexible yet standardized way to represent electrochemical data.

This section provides guidelines for representing these key electrochemical quantities within the ontology, along with structured examples for each type.

.. toctree::
   :maxdepth: 1
   :caption: Quantities Contents
   
   quantities_cell_voltage
   quantities_nominal_voltage
   quantities_overpotential
   quantities_specific_capacity
   quantities_rated_capacity
   quantities_specific_energy
   quantities_energy_density