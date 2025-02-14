Other files
===========

While there are no universal rules to describe generic files, we reccommend following two general rules:  

* *Avoid starting from stracth*. Use an existing JSON-LD template for a file type similar to the one you wish to describe. For instance,  `Feather file types <https://arrow.apache.org/docs/python/feather.html>`_ store tabular data in binary format, so it is natural to use the template of Parquet files to describe Feather files.
* *Maximize coverage of attributes*. The more attributes you describe about your data, the easier will be to interpret by other humans and machines.

Here are some generic guidelines to describe other file formats you might encounter.


Excel Files
~~~~~~~~~~~~

Excel files are hierarchical, since they support sheets, each supporting tabular datasets. It is therefore a good idea to start from the HDF5 template, mapping sheets as groups and the tables within sheets as datasets. 

Note, however, that Excel files might be complex, e.g. might have more than one table per sheet, attributes might be stored as rows and observations as columns, sheets might additionally contain images, plots, macros, etc. Therefore, before investing time developing a JSON-LD description for a particular Excel file, consider how much effort is required. 

As a general rule:

* Start by describing the bibliographic, governance, domain and technical metadata. 
* If the Excel files are simple and tidy, use the HDF5 template to describe sheets as groups, and tables as arrays.
* Instead, if the Excel files are complex, you might either:
   * Stop at the file metadata level, without describing the contents of the file. Or
   * Embark in a detailed JSON-LD description if you expect to deal with a large number of Excel files that share the same internal schema. Might the force be with you.

Remember to describe the Excel encoding format as part of the technical metadata.

.. code-block:: json

      {
      "schema:contentSize": "42 MB",
      "schema:encodingFormat": "application/vnd.ms-excel",
      "@reverse": {
            "hasOutput": {"@type": "CyclicVoltammetry"}
        }

      }


JSON Files
~~~~~~~~~~~

You might encountrer datasets stored as JSON particularly if these are exchanged between APIs. Instead of creating a separate JSON-LD file ``"dataset_metadata.jsonld"`` for your ``"dataset.json"``, we reccommend embedding JSON-LD keys into the JSON file itself. In this way we can preserve the content and hierarchy of ``dataset.json`` and we avoid developing a new hierarchy for a separate JSON-LD file. 

Follow the following guidelines to upgrade your JSON dataset into a JSON-LD dataset:  

**Add a context, dataset type and unique identifier**. 

.. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "Dataset",
        "@id": "https://doi.org/10.5281/zenodo.13318553", 
        "dc:title": "Lithium Ion Battery Test Dataset",
        ...

      }

**Ensure the file has metadata**, if not, add bibliographic and governance metadata as in [LINK TO METADATA SECTION].

**Annotate each JSON object with a type**, whose value define the type or class of the object. Object types must use a term defined in the context. Objects migth describe persons ``"@type": "foaf:Person"``, quantities ``"@type": "emmo:Pressure"``, units ``"@type": "emmo:Kelvin"``, etc.


**Quantities must have values and units**, for instance:

.. code-block:: json

    {
      "@type": "ElectricCurrent",
      "hasNumericalValue": 0.093,
      "hasMeasurementUnit": "emmo:Ampere"
    } 

**Map every key to a controlloed vocabulary**, or do your best at matching each JSON key. Use the classes and attributes specificed in the `context <https://emmo-repo.github.io/domain-electrochemistry/context/context.json>`_ we provide, and include additional vocabularies if needed. If you add a new vocabulary that is not part our `context file <https://emmo-repo.github.io/domain-electrochemistry/context/context.json>`_, e.g. if you wish to use the BFO ontology, ensure the IRI of the vocabulary is referenced in the file context and assigned a prefix.

.. code-block:: json

    {
      "@context": {
        "": "https://emmo-repo.github.io/domain-electrochemistry/context/context.json",
        "bfo": "http://purl.obolibrary.org/obo/bfo.owl"
      }
    } 

XXX



