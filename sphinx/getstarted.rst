Quick Start
================================

This ontology is used mostly for generating linked data and complying with the FAIR data guidelines (although it can also do much more!). It provides machine-readable persistent identifiers for terms and semantic relations that help describe what things are and how they are related to each other.

An easy way to get started is to use the ontology vocabulary to create semantic linked data using JSON-LD files. We've provided some examples that you are free to re-use or modify for your own needs. 

But if you are new to working with ontologies, we recommend you follow this step-by-step guide to understand the background and make your first piece of linked data. 

Step 1: Install Protégé
~~~~~~~~~~~~~~~~~~~~~~~

`Protégé <https://protege.stanford.edu/>`__ is a graphical ontology editor developed by Stanford University. It is free and one of the most widely used tools for ontology development. You can read more about it in the tools section. 

Step 2: Download the pre-inferred version of the ontology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ontologies within the EMMO universe import many different modules to try to re-use knowledge and terms from other domains. We then run a tool called a "reasoner" to make logical inferrences about how terms from different domains are connected, and lump them into one ontology. 

We make it easy for you by providing a pre-inferred version in advance. You can download it from the GitHub repository `download it from the GitHub repository <https://github.com/emmo-repo/domain-electrochemistry/blob/master/electrochemistry-inferred.ttl>`__  or access it at anytime using this URL:

https://raw.githubusercontent.com/emmo-repo/domain-electrochemistry/master/electrochemistry-inferred.ttl

Step 3: Open and explore the ontology file in Protégé
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Within Protégé, you can explore the class hierarchy that contains all the "things" that are included in the ontology, as well as the object properties that describe how those things are related to each other. There are a few things to notice:

#. **Each item has a unique, persistent, and machine readable identifier called an IRI.** An IRI (Internationalized Reference Identifier) is the official identifier for that term. It is the anchor to which all other information is linked. In the EMMO universe, IRIs usually contain some Universal Unique Identifier (UUID) character sequence that ensures their uniqueness, but also makes them hard for humans to read. But fear not! Each term also comes with a set of human readable labels called prefLabel and altLabel.

#. **Each item has one human-readable preferred label and can have many alternative labels.** The EMMO universe uses the SKOS terminology for labelling items. The main label for the term is called its prefLabel (short for preferred label) and is often expressed in the source files as skos:prefLabel. But sometimes, there can be multiple labels for the same thing. In that case we use skos:altLabel to list possible alternative labels. 

#. **Each item has an elucidation, describing the meaning of the term.** The elucidation is a short human-readable text that describes the conceptualization for the term. It should give some insight into what the term means and how it can be used.

#. **Many terms have links to other sources of information.** For many terms, there are other authoritative sources of information available that can provide more context about its meaning. To account for that, we include annotations that point to places like the IEC Vocabulary, IUPAC Goldbook, DBpedia, WikiData, or Wikipedia where humans or machines can go to retrieve more information. 

.. grid::

    .. grid-item-card::
        :link: tools.html

        :octicon:`tools;1em;sd-text-info`  Tools
        ^^^^^^^^^^^
        The right tool for the right job. Here are some tools that can help you work with ontologies, knowledge graphs, and linked data. 

    .. grid-item-card::
        :link: resources.html

        :octicon:`book;1em;sd-text-info`  Resources
        ^^^^^^^^^^^
        Here are some other resources and best practices for creating linked data on the web.

What do I use this for?
~~~~~~~~~~~~~~~~~~~~~~~
 Terms and elucidations are derived from authoritative sources like the IEC and IUPAC, so you can be sure that your data & metadata are properly annotated.

How do I use it?
~~~~~~~~~~~~~~~~
The easiest way is to use it to create JSON-LD files. 

Why should I do this?
~~~~~~~~~~~~~~~~~~~~~

Persistent identifiers
----------------------

This ontology assigns persistent machine-readable identifiers to
concepts from the electrochemistry domain. These identifiers facilitate
data exchange and interoperability among various tools and systems. It
includes annotations to other sources of information including
`DBPedia <https://www.dbpedia.org/>`__ and
`Wikidata <https://www.wikidata.org/>`__.

Standardized Nomenclature
-------------------------

The ontology builds on standardized nomenclature for electrochemistry,
relying on recognized authorities including
`IUPAC <https://iupac.org/what-we-do/nomenclature/>`__ and the
`IEC <https://www.electropedia.org/>`__. IUPAC is the
universally-recognized authority on chemical nomenclature and
terminology, and IEC is the the world’s leading organization that
prepares and publishes International Standards for all electrical,
electronic and related technologies. This consistency in naming
conventions enhances collaboration and data sharing.

Key Features
------------

