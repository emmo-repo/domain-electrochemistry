Introduction to Linked Data
===========================

Linked Data is a method of structuring and connecting data so it can be easily understood and used by both humans and machines. It is the foundation of the **Semantic Web**, where data is no longer siloed but linked together, creating a web of meaningful information.

What is Linked Data?
--------------------

Linked Data is built on four simple principles:

1. **Use Uniform Resource Identifiers (URIs)** to uniquely identify things.
2. **Make URIs resolvable** (usually as web addresses) so people and systems can look them up.
3. **Provide useful information** about things in standard formats, like JSON-LD, Turtle, or RDF.
4. **Link to other URIs** to enable users to discover more related information.

By following these principles, Linked Data connects datasets in a meaningful way, enabling better data sharing, integration, and reuse.

Everyday Analogy
------------------------
Think of Linked Data as a well-organized library where:
- Every book has a unique identifier (like a catalog number).
- Each identifier points to detailed information about the book (title, author, etc.).
- Books are cross-referenced, so you can find related ones easily.

Why Linked Data Matters
------------------------

- **Interoperability**: Data from different sources can work together seamlessly.
- **Discoverability**: Links make it easy to find related data across the web.
- **Reusability**: Structured and linked data ensures it can be reused in different contexts.
- **Automation**: Machines can understand and process linked data to power intelligent systems.

The 5 Stars of Linked Data
---------------------------

Sir Tim Berners-Lee, the inventor of the Web, introduced a 5-star system to encourage better data practices:

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

How Does Linked Data Work?
--------------------------

Linked Data is powered by standard technologies and practices:

- **RDF (Resource Description Framework)**: A framework for describing resources and their relationships.
- **SPARQL**: A query language to retrieve and manipulate linked data.
- **Ontologies**: Define vocabularies and schemas (like EMMO) to provide semantic meaning to data.
- **Serialization Formats**: JSON-LD, Turtle, and RDF/XML are commonly used formats to represent linked data.

Getting Started with Linked Data
--------------------------------

1. **Start Small**: Begin by structuring your data using a simple format like JSON-LD.
2. **Adopt Standards**: Use well-defined vocabularies and ontologies (e.g., Schema.org, EMMO).
3. **Link to External Data**: Connect your dataset to relevant URIs in other datasets.
4. **Publish Your Data**: Make it accessible on the web and document its structure.

Introduction to JSON-LD
=======================

JSON-LD (JavaScript Object Notation for Linked Data) is a lightweight data interchange format designed to integrate linked data principles with the simplicity of JSON. It is widely used to describe and share structured data on the web in a machine-readable format, making it ideal for semantic web applications.

Why JSON-LD?
------------

JSON-LD provides a way to:

- Link data across different systems and domains using globally unique identifiers (IRIs).
- Maintain compatibility with standard JSON, making it accessible to developers already familiar with JSON.
- Enhance data interoperability and reusability by embedding semantics directly in the data.
- Enable easy integration with linked data tools and ontologies like EMMO.

Key Features
------------

1. **Context**:
   The `@context` keyword defines the mapping between JSON terms and their corresponding IRIs, allowing data to be unambiguously understood across different systems.

   Example:
   ```json
   {
     "@context": {
       "name": "http://schema.org/name",
       "age": "http://schema.org/age"
     },
     "name": "Alice",
     "age": 30
   }
   ```

2. **Identifiers**:
   JSON-LD uses the `@id` keyword to define unique identifiers for objects, enabling linking between entities.

   Example:
   ```json
   {
     "@id": "http://example.org/person/alice",
     "name": "Alice"
   }
   ```

3. **Types**:
   The `@type` keyword specifies the type of an object, often linked to an ontology class.

   Example:
   ```json
   {
     "@type": "http://schema.org/Person",
     "name": "Alice"
   }
   ```

4. **Relationships**:
   JSON-LD uses properties to define relationships between entities.

   Example:
   ```json
   {
     "@context": {
       "friend": "http://schema.org/knows",
       "Person": "http://schema.org/Person"
     },
     "@type": "Person",
     "name": "Alice",
     "friend": {
       "@type": "Person",
       "name": "Bob"
     }
   }
   ```

JSON-LD in Practice
------------------------

Imagine you have a dataset about books:

```json
{
  "@context": "https://schema.org",
  "@type": "Book",
  "name": "The Great Gatsby",
  "author": {
    "@type": "Person",
    "name": "F. Scott Fitzgerald"
  },
  "genre": "Novel"
}
```

This structured and linked format allows:
- Machines to understand what "The Great Gatsby" is.
- Linking to other datasets about authors, genres, or similar books.
- Easy integration with external applications like recommendation engines or library systems.

Getting Started with JSON-LD
----------------------------

1. **Define a Context**:
   The context maps your terms to IRIs. Use existing vocabularies like Schema.org or create your own.

2. **Model Your Data**:
   Identify the entities, properties, and relationships in your domain.

3. **Use Ontologies**:
   Integrate ontologies like EMMO to provide semantic meaning to your data.

4. **Validate Your Data**:
   Use tools like the [JSON-LD Playground](https://json-ld.org/playground/) to test and validate your JSON-LD.

Advantages of JSON-LD
---------------------

- **Human-Readable and Developer-Friendly**:
  JSON-LD retains the simplicity of JSON while embedding powerful linked data capabilities.

- **Extensible**:
  JSON-LD can be easily extended with new terms and vocabularies.

- **Integration with the Web**:
  JSON-LD is supported by major search engines and tools for rich semantic annotations.

Resources to Learn More
------------------------

- [Linked Data Principles](https://www.w3.org/DesignIssues/LinkedData.html)
- [SPARQL Query Language](https://www.w3.org/TR/sparql11-query/)
- [Open Data Handbook](https://opendatahandbook.org/)
- [JSON-LD Official Website](https://json-ld.org/)
- [W3C JSON-LD Specification](https://www.w3.org/TR/json-ld/)

By adopting Linked Data principles, you can create data that is discoverable, meaningful, and reusable, contributing to a more connected and intelligent web.
