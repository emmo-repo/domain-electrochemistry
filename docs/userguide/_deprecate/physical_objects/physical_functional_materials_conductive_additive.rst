Conductive Additive
-------------------

`IRI: https://w3id.org/emmo/domain/electrochemistry#electrochemistry_82fef384_8eec_4765_b707_5397054df594 <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_82fef384_8eec_4765_b707_5397054df594>`_

Description
~~~~~~~~~~~
A **conductive additive** improves the electrical conductivity of an electrode by forming conductive pathways between active material particles. These additives are necessary for ensuring efficient electron transport, reducing internal resistance, and improving electrode performance.

Commonly used conductive additives include:

.. list-table:: Common Conductive Additives
   :header-rows: 1

   * - Name
     - Label
     - IRI
   * - Carbon Black
     - ``CarbonBlack``
     - `IRI: https://w3id.org/emmo/domain/chemical-substance#substance_0a5cb747_60cf_4929_a54a_712c54b49f3b <https://w3id.org/emmo/domain/chemical-substance#substance_0a5cb747_60cf_4929_a54a_712c54b49f3b>`_

Guidelines for Use
~~~~~~~~~~~~~~~~~~

1. **Identify the Conductive Additive**  
   Define the material using the **domain-chemical-substance ontology** combined with the **ConductiveAdditive** class.

2. **Assign Properties**  
   Specify **annotation properties** (e.g., ``molecularFormula``) and **objective properties** (e.g., ``ElectricalConductivity``, ``SurfaceArea``).

3. **Link the Conductive Additive to a Functional Whole**  
   Use the ``hasConductiveAdditive`` property to connect it to an ``ElectrodeCoating``.

**Example:** Defining and linking **Carbon Black**:

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ElectrodeCoating",
     "hasConductiveAdditive": {
       "@type": "CarbonBlack"
     }
   }

---