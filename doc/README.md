# Generate documentation for Electrochemistry Domain Ontology

This directory contains the needed templates, introductory text and figures for generating a reference documentation of Electrochemistry Domain Ontology.

The documentation is generated using EMMOntoPy and pandoc.
Just run the script `mkdoc.sh`:

```shell
./mkdoc.sh
```

## Content of this directory

### EMMOntoPy `ontodoc` templates with introductory text and document layout

* [electrochemistry.md](electrochemistry.md): Main template.
  It includes the other templates.
* [introduction.md](introduction.md): Introductory text.
* [classes.md](classes.md): Introduction and sections for Classes

### `pandoc` configuration files

* [electrochemistry-meta.yaml](electrochemistry-meta.yaml): Metadata for the ontology, like title, authers, abstract, etc.
* [pandoc-args.yaml](pandoc-args.yaml): General pandoc options.
* [pandoc-html-args.yaml](pandoc-html-args.yaml): Additional pandoc options for html generation.
* [pandoc-pdf-args.yaml](pandoc-pdf-args.yaml): Additional pandoc options for pdf generation.
* [pandoc-html.css](pandoc-html.css): css file used for html generation.
* [pandoc-template.html](pandoc-template.html): Modified copy of the standard pandoc html template with a small adjustment for the author list.
* [pandoc-template.tex](pandoc-template.tex): Modified copy of the standard pandoc latex template with a small adjustment for the author list.