-  Seamless integration with the EMMO ontology.
-  Provides persistent machine-readable identifiers for electorchemical
   systems, devices, methods, datasets, and quantities.
-  Standardized nomenclature for electrochemical entities.
-  Facilitates data exchange and interoperability within the EMMO
   ecosystem.

Usage
-----

Researchers, domain experts, and developers within the electrochemical
communities can utilize the ontology for various purposes, including:

-  Incorporating consistent and standardized information into their
   modeling and simulation activities.
-  Enhancing data interoperability between modeling tools, databases,
   and platforms.
-  Supporting research projects that require precise and standardized
   electrochemical knowledge representation.
-  Building applications, databases, or knowledge graphs that leverage
   EMMO and require electrochemical information.
-  Generating linked data in the semantic web.
-  Complying with FAIR data mandates (FAIR Guidelines available
   `here <FAIR.md>`__)

Structure and Integration with EMMO
-----------------------------------

The Electrochemistry Domain Ontology is an official domain on the EMMO.
The asserted source consists of two files: - ``electrochemistry.ttl``:
describes terms and object properties for the electrochemistry domain. -
``electrochemicalquantities.ttl``: describes the physical quantities
related to the electrochemistry domain. It is encapsulated to allow it
to be imported by other EMMO domains without needing to import the
entire ontology.

The electrochemistry domain also imports other EMMO domains: - `Chemical
Substance Domain
Ontology <https://github.com/emmo-repo/domain-chemical-substance>`__:
provides material annotations for electrochemical (meta)data.

The import structure is summarized in the following table:

.. list-table::
   :header-rows: 1

   * - **Imported Ontologies**
     - **Version**
   * - EMMO
     - 1.0.0-beta5
   * - chemical-substance
     - 0.2.0-alpha 

For simplicity, we complie the source files and other imports into a
`pre-inferred
ontology <inferred_version/electrochemistry-inferred.ttl>`__. This is
the result of running the asserted source files through a semantic
reasoner and includes both asserted and inferred properties in a clear
graph.

Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

Before you begin, we recommend that you install the following tools.
They are not all required, but greatly simplify the process of working
with ontologies:

-  `Protégé <https://protege.stanford.edu/>`__ (a graphical ontology
   editor)

   -  Installation instructions are available
      `here <https://protege.stanford.edu/software.php#desktop-protege>`__.

-  `EMMOntoPy <https://github.com/emmo-repo/EMMOntoPy>`__ (python
   package for working with EMMO ontologies)

   -  Installation instructions are available
      `here <https://github.com/emmo-repo/EMMOntoPy#installation>`__.

-  `RDFLib <https://rdflib.readthedocs.io/en/stable/>`__ (optional,
   python package for working with RDF graphs)

   -  Installation instructions are available
      `here <https://rdflib.readthedocs.io/en/stable/gettingstarted.html>`__.

-  `VS Studio Code <https://code.visualstudio.com/>`__ (optional, a code
   editor with extensions for RDF formats like TTL and JSON-LD)

   -  Installation instructions are available
      `here <https://code.visualstudio.com/download>`__.

Quick Start
~~~~~~~~~~~

To quickly explore and make use of the ontology, first download the
pre-inferred version `pre-inferred
ontology <inferred_version/electrochemistry-inferred.ttl>`__. You can
then simply open the file in Protégé and explore its content or load the
ontology into python using EMMOntoPy.

In `EMMOntoPy <https://github.com/emmo-repo/EMMOntoPy>`__, you can
choose to import the ontology from your local downloaded copy or
directly from the web. Commands for both options are given below:

.. code:: python

   from ontopy import get_ontology

   # Loading from local repository
   electrochemistry = get_ontology('/path/to/domain-electrochemistry/electrochemistry-inferred.ttl').load(url_from_catalog=True)

   # Loading from web
   electrochemistry = get_ontology('https://raw.githubusercontent.com/emmo-repo/domain-electrochemistry/master/inferred_version/electrochemistry-inferred.ttl').load()

Contributing
------------

We welcome contributions from the community to enhance and expand the
ontology. If you have suggestions, improvements, or additional chemical
substance information to contribute, please refer to our `Contribution
Guidelines <CONTRIBUTING.md>`__.


Acknowledgements
~~~~~~~~~~~~~~~~

This project has received support from European Union research and
innovation programs, under grant agreement numbers:

-  957189 - `BIG-MAP <http://www.big-map.eu/>`__

License
-------

The Battery Interface Domain Ontology is released under the `Creative
Commons Attribution 4.0
International <https://creativecommons.org/licenses/by/4.0/legalcode>`__
license (CC BY 4.0).

.. |DOI| image:: https://zenodo.org/badge/570454941.svg
   :target: https://zenodo.org/badge/latestdoi/570454941
