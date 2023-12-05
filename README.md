[![DOI](https://zenodo.org/badge/570454941.svg)](https://zenodo.org/badge/latestdoi/570454941)

<!-- markdownlint-disable MD033 -->

# Electrochemistry Domain Ontology

<!-- [![CI tests](https://github.com/emmo-repo/domain-electrochemistry/workflows/CI%20tests/badge.svg)](https://github.com/emmo-repo/domain-electrochemistry/actions/) -->

An electrochemistry domain ontology developed in the [BIG-MAP][2] project.
The ontology is a part of the [Battery Interface Domain Ontology (BattINFO)](https://github.com/BIG-MAP/BattINFO).

The ontology is based on [EMMO][1].

A reference documentation of the individual classes is available in [html](https://emmo-repo.github.io/domain-electrochemistry/index.html) and [pdf](https://emmo-repo.github.io/domain-electrochemistry/electrochemistry.pdf) formats.

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
