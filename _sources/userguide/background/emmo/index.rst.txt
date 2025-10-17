Elementary Multiperspective Materials Ontology (EMMO)
=====================================================

Introduction
------------

The **Elementary Multiperspective Materials Ontology (EMMO)** is the official top-level ontology of the European Materials Modelling Council (EMMC). It provides a common, physics-based foundation for describing materials, processes, and measurements in a way that connects scientific knowledge with digital data.

Put simply, EMMO is a **semantic framework for science** — a bridge between how humans reason about the world and how computers represent it. It defines a shared, logically consistent structure that supports interoperability between different domains, such as chemistry, physics, engineering, and data science.

Why EMMO?
---------

Scientific information is diverse. A single experiment might involve:

- physical samples and instruments,  
- abstract models and mathematical relations,  
- measurements stored in databases,  
- and textual descriptions in publications.

Traditionally, these pieces live in separate systems with little semantic connection. EMMO provides a unifying layer that allows us to describe all of them — *matter, models, data, and meaning* — in one coherent framework.

By grounding everything in a common ontology, EMMO enables machines to understand how a **measurement**, a **simulation**, and a **physical object** are related. This makes it possible to link data from different sources and automate tasks that would otherwise require manual interpretation.

Philosophical roots (in plain language)
---------------------------------------

EMMO is based on ideas from both **philosophy** and **physics**. From philosophy, it borrows the concept of *ontology* — a systematic account of what exists and how things relate. From physics, it adopts the principle that every entity we describe should be anchored to physical reality: a particle, a field, a process, or an observation.

The result is an ontology that models the world from **multiple perspectives**:

- **Physical** — how things exist and interact in space and time.  
- **Semiotic** — how we *represent* those things (data, symbols, language).  
- **Mathematical** — how we *quantify* and *model* their behaviour.  

Hence the name *Elementary Multiperspective Materials Ontology*.

Core principles
---------------

1. **Reality-based**  
   Every class in EMMO ultimately refers to something that can be observed, measured, or represented.

2. **Graph-based logic**  
   Relationships between entities (part-of, has-participant, represents, etc.) are defined using RDF and OWL, ensuring logical consistency and reasoning.

3. **Modularity**  
   EMMO is designed as a foundation that other ontologies can extend — such as *domain-electrochemistry*, *domain-battery*, and *domain-chemical-substance*.

4. **Interoperability**  
   Because it follows Semantic Web standards, EMMO can integrate seamlessly with datasets, software, and databases across scientific fields.

What EMMO provides
------------------

- A consistent vocabulary for describing *physical systems, materials, and processes*.
- A framework for connecting *experimental, modelling, and simulation data*.
- Logical definitions that enable **automated reasoning**, **data validation**, and **semantic interoperability** across projects.
- A solid base for developing **domain ontologies** that inherit common meaning.

Relation to other ontologies
----------------------------

EMMO sits at the **top** of the ontology hierarchy. Other ontologies — such as the Domain Electrochemistry Ontology or the Battery Ontology — extend EMMO to specialise its concepts for specific fields.

For example:

::
   EMMO → defines Matter, Process, Property
     ↓
   Domain Electrochemistry → defines Electrode, Electrolyte, IonTransport
       ↓
   Domain Battery → defines Cell, Separator, Charging, Discharging

This layered approach ensures that all domain ontologies remain compatible with each other and with the broader Semantic Web ecosystem.

.. figure:: images/emmo_hierarchy.svg
   :align: center
   :alt: Hierarchy of ontologies extending EMMO
   :width: 80%

   The EMMO provides a common foundation for domain ontologies that describe
   specific scientific and engineering systems.

Why this matters for researchers
--------------------------------

By using EMMO as a common foundation, data and models from different disciplines can speak the same language. This supports:

- **FAIR data** — findable, accessible, interoperable, reusable  
- **Cross-domain linking** — connecting experiments, simulations, and literature  
- **Automation** — enabling reasoning, query, and workflow integration

EMMO is not an abstract philosophical exercise — it is a practical tool for building a **digital ecosystem for science**, where knowledge can flow freely between people, software, and data.

Contents
--------

.. toctree::
   :maxdepth: 2
   
   emmo_units
   emmo_properties_and_quantities
   emmo_measurements
   emmo_processes
   emmo_wholes_and_parts
   emmo_naming_conventions

