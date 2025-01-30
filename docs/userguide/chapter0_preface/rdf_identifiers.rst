Identifiers
~~~~~~~~~~~
If an ontology is a language, then its identifiers are like the words. Identifiers are unique, persistent strings used to identify concepts and resources. They enable both humans and machines to uniquely reference and access information, ensuring clarity and interoperability across datasets.

.. admonition:: Thought Experiment: Who says the Taj Mahal is in India?

   **You**: "I'm in New York City, and I can't wait to see Taj Mahal later!"  
   **Friend**: "New York City? You've got a long way to go...the Taj Mahal is in India!"  
   **You**: "No, not that Taj Mahal...the musician! Here's a link... `https://en.wikipedia.org/wiki/Taj_Mahal_(musician)`"

   This example shows how identifiers (URLs in this case) help disambiguate terms and point to more detailed information about specific concepts.

Types of Identifiers
^^^^^^^^^^^^^^^^^^^^

Uniform Resource Identifier (URI)
"""""""""""""""""""""""""""""""""
A URI is a globally unique identifier used to reference a resource. It often takes the form of a web address that can be resolved (like `https://example.com/ontology#Person`), but can also be non-resolvable (like `urn:isbn:0451450523`).

Internationalized Resource Identifier (IRI)
"""""""""""""""""""""""""""""""""""""""""""
IRIs extend URIs to include Unicode characters (like Chinese, Japanese, or Cyrillic), making them more inclusive for international use.

Blank Nodes
"""""""""""
Blank nodes are unnamed resources without persistent identifiers. They're useful when an entity needs to exist in the data structure but doesn't require a global identifier.

Structure of Identifiers
^^^^^^^^^^^^^^^^^^^^^^^^
Identifiers have three parts: `<namespace><delimiter><term_name>`

- **Namespace**: Groups related identifiers (e.g., `https://w3id.org/emmo`)
- **Delimiter**: Either `/` or `#`, indicating hierarchy or self-contained terms
- **Term name**: Either human-readable (like `Person`) or a UUID for guaranteed uniqueness

To simplify long identifiers, prefixes are used. For example:
```
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
rdf:type  # Instead of the full URI
```

Permanent URLs (PURLs)
""""""""""""""""""""""
PURLs provide persistent identifiers that can redirect to different locations, ensuring stability even if hosting changes. EMMO uses the w3id.org service for this purpose.