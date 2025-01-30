Classes, Properties, and Triples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Like any language, an ontology consists of different types of words that define concepts and relationships. **Classes** function like *nouns*, representing people, places, things, and ideas. While classes typically act like common nouns, describing general categories of things (e.g., :code:`schema:Person` for people), **individuals** act more like proper nouns, identifying specific instances of those classes (e.g., :code:`ex:MarieCurie` as an instance of :code:`schema:Person`).

**Properties** function like *verbs*, linking classes and individuals by defining relationships or attributes. These relationships and attributes form **triples**, which are the basic building blocks of RDF-based ontologies. A triple consists of three components: a **subject**, a **predicate**, and an **object**, analogous to a simple sentence structure.

For example, we can define the class **CreativeWork** (:code:`schema:CreativeWork`) and a subclass **Book** (:code:`schema:Book`). To indicate that a book is a type of creative work, we use the property :code:`rdf:type`, which expresses an "is a" relationship. This can be written as:  

:code:`schema:Book rdf:type schema:CreativeWork .`

In natural language, this translates to:  
*"A book is a creative work."*

In this triple:
- **Subject**: :code:`schema:Book` (the entity being described)  
- **Predicate**: :code:`rdf:type` (the relationship)  
- **Object**: :code:`schema:CreativeWork` (the entity that the subject is linked to)  

Predicates are always **properties**, while subjects and objects can be **classes, individuals, or literal values**.

Properties
""""""""""""
Properties in ontologies define relationships between entities and can specify **constraints** on how they are used. Every property has:
- **Domain**: The class or set of classes that can appear as the subject.  
- **Range**: The class or set of classes that can appear as the object.  

For example, consider the property :code:`ex:hasAuthor`, where:
- **Domain**: :code:`schema:CreativeWork` (a creative work can have an author)  
- **Range**: :code:`schema:Person` (the author must be a person)  

A valid use of this property:  
:code:`ex:MyBook ex:hasAuthor ex:Alice .`  

An **invalid** use of this property:  
:code:`ex:Alice ex:hasAuthor ex:MyBook .`  

To allow statements in the reverse direction, ontologies sometimes define **inverse properties**. For instance, an inverse property of :code:`ex:hasAuthor` could be :code:`ex:isAuthorOf`, allowing:  

:code:`ex:Alice ex:isAuthorOf ex:MyBook .`

RDF Ontologies define different types of properties based on their function:

1. **Object Properties**: Connect two classes or individuals.  
   Example:  
   :code:`ex:MyBook ex:hasAuthor ex:Alice .`  
   *(This states that "MyBook" was written by Alice.)*  

2. **Annotation Properties**: Provide metadata such as labels, descriptions, or documentation.  
   Example:  
   :code:`schema:Book rdfs:comment "A written work, typically bound and published." .`  
   *(This provides a human-readable description of a book.)*  

3. **Data Properties**: Link a class or individual to literal values (e.g., numbers, strings, or dates).  
   Example:  
   :code:`ex:Alice schema:birthDate "1965-07-20"^^xsd:date .`  
   *(This states that Alice was born on July 20, 1965.)*  

Together, **classes, properties, and triples** form the foundation of an ontology, structuring knowledge in a way that is both human-readable and machine-processable.
