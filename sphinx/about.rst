About
=====

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
