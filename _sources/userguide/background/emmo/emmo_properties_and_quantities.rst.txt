Properties and Quantities
=========================

Introduction
------------

In science and engineering, we describe the world by assigning **properties** to objects — color, mass, length, hardness, conductivity, and so on. Some of these properties can be *measured* and expressed numerically; others are qualitative or categorical.

EMMO captures this full range through the class ``Property`` and its subclasses. Among these, **Quantity** represents properties that can be expressed as the product of a *number* and a *unit* — such as “1.8 cm,” “1.4 kg,” or “50 Ω.”

.. image:: ../../assets/img/fig/png/Diameter.png
   :align: center
   :alt: Example of a measured diameter.

Understanding Properties in EMMO
--------------------------------

In EMMO, a **Property** is any characteristic that describes an entity or system. It answers questions like:

- What color is it?  
- How heavy is it?  
- What is its porosity, density, or composition?  

A property is always *about* something — a material, a process, or a system.

EMMO distinguishes several types of properties depending on how their values are obtained or defined.

Objective and Subjective Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Objective properties** can be determined through systematic observation or calculation. EMMO includes several key subclasses:

- **MeasuredProperty** — obtained through direct measurement or observation   (e.g., measuring a cell’s voltage with a potentiostat).  
- **ModelledProperty** — computed from experimental or simulation models   (e.g., estimating diffusion coefficient from simulation).  
- **ConventionalProperty** — assigned by convention or agreement, such as a   vendor-specified material density, a standard reference potential, or a rated capacity on a specification sheet.

**Subjective properties**, by contrast, depend on human perception or judgment, such as aesthetic appeal or perceived roughness. These are important for some domains (e.g., quality assessment, usability) but are not expressed numerically in the same way as quantities.

Quantities: Measurable Properties
---------------------------------

A **Quantity** in EMMO is defined as *a quantifiable property of a phenomenon, body, or substance*. All quantities are therefore properties, but not all properties are quantities.

Quantities allow us to express *how much* of something exists — mass, length, time, current, temperature, etc. The `SI Brochure <https://www.bipm.org/en/publications/si-brochure>`__ defines a quantity as *“the product of a number and a unit.”* For example:

- Diameter: ``1.8 cm``  
- Mass: ``1.4 kg``  
- Electric resistance: ``50 Ω``

Structure of Quantities in EMMO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quantities are represented as a **composite of two parts**:

  1. **Numerical Part** — the numeric value (scalar, vector, or tensor).  
  2. **Measurement Unit** — the unit that gives the number meaning.

These are connected through:

- ``emmo:hasNumericalPart``  
- ``emmo:hasMeasurementUnit``

.. admonition:: Example — Expressing a Quantity (Mass) in EMMO

   .. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@graph": [
          {
            "@type": "PhysicalObject",
            "hasProperty": {
              "@type": "Mass",
              "hasNumericalPart": {
                "@type": "emmo:RealData",
                "hasNumberValue": 1.4
              },
              "hasMeasurementUnit": "emmo:Kilogram"
            }
          }
        ]
      }

This expresses that a ``PhysicalObject`` has a property of type ``Mass`` — a Quantity — with a value of **1.4 kilograms**.

Base and Derived Quantities
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quantities follow the SI structure of **base**, **derived**, and **dimensionless** types.

+---------------------------+-----------------+
| Quantity                  | SI Unit         |
+===========================+=================+
| Length                    | metre (m)       |
| Mass                      | kilogram (kg)   |
| Time                      | second (s)      |
| Electric current           | ampere (A)     |
| Temperature               | kelvin (K)     |
| Amount of substance        | mole (mol)     |
| Luminous intensity         | candela (cd)   |
+---------------------------+-----------------+

**Derived quantities** combine base quantities (through multiplication or division):

- **Velocity** = length / time → ``emmo:MetrePerSecond``  
- **Force** = mass × acceleration → ``emmo:Newton``  
- **Energy** = force × distance → ``emmo:Joule``

Scalar, Vector, and Tensor Quantities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quantities can represent scalar values (single numbers), vectors (ordered lists), or tensors (matrices). The numerical part is typed accordingly:

