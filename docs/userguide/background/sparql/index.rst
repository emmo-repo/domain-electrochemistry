SPARQL: Querying RDF Graphs
===========================

Once data is represented as an RDF graph, the next step is learning how to retrieve information from it. The **SPARQL Query Language** (SPARQL = SPARQL Protocol and RDF Query Language) is the W3C standard for querying and updating RDF data.

SPARQL plays the same role for RDF as SQL does for relational databases: it lets you express questions about data, combine results from multiple sources, and transform graphs into tables or new graphs.

Core idea
---------

SPARQL matches **patterns of triples** in the RDF graph. If the pattern fits, it returns the variables that make the pattern true.

Example — Find all books and their authors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sparql

   PREFIX schema: <https://schema.org/>
   PREFIX ex:     <https://example.org/>

   SELECT ?book ?authorName
   WHERE {
     ?book a schema:Book ;
           schema:author ?author .
     ?author schema:name ?authorName .
   }

This query finds all things that are `schema:Book`, follows the `schema:author` property, and returns each author’s name.

SPARQL results look like tables, but they’re built from the underlying graph.

Common query forms
------------------

- **SELECT** – return a table of results  
- **CONSTRUCT** – build a new RDF graph  
- **ASK** – true/false test for whether a pattern exists  
- **DESCRIBE** – return all known triples about a resource  

Example — Build a subgraph (CONSTRUCT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sparql

   CONSTRUCT {
     ?author schema:name ?name .
   }
   WHERE {
     ?book a schema:Book ;
           schema:author ?author .
     ?author schema:name ?name .
   }

This creates a new graph containing only authors and their names.

Filters and conditions
----------------------

SPARQL supports comparisons, regular expressions, and logical filters.

.. code-block:: sparql

   SELECT ?book ?year
   WHERE {
     ?book a schema:Book ;
           schema:datePublished ?year .
     FILTER (?year > "1950"^^xsd:gYear)
   }

Federated and linked queries
----------------------------

SPARQL can query across datasets and endpoints using the same vocabulary. For example, you can combine data about chemical compounds from Wikidata with material properties from your own RDF store — as long as both use consistent identifiers.

Tips for beginners
------------------

- Always **declare prefixes** at the top.  
- Keep queries simple at first; RDF graphs can be very rich.  
- Use online tools such as the
  `Yasgui SPARQL editor <https://yasgui.triply.cc/>`_ to experiment.  
- Remember: RDF data is *schema-flexible* — not all resources have all
  properties.

Summary
-------

SPARQL turns RDF graphs into an interactive, queryable knowledge base. It lets you explore, filter, and combine linked data — turning structure into insight.

Next steps
-----------

- Learn more at the `W3C SPARQL 1.1 specification <https://www.w3.org/TR/sparql11-query/>`_.  
- Try the `Wikidata Query Service <https://query.wikidata.org/>`_ for live examples.  
