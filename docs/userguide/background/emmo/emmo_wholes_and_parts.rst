Describing Wholes and Parts
===========================

Introduction
------------

One of the central ideas in EMMO is that everything in the physical world can be described as a **whole composed of parts**. This view is called the **holistic perspective**, and it is grounded in *mereology* — the study of part–whole relations.

In this perspective:

- A **whole** is anything that exists as a unified entity.  
- **Parts** are the entities that collectively make up the whole.  

For example:

- A **battery cell** consists of electrodes, electrolyte, separator, and case.  
- Each **electrode** may consist of a coating and a current collector.  
- A **coating** may itself contain active material, binder, and conductive
  additive.

By describing systems in terms of their parts, EMMO provides a clear, logical structure for representing complex physical objects across scales — from atoms to full devices.

The Holistic Perspective in EMMO
--------------------------------

EMMO models mereological relations using the general property ``hasPart`` and its inverse ``isPartOf``. This structure allows any physical entity to be expressed as a hierarchy of parts, enabling queries and reasoning such as:

- *“What are the parts of this object?”*  
- *“Which systems contain this component?”*  
- *“If object A is part of B, and B is part of C, then A is part of C.”*

Because mereological relations are **transitive**, reasoning engines can infer part–whole relationships several levels deep.

.. figure:: ../../assets/img/fig/png/holistic_structure.png
   :align: center
   :alt: Holistic structure example
   :width: 80%

   Example of a hierarchical part–whole structure: a cell as a whole composed of    parts at multiple levels of granularity.

Using hasPart
--------------

The most general way to describe composition in EMMO is with ``emmo:hasPart``.

- ``hasPart`` expresses that the subject *contains* the object as one of its
  physical parts.  
- ``isPartOf`` is its inverse, expressing that the subject *belongs to* the
  object.

This is the safest relation to use when the composition type is unknown or unspecified. It works at any scale and in any domain.

.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "PhysicalObject",
     "hasPart": [
       { "@type": "Electrode" },
       { "@type": "Electrolyte" },
       { "@type": "Separator" }
     ]
   }

Here, the physical object (for example, a battery cell) is described generically as having three main parts. Using ``hasPart`` keeps the model flexible and broadly applicable.

Specialized Subproperties of hasPart
------------------------------------

While ``hasPart`` can be used universally, EMMO also defines several **specialized subproperties** that refine the meaning of part–whole relations. These subproperties add semantic precision, helping you describe *how* a part relates to the whole — whether as a material constituent, a functional component, or a member of a collection.

All of these are **subproperties of ``hasPart``**, meaning that if ``A hasConstituent B`` or ``A hasComponent B``, a reasoning engine will also infer that ``A hasPart B``. This ensures consistency while allowing for more precise modeling.

hasConstituent
~~~~~~~~~~~~~~

**Definition:**  
The relation between an object and one of its holistic parts that contributes to the object under some **spatial-based criteria**.

In practice, ``hasConstituent`` is used to describe **material composition** — the parts that occupy space within the whole and define what it is *made of*. These parts may blend or mix, and they do not necessarily maintain distinct boundaries.

Use ``hasConstituent`` when representing the **material makeup** of substances or mixtures.

Examples:

- A **polymer composite** hasConstituent **filler** and **polymer matrix**.  
- An **electrode coating** hasConstituent **active material**, **binder**, and
  **conductive additive**.  
- A **gas mixture** hasConstituent **oxygen** and **nitrogen**.

.. code-block:: json

   {
     "@type": "ElectrodeCoating",
     "hasConstituent": [
       { "@type": "ActiveMaterial" },
       { "@type": "Binder" },
       { "@type": "ConductiveAdditive" }
     ]
   }

hasComponent
~~~~~~~~~~~~

**Elucidation:**  
The relation between an object and one of its holistic parts that contributes to the **structure or function** of the object while retaining a **distinct identity**.

In EMMO, ``Component`` is a **subclass of ``Constituent``** — every component is a constituent (it occupies space within the whole), but not every constituent is a component. Components are typically **assembled or connected** parts that work together to realize the behavior of the whole.

Use ``hasComponent`` for **structural or functional subunits** that can be identified individually.

Examples:

- A **battery cell** hasComponent **positive electrode**, **negative electrode**,
  **separator**, and **electrolyte**.  
- A **motor** hasComponent **rotor**, **stator**, and **shaft**.  
- A **sensor module** hasComponent **microcontroller** and **housing**.

.. code-block:: json

   {
     "@type": "BatteryCell",
     "hasComponent": [
       { "@type": "PositiveElectrode" },
       { "@type": "NegativeElectrode" },
       { "@type": "Separator" },
       { "@type": "Electrolyte" }
     ]
   }

hasMember
~~~~~~~~~

**Definition:**  
The relation between individuals representing a **collection** and one or more of its **members**.

