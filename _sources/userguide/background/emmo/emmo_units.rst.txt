Units
=====

Units of measurement ensure precision and standardization in data exchange. Without explicit units, numerical values can become meaningless or even dangerous when combined or compared.

.. admonition:: Case Study: The Mars Climate Orbiter  

    On September 23, 1999, NASA's Mars Climate Orbiter was lost due to a unit mismatch. A subcontractor’s software provided motor impulse values in **pound-force seconds**, while NASA’s software expected values in **Newton seconds**. The resulting miscalculation caused the spacecraft to enter an incorrect trajectory, leading to its destruction.
    
    Even when numerical data is correct, if the unit is misinterpreted, the consequences can be severe. Ontologies help prevent such errors by enforcing explicit unit definitions.

Several widely used ontological frameworks express units, including `Quantities, Units, Dimensions, and Data Types Ontologies (QUDT) <https://www.qudt.org/>`__ and `Semantic Aspect Meta Model (SAMM) <https://eclipse-esmf.github.io/samm-specification/snapshot/units.html>`__. 

EMMO also provides a structured approach for unit representation, ensuring self-consistency within the EMMO framework. By aligning with QUDT, which offers a comprehensive and standards-compliant unit representation, EMMO ensures compatibility across multiple ontological systems.

Expressing Units in EMMO
------------------------

EMMO provides human-readable IRIs for units, making them intuitive and easy to use. The unit IRIs follow the structure: :code:`<namespace>#<UnitName>`

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
-------------

EMMO supports unit conversion by providing data properties such as :code:`hasSIConversionMultiplier` and :code:`hasSIConversionOffset`. These properties define conversion factors relative to SI units:

.. code-block::

   emmo:CentiMetre hasSIConversionMultiplier 0.01 .
   emmo:MilliGram hasSIConversionMultiplier 1E-6 .

Units in EMMO are also classified by physical dimensionality. For example:

- :code:`emmo:Kilogram` is a :code:`MassUnit`
- :code:`emmo:MilliMetre` is a :code:`LengthUnit`

This classification enables automated reasoning. If an instance of :code:`Mass` is assigned the unit :code:`MicroGram`, the system will validate it. However, assigning a length-based unit like :code:`CentiMetre` to mass would trigger an inconsistency.

Supported Systems of Units
--------------------------

EMMO supports both SI and non-SI units:

- **SI Units** — defined by the International System of Units (metre, kilogram, second, etc.)
- **Derived Units** — combinations such as ``Newton``, ``Volt``, ``Pascal``
- **Non-SI Units** — used in specific domains, such as ``minute``, ``liter``, or ``electronvolt (eV)``
