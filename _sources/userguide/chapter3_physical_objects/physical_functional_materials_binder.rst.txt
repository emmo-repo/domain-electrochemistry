Binder
------

`IRI: https://w3id.org/emmo/domain/electrochemistry#electrochemistry_68eb5e35_5bd8_47b1_9b7f_f67224fa291e <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_68eb5e35_5bd8_47b1_9b7f_f67224fa291e>`_

Description
~~~~~~~~~~~
A **binder** is a component in many electrode formulations, ensuring mechanical stability and cohesion of active materials and conductive additives within the electrode structure. Binders help maintain electrode integrity during charge and discharge cycles, preventing material detachment and enhancing overall electrochemical performance.

Commonly used binders in electrochemical systems include:

.. list-table:: Common Binders
   :header-rows: 1

   * - Name
     - Label
     - IRI
   * - Polyvinylidene Fluoride (PVDF)
     - ``PolyvinylideneFluoride``
     - `IRI: https://w3id.org/emmo/domain/chemical-substance#substance_f2e48e9e_f774_4f42_939f_1fe522efb7c8 <https://w3id.org/emmo/domain/chemical-substance#substance_f2e48e9e_f774_4f42_939f_1fe522efb7c8>`_
   * - Styrene-Butadiene Rubber (SBR)
     - ``StyreneButadiene``
     - `IRI: https://w3id.org/emmo/domain/chemical-substance#substance_210edf30_ad63_438c_97db_f817942db49b <https://w3id.org/emmo/domain/chemical-substance#substance_210edf30_ad63_438c_97db_f817942db49b>`_
   * - Carboxymethyl Cellulose (CMC)
     - ``CarboxymethylCellulose``
     - `IRI: https://w3id.org/emmo/domain/chemical-substance#substance_d36fbe2f_6b0a_4178_b6ca_7373bdefcb51 <https://w3id.org/emmo/domain/chemical-substance#substance_d36fbe2f_6b0a_4178_b6ca_7373bdefcb51>`_

Guidelines for Use
~~~~~~~~~~~~~~~~~~

To represent a **Binder** in the ontology, follow these steps:

1. **Identify the Binder**  
   Define the material using the **domain-chemical-substance ontology** combined with the **Binder** class in the electrochemistry domain.

2. **Assign Properties**  
   Specify **annotation properties** (e.g., ``molecularFormula``) and **objective properties** (e.g., ``Viscosity``, ``GlassTransitionTemperature``).

3. **Link the Binder to a Functional Whole**  
   Use the ``hasBinder`` property to associate the binder with an ``ElectrodeCoating``.

Step 1: Identifying the Binder
"""""""""""""""""""""""""""""""

**Example:** Defining **PVDF** as a binder:
.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": ["Binder", "PVDF"]
   }

Step 2: Assigning Properties
""""""""""""""""""""""""""""

**Example:** Adding properties to **PVDF**:
.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": ["Binder", "PVDF"],
     "molecularFormula": "C2H2F2",
     "hasProperty": [
       {
         "@type": "GlassTransitionTemperature",
         "hasNumericalPart": {
           "@type": "RealData",
           "hasNumericalValue": -39
         },
         "hasMeasurementUnit": "emmo:DegreeCelsius"
       }
     ]
   }

Step 3: Linking the Binder to a Functional Whole
"""""""""""""""""""""""""""""""""""""""""""""""""""

**Example:** Associating PVDF with an electrode coating:
.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ElectrodeCoating",
     "hasBinder": {
       "@type": ["Binder", "PVDF"],
       "molecularFormula": "C2H2F2",
       "hasProperty": [
         {
           "@type": "GlassTransitionTemperature",
           "hasNumericalPart": {
             "@type": "RealData",
             "hasNumericalValue": -39
           },
           "hasMeasurementUnit": "emmo:DegreeCelsius"
         }
       ]
     }
   }

---
