![reason](https://github.com/emmo-repo/domain-electrochemistry/actions/workflows/reason.yml/badge.svg)
![docs](https://github.com/emmo-repo/domain-electrochemistry/actions/workflows/doc.yml/badge.svg)
[![DOI](https://zenodo.org/badge/570454941.svg)](https://zenodo.org/badge/latestdoi/570454941)


<!-- markdownlint-disable MD033 -->

# Electrochemistry Domain Ontology

<!-- [![CI tests](https://github.com/emmo-repo/domain-electrochemistry/workflows/CI%20tests/badge.svg)](https://github.com/emmo-repo/domain-electrochemistry/actions/) -->
The Electrochemistry Domain Ontology is a specialized domain within the Elementary Multiperspective Materials Ontology [(EMMO)][1], that encompasses essential terms and relationships for electrochemical systems, materials, methods, and data. Its primary objective is to enable the creation of linked and FAIR (Findable, Accessible, Interoperable, and Reusable) data, thereby fostering advancements in research and innovation within the realm of electrochemistry. This ontology serves as a foundational resource for harmonizing electrochemical knowledge representation, enhancing data interoperability, and accelerating progress in electrochemical research and development.

A reference documentation is available in [html](https://emmo-repo.github.io/domain-electrochemistry/index.html) and [pdf](https://emmo-repo.github.io/domain-electrochemistry/electrochemistry.pdf) formats.

### Persistent Identifiers

This ontology assigns persistent machine-readable identifiers to concepts from the electrochemistry domain. These identifiers facilitate data exchange and interoperability among various tools and systems. It includes annotations to other sources of information including [DBPedia](https://www.dbpedia.org/) and [Wikidata](https://www.wikidata.org/). 

### Standardized Nomenclature

The ontology builds on standardized nomenclature for electrochemistry, relying on recognized authorities including [IUPAC](https://iupac.org/what-we-do/nomenclature/) and the [IEC](https://www.electropedia.org/). IUPAC is the universally-recognized authority on chemical nomenclature and terminology, and IEC is the the world's leading organization that prepares and publishes International Standards for all electrical, electronic and related technologies. This consistency in naming conventions enhances collaboration and data sharing.

## Usage

This domain ontology can be used to generate Linked Data in any RDF-supported format. Below is an example desecribing a zinc foil electrode with some creator information and properties. Please see the documentation for [more examples](https://emmo-repo.github.io/domain-electrochemistry/pages/examples.html). 

```json
{
    "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
    "@type": "Electrode",
    "schema:manufacturer": {
       "@type": "schema:ResearchOrganization",
       "@id": "https://www.wikidata.org/wiki/Q3041255",
       "schema:name": "SINTEF"
    },
    "schema:creator": {
       "@type": "schema:Person",
       "@id": "https://orcid.org/0000-0002-8758-6109",
       "schema:name": "Simon Clark"
    },
    "hasActiveMaterial": {
       "@type": ["Zinc", "Foil"]
    },
    "hasProperty": [
       {
             "@type": ["SpecificCapacity", "MeasuredProperty"],
             "hasNumericalPart": {
                "@type": "Real",
                "hasNumericalValue": 800
             },
             "hasMeasurementUnit": "emmo:MilliAmpereHourPerGram"
       },
       {
             "@type": ["Thickness", "ConventionalProperty"],
             "hasNumericalPart": {
                "@type": "Real",
                "hasNumericalValue": 250
             },
             "hasMeasurementUnit": "emmo:MicroMetre"
       },
       {
             "@type": ["Diameter", "MeasuredProperty"],
             "hasNumericalPart": {
                "@type": "Real",
                "hasNumericalValue": 2
             },
             "hasMeasurementUnit": "emmo:CentiMetre"
       },
       {
             "@type": ["Mass", "MeasuredProperty"],
             "hasNumericalPart": {
                "@type": "Real",
                "hasNumericalValue": 2.5
             },
             "hasMeasurementUnit": "emmo:Gram"
       }
    ]
}
```

## Structure and Integration with EMMO

The Electrochemistry Domain Ontology is an official domain on the EMMO. The asserted source consists of two files:
- `electrochemistry.ttl`: describes terms and object properties for the electrochemistry domain.
- `electrochemicalquantities.ttl`: describes the physical quantities related to the electrochemistry domain. It is encapsulated to allow it to be imported by other EMMO domains without needing to import the entire ontology.

The electrochemistry domain also imports other EMMO domains:
- [Chemical Substance Domain Ontology](https://github.com/emmo-repo/domain-chemical-substance): provides material annotations for electrochemical (meta)data.

The import structure is summarized in the following table:
| Imported Ontologies | Version           |
| ------------------- | ----------------- |
| EMMO                | 1.0.0-beta5       |
| chemical-substance  | 0.2.0-alpha       |

For simplicity, we complie the source files and other imports into a [pre-inferred ontology](inferred_version/electrochemistry-inferred.ttl). This is the result of running the asserted source files through a semantic reasoner and includes both asserted and inferred properties in a clear graph. 

## Getting Started

### Prerequisites

Before you begin, we recommend that you install the following tools. They are not all required, but greatly simplify the process of working with ontologies:

- [Protégé](https://protege.stanford.edu/) (a graphical ontology editor)
  - Installation instructions are available [here](https://protege.stanford.edu/software.php#desktop-protege).

- [EMMOntoPy](https://github.com/emmo-repo/EMMOntoPy) (python package for working with EMMO ontologies)
  - Installation instructions are available [here](https://github.com/emmo-repo/EMMOntoPy#installation).

- [RDFLib](https://rdflib.readthedocs.io/en/stable/) (optional, python package for working with RDF graphs)
  - Installation instructions are available [here](https://rdflib.readthedocs.io/en/stable/gettingstarted.html).

- [VS Studio Code](https://code.visualstudio.com/) (optional, a code editor with extensions for RDF formats like TTL and JSON-LD)
  - Installation instructions are available [here](https://code.visualstudio.com/download).

### Quick Start

To quickly explore and make use of the ontology, first download the pre-inferred version [pre-inferred ontology](inferred_version/electrochemistry-inferred.ttl). You can then simply open the file in Protégé and explore its content or load the ontology into python using EMMOntoPy.

In [EMMOntoPy](https://github.com/emmo-repo/EMMOntoPy), you can choose to import the ontology from your local downloaded copy or directly from the web. Commands for both options are given below:

```python
from ontopy import get_ontology

# Loading from local repository
electrochemistry = get_ontology('/path/to/domain-electrochemistry/electrochemistry-inferred.ttl').load(url_from_catalog=True)

# Loading from web
electrochemistry = get_ontology('https://raw.githubusercontent.com/emmo-repo/domain-electrochemistry/master/inferred_version/electrochemistry-inferred.ttl').load()
```

## Contributing

We welcome contributions from the community to enhance and expand the ontology. If you have suggestions, improvements, or additional chemical substance information to contribute, please refer to our [Contribution Guidelines](CONTRIBUTING.md).

### Acknowledgements

<img src="docs/assets/img/Flag_of_Europe.png" alt="EU-Flag" width="100">

This project has received support from European Union research and innovation programs, under grant agreement numbers:

* 957189 - [BIG-MAP](http://www.big-map.eu/) 

## License

The Battery Interface Domain Ontology is released under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode) license (CC BY 4.0).

[1]: https://github.com/emmo-repo/EMMO
[2]: https://www.big-map.eu
