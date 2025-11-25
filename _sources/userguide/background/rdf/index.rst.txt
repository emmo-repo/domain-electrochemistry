Resource Description Framework (RDF)
====================================

The **Resource Description Framework (RDF)** provides the tools we need to implement ontologies in practice. RDF is the W3C standard for encoding knowledge as a graph of statements that link
*things* (resources) with *relationships* (properties). 

Think of RDF as a simple, universal, and machine-readable sentence structure. Just as human sentences use subjects, verbs, and objects to express meaning, RDF uses a similar pattern called a *triple* to create statements that computers can process.

A triple is a three positional statement, **subject — predicate — object**, that expressed some little bit of knowledge. For example, **Simon — is a — Person**. Triples can be combined to form a directed graph that computers can store, merge, and query.

In this chapter, we will discuss the core building block of RDF triples and graphs, including:

1. **Identifiers** serve as unique names for every entity or concept we want to talk about. In RDF, these typically take the form of URIs (Uniform Resource Identifiers), ensuring that each thing we reference has a precise, unambiguous identity.  

2. **Classes** represent categories or types of things. For example, in EMMO, we might have classes for different types of materials, physical properties, or measurement units. Classes help us organize and group related concepts.  

3. **Properties** describe relationships between things or specify characteristics of entities. They allow us to express how different concepts are connected or what attributes they possess.  

4. **Triples** are the basic building blocks of RDF statements. Each triple consists of a subject, predicate, and object - similar to how we construct basic sentences in natural language. By combining triples, we can build complex networks of interconnected information.

As we explore these components in more detail, you'll see how they work together to create a robust framework for representing knowledge. The power of RDF lies not just in its ability to describe individual facts, but in how it enables us to connect and integrate information from different sources into a coherent whole.

Contents:

.. toctree::
   :maxdepth: 2

   rdf_identifiers
   rdf_classes_properties_triples
   rdf_graphs
   rdf_formats

---