# Contributing to the ontology

There are two ways you can contribute to the ontology:
- Suggesting minor changes to the developers by reporting issues. This is the best option for most people.
- Editing the ontology files directly and submitting a pull request. This requires a more detailed knowledge of ontology development and EMMO guidelines.

These two options are described below. 

## Suggest minor changes on existing elements

[Create a feature request](https://github.com/emmo-repo/domain-electrochemistry/issues/new) in a [Github Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue) to suggest edits to names, defintions, references on existing classes and properties.

## Propose additions/deletion of elements

We recommend using the [forking workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow) to contribute additions/deletions.
Fork this repository, clone the fork on your local PC, create your branch based on the existing `dev` branch (e.g. `dev_john_doe`) and work on the editions in you local copy.

### Editing the ontology programmatically in python
One is programmatically, using for instance [EMMOntoPy](https://github.com/emmo-repo/EMMOntoPy).

### Editing the ontology in a graphical user interface (GUI) 
[Protégé](https://protege.stanford.edu/)  is a widely used graphical development environment for ontologies and knowledge graphs. It is open-source software that is maintained by Stanford University in the United States.

Before adding elements, ensure Prot´égé is configured to create IRIs in the right format:

* Open Protégé
* Go to File/Open and load the ontology file you wish to modify
* Go to File/Preferences and there go to the New Entities Tab
* Ensure you have configured the preferences as shown below:

  ![Protege config.](docs/images/protege_config_contribute.png)  
  Here is the "Specified IRI" for you to copy: ```https://w3id.org/emmo/domain/electrochemistry#```

Once you have made your changes, commit them to your fork and [create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
* We will assess the request and submit feedback if necessary. If the pull request meets the requirements for inclusion, we will merge it.
