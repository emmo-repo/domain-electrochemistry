RDF Formats
~~~~~~~~~~~~

RDF supports multiple serialization formats, each suited for different use cases such as human readability, web compatibility, or efficient data storage. Understanding these formats is key to selecting the best representation for your linked data.

Turtle (Terse RDF Triple Language)
""""""""""""""""""""""""""""""""

**Turtle (`.ttl`)** is a human-readable format that provides a compact way to write RDF triples using prefixes.

**Example in Turtle:**
.. code-block:: turtle

   @prefix schema: <https://schema.org/> .
   @prefix ex: <https://example.org/> .

   ex:TheHobbit a schema:Book ;
       schema:author ex:Tolkien ;
       schema:genre "Fantasy" ;
       schema:publicationYear "1937"^^xsd:gYear .

Turtle is widely used in ontology development and linked data applications due to its readability.

JSON-LD (JSON for Linked Data)
""""""""""""""""""""""""""""""""

**JSON-LD (`.jsonld`)** is designed for web applications, integrating RDF data with existing JSON-based APIs.

**Example in JSON-LD:**
.. code-block:: json

   {
     "@context": "https://schema.org/",
     "@type": "Book",
     "@id": "https://example.org/TheHobbit",
     "author": { "@id": "https://example.org/Tolkien" },
     "genre": "Fantasy",
     "publicationYear": "1937"
   }

JSON-LD is ideal for **structured web data and APIs**, making it easy to integrate linked data into web applications.

RDF/XML
""""""""""""""""""""""""""""""""

**RDF/XML (`.rdf`)** is the original RDF format, using an XML structure for representing triples.

**Example in RDF/XML:**
.. code-block:: xml

   <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
            xmlns:schema="https://schema.org/"
            xmlns:ex="https://example.org/">
   
     <rdf:Description rdf:about="https://example.org/TheHobbit">
       <rdf:type rdf:resource="https://schema.org/Book"/>
       <schema:author rdf:resource="https://example.org/Tolkien"/>
       <schema:genre>Fantasy</schema:genre>
       <schema:publicationYear rdf:datatype="http://www.w3.org/2001/XMLSchema#gYear">1937</schema:publicationYear>
     </rdf:Description>

   </rdf:RDF>

RDF/XML is less human-readable but remains widely used for interoperability with XML-based systems.

N-Triples and N-Quads
""""""""""""""""""""""""""""""""

**N-Triples (`.nt`)** and **N-Quads (`.nq`)** are line-based formats used for **efficient data storage and processing**.

**Example in N-Triples:**
.. code-block:: turtle

   <https://example.org/TheHobbit> <https://schema.org/author> <https://example.org/Tolkien> .
   <https://example.org/TheHobbit> <https://schema.org/genre> "Fantasy" .

N-Quads extends N-Triples by adding a **graph name**, making it suitable for **named graphs and RDF databases**.

Choosing an RDF Format
""""""""""""""""""""""""""""""""

Each RDF format serves different needs:

- **Turtle**: Best for human-readable RDF data.
- **JSON-LD**: Ideal for web applications and structured APIs.
- **RDF/XML**: Useful for XML-based interoperability.
- **N-Triples/N-Quads**: Optimized for **large-scale data storage**.

Selecting the right format depends on whether **readability, system compatibility, or data scalability** is the priority.
