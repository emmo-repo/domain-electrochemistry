# Example Queries

## SPARQL Queries

### Retrieve All Electrochemical Cells
```sparql
SELECT ?cell WHERE {
  ?cell a :ElectrochemicalCell .
}
```
### JSON-LD Examples
{
  "@context": "https://w3id.org/emmo/domain/electrochemistry",
  "@type": "ElectrochemicalCell",
  "hasNegativeElectrode": {
    "@type": "ZincElectrode"
  },
  "hasPositiveElectrode": {
    "@type": "ManganeseDioxideElectrode"
  }
}
