Metadata
========

What we will describe with semantic annotation is *metadata*, i.e. data about the data. It is the list of attributes describing a subject, which in our case will be a data file. Metadata is instrumental to help humans and computers understand files, i.e. to explicitly describe its source, contents, creator, purpose, maintainance, etc. There is a large list of metadata attributes to describe files, many ways to `categorize <https://en.wikipedia.org/wiki/Metadata#Types>`_ such attributes, several `standards <https://en.wikipedia.org/wiki/Metadata_standard#Available_metadata_standards>`_  defining terms to name attributes, and `guidelines <https://data.research.cornell.edu/data-management/storing-and-managing/metadata/>`_ with rules to describe data.

Metadata standards
~~~~~~~~~~~~~~~~~~

To the best of our knowledge, there is no metadata standard tailored to electrochemical data. Instead, our guideline draws inspiration from several standards and guidelines we consider authoritative, widely used, rigorously managed and applicable to us, which we follow in the following order of importance: 

* `FAIR Data principles <https://www.go-fair.org/fair-principles/>`_. A set of guiding principles to make data machine-actionable, i.e. findable, accessible, interoperable and reusable by computational systems. The principles are promoted by the GO FAIR Initiative.
* `Dublin Core (DC) <https://www.dublincore.org/specifications/dublin-core/dcmi-terms/>`_. Specification for metadata terms for digital resources, including datasets. It is widely used and regularly maintained by an independent organization, the Dublin Core Metadata Initiative.
* `Data Catalog Vocabulary (DCAT) <https://www.w3.org/TR/vocab-dcat-3/>`_. A vocabulary of metadata terms to describe datasets and data catalogs (i.e. repositories) in the web. It is developed and maintained by the World Wide Web Consortium (W3C).
* `Schema.org <https://schema.org/>`_. Set of schemas to describe web pages with a common set of structured terms. It is designed to improve the discoverability of web pages by search engines, and it is maintained by a community of developers and organizations, including Google, Microsoft, Yahoo and Yandex.

Following this order means we first aim to ensure compliance with FAIR principles. Then, we primarily use Dublin Core Metadata terms as much as possible to describe datasets. If terms are not avaiable in DC, we draw from terms in DCAT. Finally, we use Schema.org terms if none of the other vocabularies support an attribute. This order is not arbitrary: DC is the foundational metadata vocabulary from which DCAT inherits and extends on. Moreover, many terms in Schema.org can be uniquely mapped to terms in DC.


Metadata encoding
~~~~~~~~~~~~~~~~~~

Metadata is arranged as key-value pairs; each key describes a metadata attribute named according to a controlled vocabulary, and has a value assigned to it. It is therefore natural to encode metadata in JSON format. 

In the following sections we will describe metadata attributes common to all file types, and then metadata properties particular to each file type, along with JSON examples for each type.
