Introduction to Linked Data
===========================

Data often exists in silos, scattered across different formats and systems. Linked data breaks down these walls by creating meaningful connections between pieces of information, making it easier to share, combine, and understand data in a unified way. It’s like building a world wide web for your data, where every table, property, and source of information is hyperlinked together. 

Put simply, linked data is a way to structure and connect data, so that it can be better understood and utilized. The linked data framework is designed to be understood by both humans and machines. It represents data as a network graph of interconnected data points, each described using a shared vocabulary and unique identifiers. By linking pieces of information, linked data facilitates interoperability between systems and helps users extract meaningful insights across different datasets.

Background
----------

Linked data is a key component of the Semantic Web, an idea introduced by Sir Tim Berners-Lee in the early 2000s. The goal of the Semantic Web is to make the web smarter by allowing machines to not only display information but also understand and process it. This would improve the connection between data, making information more useful and accessible.

At the core of linked data is the **Resource Description Framework (RDF)**, which organizes information as **triples**. A triple is a three-part statement, comprised of a subject, a predicate, and an object. Triples are like node-edge-node structures, that can be combined to create a network graph of inforamtion. For example, we can create conceptual triples like: 

- **subject:** "MarieCurie"
- **predicate:** "birthDate"
- **object:** "1867-11-07"

and

- **subject:** "MarieCurie"
- **predicate:** "spouse"
- **object:** "PierreCurie"

When combined, these triples form a graph of interconnected data, enabling the definition of relationships that make it easier to explore related information.

Today, linked data is foundational to modern search engines and knowledge graphs. For instance, Google uses linked data in the `Google Knowledge Graph <https://blog.google/products/search/introducing-knowledge-graph-things-not/>`__, which powers rich search results by connecting facts about people, places, and things from various sources. `Wikidata <https://www.wikidata.org/>`__, a structured data hub for Wikipedia, relies heavily on linked data principles to link information about millions of topics. These technologies enable search engines to deliver more relevant and precise results by understanding relationships between data, making the web more interconnected and useful for both people and machines.

Key Concepts in Linked Data
---------------------------

The `**Resource Description Framework (RDF)** <https://www.w3.org/RDF/>`__is the foundational model for representing information in linked data. It structures data as a set of triples, each consisting of a subject, predicate, and object. These triples are used to create graphs where each node (subject or object) is connected by edges (predicates). RDF graphs can be stored in a variety of supported formats, including **JSON-LD** and **Turtle**. Data stored in RDF graphs can be semantically queried using the query language `**SPARQL** <https://www.w3.org/TR/sparql11-query/>`__.

In linked data, every resource (such as a battery, material, or test result) is identified by a `**Uniform Resource Identifier (URI)** <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__. URIs ensure that each entity is globally unique and can be referenced unambiguously across datasets. URIs are limited to using US-ASCII characters. 
A more expansive identifier standard called `**Internationalized Resource Identifier (IRI)** <https://en.wikipedia.org/wiki/Internationalized_Resource_Identifier>`__ is an extension of the URI standard that can contain most characters from the Universal Character Set. 

An **ontology** is a formal vocabulary that defines the relationships and concepts within a domain, providing a shared language for describing data. Ontologies in linked data use RDF to standardize the meanings of terms, ensuring that the same concept is understood consistently across different datasets. 

Why Linked Data Matters
------------------------

- **Interoperability**: Data from different sources can work together seamlessly.
- **Discoverability**: Links make it easy to find related data across the web.
- **Reusability**: Structured and linked data ensures it can be reused in different contexts.
- **Automation**: Machines can understand and process linked data to power intelligent systems.

The 5 Stars of Linked Data
---------------------------

Sir Tim Berners-Lee introduced a `5-star system <https://www.w3.org/2011/gld/wiki/5_Star_Linked_Data>`__ to encourage better data practices:

1. ⭐ **Available on the Web (in any format)**: Data is accessible online.
   - Example: A PDF file of a dataset.

2. ⭐⭐ **Available in a structured format**: Data is machine-readable (e.g., Excel, CSV).
   - Example: An Excel file instead of a PDF.

3. ⭐⭐⭐ **Uses non-proprietary formats**: Data is in open formats (e.g., CSV instead of Excel).
   - Example: A CSV file instead of a proprietary Excel format.

