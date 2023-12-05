[![DOI](https://zenodo.org/badge/570454941.svg)](https://zenodo.org/badge/latestdoi/570454941)

<!-- markdownlint-disable MD033 -->

# Electrochemistry Domain Ontology

<!-- [![CI tests](https://github.com/emmo-repo/domain-electrochemistry/workflows/CI%20tests/badge.svg)](https://github.com/emmo-repo/domain-electrochemistry/actions/) -->
The Electrochemistry Domain Ontology, a specialized domain within the Elementary Multiperspective Materials Ontology [(EMMO)][1], encompasses essential terms and relationships for electrochemical systems, materials, methods, and data. Its primary objective is to enable the creation of linked and FAIR (Findable, Accessible, Interoperable, and Reusable) data, thereby fostering advancements in research and innovation within the realm of electrochemistry. This ontology serves as a foundational resource for harmonizing electrochemical knowledge representation, enhancing data interoperability, and accelerating progress in electrochemical research and development.

A reference documentation is available in [html](https://emmo-repo.github.io/domain-electrochemistry/index.html) and [pdf](https://emmo-repo.github.io/domain-electrochemistry/electrochemistry.pdf) formats.

## Integration with EMMO

The Electrochemistry Domain Ontology is an official domain on the EMMO. It consists of two files:
- `electrochemistry.ttl`: describes terms and object properties for the electrochemistry domain.
- `electrochemicalquantities.ttl`: describes the physical quantities related to the electrochemistry domain. It is encapsulated to allow it to be imported by other EMMO domains without needing to import the entire ontology.

The electrochemistry domain also imports:
- the [Chemical Substance Domain Ontology](https://github.com/emmo-repo/domain-chemical-substance): provides material annotations for electrochemical (meta)data.

## Obtaining the ontology

The correct path to the inferred verion `emmo-inferred` is specified in the catalog file, [`catalog-v001.xml`](catalog-v001.xml).

The domain ontology is obtained with:

```console
git clone https://github.com/emmo-repo/domain-electrochemistry.git
```

When opening electrochemistry.ttl in Protégé, the correct versions of EMMO and other ontology dependencies will be downloaded and imported.

In [EMMOntoPy](https://github.com/emmo-repo/EMMOntoPy), correct import is obtained with:

```python
from ontopy import get_ontology

# Loading from local repository
electrochemistry = get_ontology('/path/to/domain-electrochemistry/electrochemistry.ttl').load(url_from_catalog=True)

# Loading from web
electrochemistry = get_ontology('https://raw.githubusercontent.com/emmo-repo/domain-electrochemistry/master/electrochemistry.ttl').load()
```

### Acknowledgements

<img src="documentation/images/flag_of_europe.png" alt="EU-Flag" width="100">

This project has received support from European Union research and innovation programs, under grant agreement numbers:

* 957189 - [BIG-MAP](http://www.big-map.eu/) 

## License

The Battery Interface Domain Ontology is released under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode) license (CC BY 4.0).

[1]: https://github.com/emmo-repo/EMMO
[2]: https://www.big-map.eu
