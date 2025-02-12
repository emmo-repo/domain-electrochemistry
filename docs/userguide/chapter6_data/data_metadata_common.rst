Metadata common to all data
===========================

We have selected a minimum set of metadata attributes we consider are required to guarantee compliance with the FAIR data principles. We name these attributes using terms available in authoritative standards, and categorize them according to what information they convey about the data.

By JSON-LD conventions, the metadata file must specify:  

* A *context*, mapping the terms to be used with their unique identifiers. The contect is either contained in the same metadata file or references another JSON-LD file. For simplicity we have prepared a context file with most of the terms to be used; we reference the identifier of that file in the context.
* A *type*, defining what resource we are describing. In our examples, all resurces are datasets, so we assign the class Dataset to the type.

.. code-block:: json

      {
        "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
        "@type": "Dataset"

      }

Bibliographic metadata
~~~~~~~~~~~~~~~~~~~~~~~
Describe the dataset as a resource, with attributes such as title, description, authors, affiliations, creation date, etc. The following example is an excerpt from a dataset `published <https://zenodo.org/records/13318553>`_ in Zenodo.

.. code-block:: json

      {
        "@id": "https://doi.org/10.5281/zenodo.13318553",
        "dc:title": "Lithium Ion Battery Test Dataset for Maritime Transport INR18650-MJ1",
        "dc:description": "INR18650-MJ1 test data obtained from cycling under conditions relevant for maritime transport applications.",
        "dc:created": "2024-11-05T13:25:47",
        "dc:version": "1.0.0",
        "dc:creator": [
            {
            "@type": "Person",
            "@id": "https://orcid.org/0009-0004-5898-2411",
            "schema:name": "Kristian Fredrik Klepp Thorbjørnsen",
            "schema:affiliation": {
                                    "@type": "Organization", 
                                    "@id":"https://ror.org/011sn6j23", 
                                    "schema:name": "Corvus Energy"
                                    }
            },
            {
            "@type": "Person",
            "@id": "https://orcid.org/0009-0007-1253-1553",
            "schema:name": "Omar Mousteau",
            "schema:affiliation": {
                                    "@type": "Organization", 
                                    "@id":"https://ror.org/01f677e56", 
                                    "schema:name": "SINTEF"
                                    }
            },
        ],
        
        "dc:contributor": [
            {
            "@type": "Person",
            "@id": "https://orcid.org/0000-0003-2954-1233",
            "schema:name": "Eibar Flores",
            "schema:affiliation": {
                                    "@type": "Organization", 
                                    "@id":"https://ror.org/01f677e56", 
                                    "schema:name": "SINTEF"
                                    }
            },
            {
            "@type": "Person",
            "@id": "https://orcid.org/0000-0002-2228-2016",
            "schema:name": "Dennis Kopljar",
            "schema:affiliation": {
                                    "@type": "Organization", 
                                    "@id":"https://ror.org/04bwf3e34", 
                                    "schema:name": "Deutsches Zentrum für Luft- und Raumfahrt e. V. (DLR)"
                                    }
            },
        ]

      }

Notice how the keys with metadata terms use either Dublin Core (abbreviated with the prefix "dc") or Schema.org (abbreviated with the prefix "schema") terms. This is indeed common: we mix terms from different authoritative vocabularies to cover the attributes we wish to describe.


Technical metadata
~~~~~~~~~~~~~~~~~~
Describe file properties such as format and size.

.. code-block:: json

      { 
        "schema:contentSize": "138 kB",
        "schema:encodingFormat": "text/csv"

      }


Governance metadata
~~~~~~~~~~~~~~~~~~
Describe how the data should be managed, with attributes about permissions, licenses, policies and compliance requirements.

.. code-block:: json

      { 
        "dc:license": {
                        "@type": "dc:LicenseDocument", 
                        "@id": "https://creativecommons.org/licenses/by/4.0/",
                        "dc:title":"Creative Commons Attribution 4.0 International", 
                        },
        "dc:rightsHolder": {
                            "@type": "Organization", 
                            "@id":"https://ror.org/01f677e56", 
                            "schema:name": "SINTEF"
                            }
      }


Domain metadata
~~~~~~~~~~~~~~~
Describe the context about the scientific domain of the data, with attributes related to methodologies used in the acquisition of the data, acquisition conditions, processes and devices involved, etc.

.. code-block:: json

    {
    "@reverse": {
        "hasOutput": {
        "@type": "CyclicVoltammetry"
        }
    }