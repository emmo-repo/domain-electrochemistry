Ontology Capabilities
---------------------

Semantic Reasoning
~~~~~~~~~~~~~~~~~~

Reasoning allows machines to infer facts from existing data. For example, if we know that *every mammal is an animal* and *a cat is a mammal*, a reasoning engine can infer that *a cat is an animal* — even if it’s not written anywhere.

This inferencing capability is crucial for solving complex problems and answering questions that go beyond surface-level information. Reasoning in ontologies is supported by formal logic and rules embedded within frameworks like OWL. These rules allow machines to:

- **Classify data:** Automatically categorize new items based on their properties and relationships.  

- **Check logical consistency:** Ensure that data does not contain logical contradictions (e.g., an object cannot simultaneously be defined as "hot" and "cold").  

- **Discover hidden relationships among entities:** Identify hidden connections between concepts, enhancing data integration and discovery.  

For instance, reasoning systems are used in healthcare to determine potential drug interactions based on patient data and medical ontologies. Similarly, in battery science, reasoning can help identify optimal materials by linking experimental results with material properties and performance metrics.

.. admonition:: Thought Experiment: The One-Armed Person

   Imagine we want to describe humans in an ontology. We might include some relationships like:

   - A human is a mammal  
   - A human has two arms  
   - A man is a human  
   - A woman is a human  
   - etc.   

   We create an individual called *Tim* and make the statement that 'Tim is a man'. Reasoning according to the knowledge in the ontology will return that 'Tim is a human'.

   But then, Tim loses an arm in some terrible accident. We append the statement 'Tim has one arm'. Reasoning again will create a logical inconsistency because if 'Tim has one arm' and 'a human as two arms', then it follows that Tim cannot be a human. 

   This demonstrates how tricky it can be to maintain internal logical consistency, especially for complex ontologies, and how important it is to support correct reasoning and inferrence. 

By enabling machines to "think" beyond the explicit data provided, reasoning transforms ontologies into dynamic tools for problem-solving and decision-making.

Semantic Querying
~~~~~~~~~~~~~~~~~

Ontologies enable a powerful form of search called semantic querying. Unlike simple keyword searches, semantic queries use the structured knowledge within an ontology to find results based on meaning, not just matching words. By understanding how concepts relate to each other, machines can interpret questions in a way that resembles human reasoning.

For example, if an ontology knows that stainless steel is a type of steel, and steel is a type of metal, then a search for “metal” can automatically include results about stainless steel — even if “metal” is not mentioned in the dataset.

Semantic queries are written in SPARQL, a query language for RDF-based data. SPARQL retrieves and filters information by matching patterns in the ontology’s graph. It can answer questions such as:

 - *“Which restaurants serve vegetarian salads?”*  
 - *“Which materials are compatible with a given battery type?”*  

Because ontologies define relationships between entities, SPARQL can traverse those links to return accurate and context-aware results.

This capability is invaluable across fields. In healthcare, it can reveal drug interactions or relate symptoms to diagnoses. In environmental science, it can connect climate data with biodiversity and conservation records. By enabling machines to understand and connect information, semantic querying has become a cornerstone of modern knowledge systems.

---