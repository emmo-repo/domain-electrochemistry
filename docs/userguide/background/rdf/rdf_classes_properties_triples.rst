Classes, Properties, and Triples
================================

RDF statements are build from **classes**, **individuals**, and **properties**.

Classes and Individuals
"""""""""""""""""""""""
A **class** is a category of a thing. Think of them as nouns in a sentence, like "a person" (``schema:Person``) or "a book" (``schema:Book``).

An **individual** is a specific instance of a class. If "Person" is the class, then "Marie Curie" would be an individual belonging to that class. We can express this relationship as an RDF triple like this:

.. code-block:: turtle

    @prefix ex: <https://example.org/> .
    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    @prefix schema: <https://schema.org/> .

    ex:MarieCurie rdf:type schema:Person .

Properties
----------

A **Property** connects resources or attaches values.

* ``hasAuthor`` (connects a book to its author)  
* ``birthDate`` (specifies when someone was born)  

RDF properties come in three main flavors:

1. **Object properties** connect things to other things:

   .. code-block:: turtle

       ex:MyBook ex:hasAuthor ex:Alice .
       # Connects one resource to another resource

2. **Data properties** connect things to values:

   .. code-block:: turtle

       ex:Alice schema:birthDate "1965-07-20"^^xsd:date .
       # Connects a resource to a specific value

3. **Annotation properties** add human-readable information:

   .. code-block:: turtle

       schema:Book rdfs:comment "A written work, typically bound and published." .
       # Adds documentation or metadata

Every property has rules about what it can connect:

* The **domain** specifies what can appear at the start of the relationship  
* The **range** specifies what can appear at the end  

For example, ``hasAuthor`` might have:

* Domain: Creative works (only creative works can have authors)
* Range: Persons (only persons can be authors)

Triples: the basic statement
----------------------------
In RDF, we combine classes, individuals, and properties to make statements called **triples**. Each triple has three parts:

* Subject (what we're talking about)  
* Predicate (the property or relationship)  
* Object (what we're saying about the subject)  

For example:

.. code-block:: turtle

    # A class relationship
    schema:Book rdf:type schema:CreativeWork .
    # Means: "A Book is a type of Creative Work"

    # An individual relationship
    ex:MyBook ex:hasAuthor ex:Alice .
    # Means: "MyBook was written by Alice"

Together, classes, properties, and triples form the foundation of an ontology, structuring knowledge in a way that is both human-readable and machine-processable.