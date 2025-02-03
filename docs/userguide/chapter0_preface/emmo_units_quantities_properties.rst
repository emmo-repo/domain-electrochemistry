Units, Quantities, and Properties
---------------------------------

Units
~~~~~

Units of measurement are essential in ontologies, ensuring precision and standardization when describing quantities. Without a structured representation of units, data exchange across domains becomes error-prone and inconsistent. Scientific and engineering ontologies address this by explicitly defining units and their relationships, ensuring clarity and interoperability.

.. admonition:: Case Study: The Mars Climate Orbiter  

    On September 23, 1999, NASA's Mars Climate Orbiter was lost due to a unit mismatch. A subcontractor’s software provided motor impulse values in **pound-force seconds**, while NASA’s software expected values in **Newton seconds**. The resulting miscalculation caused the spacecraft to enter an incorrect trajectory, leading to its destruction.
    
    This highlights the dangers of inconsistent unit representation in software. Even when numerical data is correct, if the unit is misinterpreted, the consequences can be severe. Ontologies help prevent such errors by enforcing explicit unit definitions.

Several widely used ontological frameworks express units, including `Quantities, Units, Dimensions, and Data Types Ontologies (QUDT) <https://www.qudt.org/>`__ and `Semantic Aspect Meta Model (SAMM) <https://eclipse-esmf.github.io/samm-specification/snapshot/units.html>`__. 

EMMO also provides a structured approach for unit representation, ensuring self-consistency within the EMMO framework. By aligning with QUDT, which offers a comprehensive and standards-compliant unit representation, EMMO ensures compatibility across multiple ontological systems.

Expressing Units in EMMO
^^^^^^^^^^^^^^^^^^^^^^^^
EMMO provides human-readable IRIs for units, making them intuitive and easy to use. The unit IRIs follow the structure: :code:`<namespace>#<unit_name>`

For example, the IRI for "metre" in EMMO is:

:code:`https://w3id.org/emmo#Metre`

To simplify handling, EMMO defines a namespace prefix, allowing for the shorthand form:

:code:`emmo:Metre`

Units follow Pascal case naming conventions:

.. code-block::

   emmo:MilliVolt
   emmo:CentiMetre
   emmo:KiloWatt

An exception is :code:`emmo:Kilogram`, as the SI base unit is the kilogram rather than the gram. Compound units are expressed similarly:

.. code-block::

   emmo:MetrePerSecond
   emmo:AmpereHour
   emmo:MilliGramPerSquareCentiMetre
   emmo:KilogramPerCubicMetre

This ensures units remain both machine-readable and human-interpretable, reducing ambiguity and improving usability.

Unit Features
^^^^^^^^^^^^^
EMMO supports unit conversion by providing data properties such as :code:`hasSIConversionMultiplier` and :code:`hasSIConversionOffset`. These properties define conversion factors relative to SI units:

.. code-block::

   emmo:CentiMetre hasSIConversionMultiplier 0.01 .
   emmo:MilliGram hasSIConversionMultiplier 1E-6 .

Units in EMMO are also classified by physical dimensionality. For example:

- :code:`emmo:Kilogram` is a :code:`MassUnit`
- :code:`emmo:MilliMetre` is a :code:`LengthUnit`

This classification enables automated reasoning. If an instance of :code:`Mass` is assigned the unit :code:`MicroGram`, the system will validate it. However, assigning a length-based unit like :code:`CentiMetre` to mass would trigger an inconsistency.

Supported Systems of Units
^^^^^^^^^^^^^^^^^^^^^^^^^^
EMMO supports both SI and non-SI units:

- **SI Units**: The standard units defined by the International System of Units (e.g., metre, kilogram, second).
- **Non-SI Units**: Includes units commonly used alongside SI (e.g., liter, minute) and domain-specific units such as electronvolt (eV).

Quantities in EMMO
~~~~~~~~~~~~~~~~~~
The `SI handbook <https://physics.nist.gov/cuu/pdf/sp811.pdf>`__ defines a quantity as "the product of a number and a unit." For example, 

- Diameter: `"1.8 cm"`
- Mass: `"1.4 kg"`
- Electric Resistance: `"50 ohm"`

.. image:: ../../assets/img/fig/png/Diameter.png

EMMO follows this convention and structures a quantity using two parts: a **numerical part** and a **unit**. To express a quantity in EMMO, we first define the type of quantity, and then link it to its numerical part (:code:`hasNumericalPart`) and its unit (:code:`hasMeasurementUnit`). 

.. admonition:: Example: Expressing a Quantity in EMMO

   .. code-block:: json

      {
          "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
          "@type": "Diameter",
          "hasNumericalPart": {
              "@type": "RealData",
              "hasNumberValue": 1.8
          },
          "hasMeasurementUnit": "emmo:CentiMetre"
      }

Properties
~~~~~~~~~~
A **semiotic property** in EMMO is a well-defined, measurable characteristic (it should not be confused with an RDF property, which represents relationships in linked data). A property is a characteristic that describes an object or system. Properties answer specific questions such as:

- What color is it? (e.g., black, red)
- How heavy is it? (e.g., 1.4 kg)
- What is its hardness? (e.g., 10000 HV)

Types of Properties in EMMO
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**1. Objective Properties**
These are properties that can be determined through a well-defined, systematic procedure:

- **Conventional Property**: A value determined by agreement, such as a vendor-specified material property.
- **Measured Property**: A property obtained through direct observation or instrumentation (e.g., measuring mass with a scale).
- **Modelled Property**: A property derived from experimental data using a computational model.

**2. Subjective Properties**
These properties are based on perception rather than measurement, such as aesthetic preferences (e.g., "beauty on a scale of 1 to 10").

**3. Physical Quantities**
These refer to measurable attributes such as mass, length, and temperature. They are represented by numerical values and units.

**4. Ordinal Quantities**
These allow comparison but not algebraic operations. For example, Rockwell C hardness values indicate hardness rankings but cannot be added or subtracted meaningfully.

.. admonition:: Example: Expressing a Property in EMMO

   .. code-block:: json

      {
          "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
          "@type": "Device",
          "hasProperty": {
              "@type": "Mass",
              "hasNumericalPart": {
                  "@type": "RealData",
                  "hasNumberValue": 10
              },
              "hasMeasurementUnit": "emmo:Kilogram"
          }
      }

This structured approach ensures that **units, quantities, and properties** in EMMO are clearly defined, machine-readable, and interoperable with other ontological frameworks.