Classes, Properties, and Triples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Like any language, an ontology has different types of "words" that we use to express meaning. Let's break these down:

Classes and Individuals
"""""""""""""""""""""""
**Classes** are like categories or types of things. Think of them as nouns in a sentence:

* A Person (``schema:Person``)
* A Book (``schema:Book``)
* A Material (``emmo:Material``)

**Individuals** are specific instances of these classes. If "Person" is the class, then "Marie Curie" would be an individual belonging to that class. We express this relationship like this:

.. code-block:: turtle

    ex:MarieCurie rdf:type schema:Person .

Properties
""""""""""
**Properties** are like verbs - they describe relationships between things or their characteristics. For example:

* ``hasAuthor`` (connects a book to its author)  
* ``birthDate`` (specifies when someone was born)  

Every property has rules about what it can connect:

* The **domain** specifies what can appear at the start of the relationship  
* The **range** specifies what can appear at the end  

For example, ``hasAuthor`` might have:

* Domain: Creative works (only creative works can have authors)
* Range: Persons (only persons can be authors)

Building Statements with Triples
""""""""""""""""""""""""""""""""
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

Types of Properties
"""""""""""""""""
Properties come in three main flavors:

1. **Object Properties** connect things to other things:

   .. code-block:: turtle

       ex:MyBook ex:hasAuthor ex:Alice .
       # Connects one resource to another resource

2. **Data Properties** connect things to values:

   .. code-block:: turtle

       ex:Alice schema:birthDate "1965-07-20"^^xsd:date .
       # Connects a resource to a specific value

3. **Annotation Properties** add human-readable information:

   .. code-block:: turtle

       schema:Book rdfs:comment "A written work, typically bound and published." .
       # Adds documentation or metadata

Together, classes, properties, and triples form the foundation of an ontology, structuring knowledge in a way that is both human-readable and machine-processable.