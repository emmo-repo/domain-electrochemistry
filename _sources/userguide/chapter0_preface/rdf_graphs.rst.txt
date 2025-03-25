Building RDF Graphs
~~~~~~~~~~~~~~~~~~~~

While individual triples are useful for making simple statements, the real power of RDF comes from connecting multiple triples together to form a graph. A graph allows us to represent complex relationships and build up rich descriptions of things we encounter every day.

What is a Graph?
"""""""""""""""
In RDF, a graph is simply a collection of connected triples. Each triple can be visualized as two nodes (the subject and object) connected by an arrow (the predicate). When multiple triples share common nodes, they form a network structure.

Let's build up a simple example about a book and its author:

.. tabs::

   .. tab:: Turtle
      
      .. code-block:: turtle

          # Define a book and its basic properties
          ex:TheHobbit rdf:type schema:Book ;
              schema:name "The Hobbit" ;
              schema:author ex:JRRTolkien ;
              schema:datePublished "1937-09-21"^^xsd:date .
          
          # Define information about the author
          ex:JRRTolkien rdf:type schema:Person ;
              schema:name "J.R.R. Tolkien" ;
              schema:birthDate "1892-01-03"^^xsd:date ;
              schema:jobTitle "Professor" .

   .. tab:: JSON-LD

      .. code-block:: json

          {
            "@context": {
              "schema": "http://schema.org/",
              "xsd": "http://www.w3.org/2001/XMLSchema#"
            },
            "@graph": [
              {
                "@type": "schema:Book",
                "@id": "ex:TheHobbit",
                "schema:name": "The Hobbit",
                "schema:author": {"@id": "ex:JRRTolkien"},
                "schema:datePublished": {
                  "@value": "1937-09-21",
                  "@type": "xsd:date"
                }
              },
              {
                "@type": "schema:Person",
                "@id": "ex:JRRTolkien",
                "schema:name": "J.R.R. Tolkien",
                "schema:birthDate": {
                  "@value": "1892-01-03",
                  "@type": "xsd:date"
                },
                "schema:jobTitle": "Professor"
              }
            ]
          }

This can be visualized as a graph where:
* Nodes represent resources (books, people, organizations)
* Arrows represent properties (relationships)
* Text in quotation marks represents literal values

.. figure:: images/book_graph.svg
   :align: center
   :alt: RDF graph of book and author

   A simple RDF graph describing a book and its author

Common Graph Patterns
""""""""""""""""""""
Certain patterns appear frequently in RDF graphs. Here are some of the most common:

Star Pattern
'''''''''''
A single subject connected to multiple objects, like spokes on a wheel. This pattern is common when describing various properties of an item:

.. tabs::

   .. tab:: Turtle

      .. code-block:: turtle

          ex:LocalCafe rdf:type schema:CafeOrCoffeeShop ;
              schema:name "Corner Cafe" ;
              schema:address "123 Main St" ;
              schema:openingHours "Mo-Fr 07:00-19:00" ;
              schema:servesCuisine "American" ;
              schema:priceRange "$$" .

   .. tab:: JSON-LD

      .. code-block:: json

          {
            "@context": "http://schema.org/",
            "@type": "CafeOrCoffeeShop",
            "@id": "ex:LocalCafe",
            "name": "Corner Cafe",
            "address": "123 Main St",
            "openingHours": "Mo-Fr 07:00-19:00",
            "servesCuisine": "American",
            "priceRange": "$$"
          }

Chain Pattern
''''''''''''
Resources connected in sequence, forming a path. This is useful for representing sequences of events or relationships:

.. tabs::

   .. tab:: Turtle

      .. code-block:: turtle

          ex:BlogPost rdf:type schema:BlogPosting ;
              schema:author ex:Alice ;
              schema:comment ex:Comment1 .
          
          ex:Comment1 rdf:type schema:Comment ;
              schema:author ex:Bob ;
              schema:comment ex:Reply1 .

   .. tab:: JSON-LD

      .. code-block:: json

          {
            "@context": "http://schema.org/",
            "@graph": [
              {
                "@type": "BlogPosting",
                "@id": "ex:BlogPost",
                "author": {"@id": "ex:Alice"},
                "comment": {"@id": "ex:Comment1"}
              },
              {
                "@type": "Comment",
                "@id": "ex:Comment1",
                "author": {"@id": "ex:Bob"},
                "comment": {"@id": "ex:Reply1"}
              }
            ]
          }

Tree Pattern
'''''''''''
Hierarchical relationships, often used for classification or organizational structures:

.. tabs::

   .. tab:: Turtle

      .. code-block:: turtle

          ex:University rdf:type schema:CollegeOrUniversity ;
              schema:name "Example University" ;
              schema:department ex:ComputerScience .
          
          ex:ComputerScience schema:department ex:AI_Lab ;
              schema:department ex:Networks_Lab .
          
          ex:AI_Lab schema:employee ex:Professor1 ;
              schema:employee ex:Researcher1 .

   .. tab:: JSON-LD

      .. code-block:: json

          {
            "@context": "http://schema.org/",
            "@graph": [
              {
                "@type": "CollegeOrUniversity",
                "@id": "ex:University",
                "name": "Example University",
                "department": {"@id": "ex:ComputerScience"}
              },
              {
                "@id": "ex:ComputerScience",
                "department": [
                  {"@id": "ex:AI_Lab"},
                  {"@id": "ex:Networks_Lab"}
                ]
              },
              {
                "@id": "ex:AI_Lab",
                "employee": [
                  {"@id": "ex:Professor1"},
                  {"@id": "ex:Researcher1"}
                ]
              }
            ]
          }

Connecting Graphs Together
""""""""""""""""""""""""
One of the most powerful features of RDF is the ability to combine graphs from different sources. Let's see how information about a movie might be combined from different databases:

Movie Database:

.. tabs::

   .. tab:: Turtle

      .. code-block:: turtle

          ex:Inception rdf:type schema:Movie ;
              schema:name "Inception" ;
              schema:director ex:ChristopherNolan ;
              schema:datePublished "2010-07-16"^^xsd:date .

   .. tab:: JSON-LD

      .. code-block:: json

          {
            "@context": "http://schema.org/",
            "@type": "Movie",
            "@id": "ex:Inception",
            "name": "Inception",
            "director": {"@id": "ex:ChristopherNolan"},
            "datePublished": "2010-07-16"
          }

Review Database:

.. tabs::

   .. tab:: Turtle

      .. code-block:: turtle

          ex:Inception schema:aggregateRating [
              rdf:type schema:AggregateRating ;
              schema:ratingValue "8.8" ;
              schema:ratingCount "2.2M"
          ] ;
          schema:review ex:Review1 .
          
          ex:Review1 rdf:type schema:Review ;
              schema:author ex:Critic1 ;
              schema:reviewRating [
                  schema:ratingValue "5" ;
                  schema:worstRating "1" ;
                  schema:bestRating "5"
              ] .

   .. tab:: JSON-LD

      .. code-block:: json

          {
            "@context": "http://schema.org/",
            "@id": "ex:Inception",
            "aggregateRating": {
              "@type": "AggregateRating",
              "ratingValue": "8.8",
              "ratingCount": "2.2M"
            },
            "review": {
              "@type": "Review",
              "@id": "ex:Review1",
              "author": {"@id": "ex:Critic1"},
              "reviewRating": {
                "ratingValue": "5",
                "worstRating": "1",
                "bestRating": "5"
              }
            }
          }

Because both sources use the same identifier (``ex:Inception``), we can automatically combine this information into a single, comprehensive description of the movie.

Common Modeling Patterns
"""""""""""""""""""""""
Here are some typical patterns you might encounter when building graphs:

