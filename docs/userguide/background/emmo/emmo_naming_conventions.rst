Naming Conventions
------------------
EMMO uses :code:`skos:prefLabel` for human readable names. Within one ontology (or namespace), all SKOS:prefLabel's should be unique. Each entity should have **one and only one** :code:`skos:prefLabel`. Use :code:`skos:altLabel` for alternative labels. It is good practice to also keep values for :code:`skos:altLabel` unique within a namespace.

Class labels should be singular nouns and PascalCase. Property labels should be lowerCamelCase. Object and data properties should (normally) start with “has” followed by a noun. EMMO top and middle does not explicitely define inverse relations (but uses :code:`inverse(has<Something>)` instead). Instance labels should be :code:`lowercase_with_underscores`.
