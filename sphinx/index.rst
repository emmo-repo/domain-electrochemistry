
.. toctree::
   :includehidden:
   :hidden:

   About <about>
   self
   electrochemistry
   Contribute <contribute>
   

Electrochemistry Domain Ontology
================================

.. raw:: html

   <!-- [![CI tests](https://github.com/emmo-repo/domain-electrochemistry/workflows/CI%20tests/badge.svg)](https://github.com/emmo-repo/domain-electrochemistry/actions/) -->
   
The Electrochemistry Domain Ontology is a specialized domain within the
Elementary Multiperspective Materials Ontology
`(EMMO) <https://github.com/emmo-repo/EMMO>`__, that encompasses
essential terms and relationships for electrochemical systems,
materials, methods, and data. Its primary objective is to enable the
creation of linked and FAIR (Findable, Accessible, Interoperable, and
Reusable) data, thereby fostering advancements in research and
innovation within the realm of electrochemistry. This ontology serves as
a foundational resource for harmonizing electrochemical knowledge
representation, enhancing data interoperability, and accelerating
progress in electrochemical research and development.

A reference documentation is available in
`html <https://emmo-repo.github.io/domain-electrochemistry/index.html>`__
and
`pdf <https://emmo-repo.github.io/domain-electrochemistry/electrochemistry.pdf>`__
formats.

Persistent Identifiers
~~~~~~~~~~~~~~~~~~~~~~

This ontology assigns persistent machine-readable identifiers to
concepts from the electrochemistry domain. These identifiers facilitate
data exchange and interoperability among various tools and systems. It
includes annotations to other sources of information including
`DBPedia <https://www.dbpedia.org/>`__ and
`Wikidata <https://www.wikidata.org/>`__.

Standardized Nomenclature
~~~~~~~~~~~~~~~~~~~~~~~~~

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

.. raw:: html
         
   <div style="position: relative; padding-top: 56.25%; height: 0;">
   <iframe src="https://json-ld.org/playground/" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" frameborder="0" allowfullscreen></iframe>
   </div>
   
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

   