Event Planning
'''''''''''''
Representing an event with multiple associated entities:

.. tabs::

   .. tab:: Turtle

      .. code-block:: turtle

          ex:Conference2024 rdf:type schema:Event ;
              schema:name "Tech Conference 2024" ;
              schema:startDate "2024-06-15T09:00:00"^^xsd:dateTime ;
              schema:location ex:ConferenceVenue ;
              schema:organizer ex:TechOrg ;
              schema:performer ex:Keynote1 .
          
          ex:ConferenceVenue rdf:type schema:Place ;
              schema:address "456 Convention Center Way" ;
              schema:maximumAttendeeCapacity "500" .
          
          ex:Workshop1 rdf:type schema:Event ;
              schema:superEvent ex:Conference2024 ;
              schema:name "AI Workshop" .

   .. tab:: JSON-LD

      .. code-block:: json

          {
            "@context": "http://schema.org/",
            "@graph": [
              {
                "@type": "Event",
                "@id": "ex:Conference2024",
                "name": "Tech Conference 2024",
                "startDate": "2024-06-15T09:00:00",
                "location": {"@id": "ex:ConferenceVenue"},
                "organizer": {"@id": "ex:TechOrg"},
                "performer": {"@id": "ex:Keynote1"}
              },
              {
                "@type": "Place",
                "@id": "ex:ConferenceVenue",
                "address": "456 Convention Center Way",
                "maximumAttendeeCapacity": "500"
              },
              {
                "@type": "Event",
                "@id": "ex:Workshop1",
                "superEvent": {"@id": "ex:Conference2024"},
                "name": "AI Workshop"
              }
            ]
          }

Best Practices for Building Graphs
""""""""""""""""""""""""""""""""
When building RDF graphs, consider these guidelines:

1. **Keep it Connected**
  Make sure all parts of your graph are connected - avoid isolated "islands" of information.

2. **Use Standard Patterns**
  Reuse common patterns when possible. This makes your data more predictable and easier to query.

3. **Balance Detail and Complexity**
  Include enough detail to be useful, but don't add relationships that won't be used.

4. **Think About Queries**
  Consider how the graph will be queried. Structure it to make common queries straightforward.

5. **Maintain Consistency**
  Use consistent patterns for similar types of information.

Summary
"""""""
RDF graphs allow us to represent complex, interconnected information in a way that's both human-readable and machine-processable. By understanding common patterns and structures, we can:

* Build meaningful connections between different pieces of information
* Combine data from multiple sources
* Create flexible, extensible data models
* Represent real-world relationships clearly

Remember these key points when building your own graphs:

1. Start simple and build up complexity gradually
2. Use standard vocabularies like schema.org where possible
3. Keep your graph connected - avoid isolated pieces of information
4. Choose the right patterns for your use case
5. Consider how your data will be queried and used

The next section will explore how to query these graphs using SPARQL, allowing us to extract specific information from our connected data.