4. ⭐⭐⭐⭐ **Uses URIs to identify things**: Data uses URIs to link concepts and entities.
   - Example: A dataset about books where each book has a unique URI.

5. ⭐⭐⭐⭐⭐ **Linked to other data**: Data is interlinked with other datasets, creating a web of data.
   - Example: A dataset about books that links to author profiles, publishers, and related genres.

The goal is to encourage datasets to move toward 5-star Linked Data for maximum accessibility, interoperability, and usefulness.

.. tip:: Getting Started with Linked Data

   1. **Start Small**: Begin by structuring your data using a simple format like JSON-LD.
   2. **Adopt Standards**: Use well-defined vocabularies and ontologies (e.g., Schema.org, EMMO).
   3. **Link to External Data**: Connect your dataset to relevant URIs in other datasets.
   4. **Publish Your Data**: Make it accessible on the web and document its structure.

Linked Data Resources
---------------------

Linked data resources are the vocabularies that make linked data possible. These vocabularies define the structure and meaning of data, allowing different datasets to connect and communicate in a standardized way. There are many vocabularies available, each suited to specific needs or domains, but all of them work together to support interoperability and meaningful data exchange. Below are some of the key linked data resources that are widely used to organize and describe information across various fields.

RDF Schema (RDFS)
~~~~~~~~~~~~~~~~~

RDF Schema (RDFS) is a framework that extends RDF (Resource Description Framework) by providing a basic vocabulary to describe relationships between resources. RDFS introduces concepts like classes and properties to allow more expressive descriptions of data. It also supports hierarchical structures through subclasses and sub properties, which allow users to define more specific relationships under broader categories. For example, you can define that a "Student" is a subclass of "Person," or that "birthPlace" is a sub property of "location."

RDFS helps establish the foundational structure of linked data, allowing different resources to be described in a standardized and meaningful way, making it a key building block for ontologies.

Dublin Core (DC) Terms
~~~~~~~~~~~~~~~~~~~~~~

Dublin Core is a set of standardized metadata terms used for describing digital resources, such as titles, creators, and subjects. These terms provide a flexible, widely adopted vocabulary for describing web content in a structured way.

Schema.org
~~~~~~~~~~~

Schema.org is a collaborative effort supported by major search engines like Google, Bing, and Yahoo to provide a shared vocabulary for structuring data on the web. Schema.org defines types and properties to describe common entities, such as people, places, and events, allowing websites and data providers to structure their information in a way that search engines and applications can easily interpret.

For example, the Person type in Schema.org can have properties like name, birthDate, and jobTitle, while the Event type includes properties like startDate and location. Schema.org’s simplicity and broad adoption make it an ideal starting point for building interoperable linked data on the web.

CSV on the Web (CSVW)
~~~~~~~~~~~~~~~~~~~~~~

CSV on the Web (CSVW) is a standard that defines how to represent metadata about CSV files to make them more accessible as linked data. CSVW helps transform tabular data (like CSV files) into structured, machine-readable formats by describing the columns, datatypes, and relationships in a CSV file. With CSVW, you can:

- Define the structure of a CSV file (e.g., what each column represents).
- Validate the data (e.g., ensure columns contain the correct datatypes).
- Link the CSV data to external resources (e.g., linking values to related entities via URIs).

By using CSVW, even simple CSV files can be turned into linked data that is interoperable across the web, bridging the gap between traditional tabular data and more advanced linked data formats.

Data Catalogue Vocabulary (DCAT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DCAT (Data Catalogue Vocabulary) is a W3C standard used for describing datasets and data catalogues, making it easier to share, discover, and integrate data across different platforms. DCAT provides a vocabulary for publishing metadata about datasets, including:

- Dataset: Describes a collection of data, such as a research dataset or a government dataset
- Catalogue: Describes a collection of datasets, such as a data repository or a catalogue of open data.
- Distribution: Describes how the dataset is made available (e.g., as a downloadable file or API).

DCAT plays a crucial role in the open data movement, helping governments, organizations, and researchers publish their datasets in a standardized way, making them easier to find and reuse. By linking datasets to their descriptions, DCAT enables data cataloguing systems to interoperate, allowing users to search for and retrieve datasets more efficiently.


- [Linked Data Principles](https://www.w3.org/DesignIssues/LinkedData.html)
- [SPARQL Query Language](https://www.w3.org/TR/sparql11-query/)
- [Open Data Handbook](https://opendatahandbook.org/)