Unlike ``hasComponent`` or ``hasConstituent``, ``hasMember`` does **not** describe physical composition but **membership** in a set, group, or ensemble.

Use ``hasMember`` when describing **collections or batches** of entities that share a collective identity but are not physically connected.

Examples:

- A **sample batch** hasMember **specimen 1**, **specimen 2**, **specimen 3**.  
- A **dataset** hasMember **file 1**, **file 2**, **file 3**.  
- A **battery module**, treated as a collection, hasMember **cell 1**–**cell n**.

.. code-block:: json

   {
     "@type": "CellBatch",
     "hasMember": [
       { "@id": "ex:Cell_001" },
       { "@id": "ex:Cell_002" },
       { "@id": "ex:Cell_003" }
     ]
   }


Domain-specific subproperties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Domain ontologies extending EMMO often introduce their own **domain-specific part relations** for clarity and query efficiency. For example, in the electrochemistry domain:

- ``hasElectrode`` — instead of a generic ``hasPart`` relation.  
- ``hasSeparator``, ``hasElectrolyte``, ``hasCurrentCollector`` — for defining
  well-known components of a cell.  
- ``hasCoating`` — to describe electrode architecture.

These are subproperties of ``hasPart`` that express physically meaningful relationships without losing generality. A reasoning engine can always infer that if ``A hasElectrode B``, then ``A hasPart B``.

When to choose which relation
-----------------------------

| **Scenario** | **Recommended Relation** | **Description** |
|---------------|---------------------------|-----------------|
| Describing blended or inseparable material composition | ``hasConstituent`` | Use when the whole is defined by the spatial presence of its material parts. |
| Describing structural or functional subparts that retain identity | ``hasComponent`` | Use when parts are assembled, connected, or serve a distinct role in the whole. |
| Describing collections or groups of similar entities | ``hasMember`` | Use for batches, datasets, or ensembles rather than physical assembly. |
| You are working within a domain ontology with specific subproperties (e.g., ``hasElectrode``) | Domain-specific property | Use the most precise available relation. |

Example: describing a battery cell
----------------------------------

Here’s how a battery cell could be represented using different levels of specificity:

**Generic description (using ``hasPart``):**

.. code-block:: json

   {
     "@type": "BatteryCell",
     "hasPart": [
       { "@type": "Electrode" },
       { "@type": "Electrolyte" },
       { "@type": "Separator" }
     ]
   }

**More specific (using domain relations):**

.. code-block:: json

   {
     "@type": "BatteryCell",
     "hasElectrode": [
       { "@type": "PositiveElectrode" },
       { "@type": "NegativeElectrode" }
     ],
     "hasElectrolyte": { "@type": "LiquidElectrolyte" },
     "hasSeparator": { "@type": "MicroporousPolymerSeparator" }
   }

**Describing composition (using ``hasConstituent``):**

.. code-block:: json

   {
     "@type": "ElectrodeCoating",
     "hasConstituent": [
       { "@type": "ActiveMaterial" },
       { "@type": "Binder" },
       { "@type": "ConductiveAdditive" }
     ]
   }

These examples are semantically consistent because all specialized properties (``hasElectrode``, ``hasConstituent``) are subproperties of ``hasPart``. This means generic queries for ``hasPart`` will still return all relevant relationships, even when specialized terms are used.

Reasoning across part hierarchies
---------------------------------

The transitive nature of ``hasPart`` allows for automatic inference. For example:

::
   If A hasPart B and B hasPart C,  
   then A hasPart C.

This means a reasoning engine can deduce, for instance, that:

- a **battery cell** hasPart **active material**, even if only indirect relations (via electrode and coating) were explicitly defined.

Best Practices
--------------

- Use ``hasPart`` when you need flexibility and broad compatibility.  
- Use ``hasComponent`` or ``hasConstituent`` when the distinction between   structural assembly and material mixture matters.  
- Use **domain-specific subproperties** (e.g., ``hasElectrode``,   ``hasSeparator``) when your ontology defines them — they improve clarity and make SPARQL queries easier.  
- Always ensure inverse relations (``isPartOf``, ``isComponentOf``) are also correctly defined in your ontology.  
- Combine part relations with classification and properties to provide rich, semantically consistent descriptions.

Summary
-------

The holistic perspective in EMMO provides a structured way to represent complex systems as **wholes composed of interrelated parts**. It supports reasoning across scales, promotes reuse of modular definitions, and ensures semantic precision through hierarchical relations:

- ``hasPart`` — general purpose.  
- ``hasComponent`` — structural assembly.  
- ``hasConstituent`` — material mixture.  
- Domain-specific subproperties (e.g., ``hasElectrode``) — context-aware precision.

By adopting this structure, you can describe materials, devices, and processes in a way that is **modular, queryable, and logically consistent** with the EMMO framework.
