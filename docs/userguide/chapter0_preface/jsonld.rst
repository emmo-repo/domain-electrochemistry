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

Example: Electrochemical Cell in JSON-LD
----------------------------------------

```json
{
  "@context": {
    "@vocab": "https://w3id.org/emmo/domain/electrochemistry#",
    "hasNegativeElectrode": "https://w3id.org/emmo/domain/electrochemistry#hasNegativeElectrode",
    "hasPositiveElectrode": "https://w3id.org/emmo/domain/electrochemistry#hasPositiveElectrode",
    "hasElectrolyte": "https://w3id.org/emmo/domain/electrochemistry#hasElectrolyte"
  },
  "@type": "ElectrochemicalCell",
  "hasNegativeElectrode": {
    "@type": "ZincElectrode"
  },
  "hasPositiveElectrode": {
    "@type": "ManganeseDioxideElectrode"
  },
  "hasElectrolyte": {
    "@type": "AlkalineElectrolyte"
  }
}
```

.. example:: Example: A Simple Description of a Person

   Below is an example of JSON-LD code for describing a person:

   .. code-block:: json

      {
          "@context": "https://schema.org",
          "@type": "Person",
          "name": "Marie Curie",
          "birthDate": "1867-11-07",
          "spouse": {
              "@type": "Person",
              "name": "Pierre Curie"
          }
      }

Learn More
----------

To dive deeper into JSON-LD, explore the following resources:

- [JSON-LD Official Website](https://json-ld.org/)
- [JSON-LD Playground](https://json-ld.org/playground/)
- [W3C JSON-LD Specification](https://www.w3.org/TR/json-ld/)
