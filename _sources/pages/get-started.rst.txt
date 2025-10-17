Getting Started
===============

Welcome
--------

The Electrochemistry Domain Ontology is part of the **Battery2030+** effort to make eletrochemistry research data structured, searchable, and interoperable across projects and institutions.

It provides a **shared vocabulary** for describing materials, processes, and test data in a consistent and  machine-readable way — so that your eletrochemistry data can be *understood, reused, and connected* automatically.

Why Ontologies Matter
---------------------

Electrochemistry research spans chemistry, physics, materials science, and engineering. Each field uses different terms and data formats, which makes sharing and reusing data difficult.

An **ontology** brings these worlds together by defining common concepts and how they relate — for example:

::

   ElectrochemicalCell → hasPositiveElectrode → Electrode  
   Electrode → hasActiveMaterial → Zinc

By structuring information in this way, we make it easier to:
- Compare data from different laboratories or formats.
- Link experimental and simulation results.
- Ensure datasets remain usable in the future.

What You Can Do
---------------

Using this ontology, you can:

- Describe **eletrochemistry components** (electrodes, electrolytes, separators, etc.)
  with standardized terminology.
- Annotate **datasets** and **experimental procedures** so they are FAIR.
- Link **test data** and **models** across projects.
- Publish machine-readable metadata in repositories such as Zenodo.

Core Components
---------------

The ontology ecosystem consists of three main parts:

- **Elementary Multiperspective Materials Ontology (EMMO)** —  
  the foundational framework that provides the logical backbone for all domain ontologies. EMMO defines the most general scientific concepts such as *material*, *process*, *property*, and *measurement*, and establishes how they are related. It ensures that all downstream ontologies share a common formal language and can interoperate seamlessly.

- **Domain Chemical Substance Ontology** —  
  focuses on describing chemical entities and their composition, structure, and relationships. It defines what a *substance* is, how it differs from a *mixture* or a *compound*, and how these concepts link to measurable properties like molar mass or density. This ontology forms the chemical foundation for describing electrode materials, electrolytes, binders, and additives.

Where to Go Next
----------------

- :doc:`linked-data-primer` — learn how linked data works and what JSON-LD means.
- :doc:`ontology-overview` — explore the structure of the eletrochemistry and
  electrochemistry ontologies.
- :doc:`examples` — see practical templates for your own data.