- ``emmo:RealData`` — single numeric value.  
- ``emmo:ArrayData`` — vector of numbers.  
- ``emmo:MatrixData`` — multi-dimensional numeric structure.

.. admonition:: Example — Vector Quantity

   .. code-block:: json

      {
        "@type": "Velocity",
        "hasNumericalPart": {
          "@type": "emmo:ArrayData",
          "hasNumberValue": [3.0, 1.2, -0.5]
        },
        "hasMeasurementUnit": "emmo:MetrePerSecond"
      }

Dimensionless Quantities
~~~~~~~~~~~~~~~~~~~~~~~~

Some quantities, like relative humidity or refractive index, are **dimensionless**. They can be represented using ``emmo:UnitOne`` or by omitting the unit entirely if context makes it clear.

Examples:

- Relative humidity = 0.65  
- Refractive index = 1.52  
- Number of cycles = 250  

Linking Properties to Entities
------------------------------

Properties are always *about* something. In EMMO, this relationship is typically expressed with ``emmo:hasProperty``, but there are two equivalent modeling approaches you can choose depending on your use case.

**1. Using dedicated object properties**

EMMO defines specialized subproperties of ``hasProperty`` such as ``hasMeasuredProperty``, ``hasModelledProperty``, and ``hasConventionalProperty``. These explicitly indicate how the property value was obtained.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "PhysicalObject",
     "hasConventionalProperty": {
       "@type": "Mass",
       "hasNumericalPart": {
         "@type": "emmo:RealData",
         "hasNumberValue": 1.4
       },
       "hasMeasurementUnit": "emmo:Kilogram"
     }
   }

This states that the ``PhysicalObject`` has a *ConventionalProperty* of type ``Mass`` equal to 1.4 kg — for instance, a value read from a vendor datasheet or standard specification.

**2. Using dual typing**

Alternatively, you can use the general ``hasProperty`` relation and make the property instance a member of both ``Mass`` and ``ConventionalProperty`` (or ``MeasuredProperty``, ``ModelledProperty``, etc.). This approach is more compact and is often preferred when serializing to JSON-LD or RDF.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "PhysicalObject",
     "hasProperty": {
       "@type": ["Mass", "ConventionalProperty"],
       "hasNumericalPart": {
         "@type": "emmo:RealData",
         "hasNumberValue": 1.4
       },
       "hasMeasurementUnit": "emmo:Kilogram"
     }
   }

Both patterns are **semantically equivalent** and fully compatible with EMMO. Choose whichever fits your data workflow and tooling best:

- **Dedicated subproperties** (`hasMeasuredProperty`, etc.) make provenance clear at the relation level and are ideal for SHACL validation or SPARQL queries.
- **Dual typing** keeps data compact and is easier to generate automatically in JSON-LD or programmatic exports.

In both cases, EMMO ensures that properties remain logically connected to the entity they describe and can be reasoned over according to their physical and provenance types.


Why this structure matters
--------------------------

- It reflects the **ontology hierarchy** — ``Quantity ⊆ Property``.  
- It keeps numerical information attached to the property itself.  
- It supports validation and reasoning (e.g., checking that mass properties have
  units of mass).  
- It distinguishes between measured, modelled, and conventional data origins.


Reasoning and Validation
------------------------

Because each Quantity links its **type**, **unit**, and **value**, EMMO supports
automatic checks and reasoning such as:

- Verifying that the unit is dimensionally consistent with the property type.  
- Converting units to a standard system (e.g., SI) for comparison.  
- Inferring derived quantities (e.g., compute density from mass and volume).  
- Ensuring only ``Quantity``-type properties contain numerical parts.

Summary
-------

- **Property** — any descriptive characteristic of an entity.  
- **Quantity** — a subclass of Property that is measurable (has a number and a
  unit).  
- **MeasuredProperty**, **ModelledProperty**, and **ConventionalProperty** —
  refine how the value was obtained.  
- Properties can be scalar, vector, or tensor-valued.  
- All properties are connected to the entity they describe using
  ``hasProperty``.  
- This structure makes EMMO-based data explicit, consistent, and interoperable
  across domains.

In short:  
> Every Quantity is a Property — but not every Property is a Quantity.
