Identifiers
===========

If an ontology is a language, **identifiers** are the words. An identifier is a stable string that names a resource so anyone (and any tool) can refer to it unambiguously.

Why they matter
---------------
Identifiers (URLs in this case) help disambiguate terms and point to more detailed information about specific concepts.

.. admonition:: Thought Experiment: Who says the Taj Mahal is in India?

   **You**: "I'm in New York City, and I can't wait to see Taj Mahal later!"  
   **Friend**: "New York City? Isn't the Taj Mahal in India?"  
   **You**: "No, not that Taj Mahal...the musician! Here's a link... `https://en.wikipedia.org/wiki/Taj_Mahal_(musician)`"

- Disambiguation (the musician *Taj Mahal* vs the monument).
- Linking (two datasets using the same identifier can be merged).
- Persistence (references keep working when data moves).

Types of Identifiers
--------------------

**Uniform Resource Identifier (URI)**
A URI is a globally unique identifier used to reference a resource. It often takes the form of a web address that can be resolved (like `https://example.com/ontology#Person`), but can also be non-resolvable (like `urn:isbn:0451450523`).

**Internationalized Resource Identifier (IRI)**
IRIs extend URIs to include Unicode characters (like Chinese, Japanese, or Cyrillic), making them more inclusive for international use.

**Blank Nodes**
Blank nodes are unnamed resources without persistent identifiers. They're useful when an entity needs to exist in the data structure but doesn't require a global identifier.

Anatomy of an identifier
------------------------
Identifiers often look like: `<namespace><delimiter><term_name>`

- **Namespace**: Groups related identifiers (e.g., `https://w3id.org/emmo`)
- **Delimiter**: Either `/` or `#`, indicating hierarchy or self-contained terms
- **Term name**: Either human-readable (like `Person`) or a UUID for guaranteed uniqueness

Prefixes can be used to shorten long identifiers. For example:
```
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
rdf:type  # Instead of http://www.w3.org/1999/02/22-rdf-syntax-ns#type
```

Persistent URLs (PURLs)
-----------------------
To keep links stable over time, many communities use PURLs (e.g. **w3id.org**) to redirect to the current hosting location. This safeguards identifiers as your sites and repositories evolve.