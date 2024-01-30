
.. toctree::
   :includehidden:
   :hidden:

   Get Started <getstarted>
   Examples <examples>
   Class Index <electrochemistry>
   About <about>
   FAQ <faq>

Electrochemistry Ontology
================================

Welcome to the **EMMO Electrochemistry Domain Ontology**, a semantic resource with essential terms and relationships to describe electrochemical systems, materials, methods, and data. **Here's a simple example:**

.. tab-set::

   .. tab-item:: JSON

      .. code-block:: json
         :linenos:

         {
            "@context": "https://raw.githubusercontent.com/emmo-repo/domain-electrochemistry/master/context.json",
            "@type": "ElectrochemicalCell",
            "hasNegativeElectrode": {
               "@type": "ZincElectrode"
            },
            "hasPositiveElectrode": {
               "@type": "ManganeseDioxideElectrode"
            },
            "hasElectrolyte": {
               "@type": "AlkalineElectrolyte"
            }
         }

   .. tab-item:: JSON-LD Playground

      .. raw:: html
         
         <iframe id="jsoncrackEmbed" width="100%" height="500" src="https://jsoncrack.com/widget?json=https://raw.githubusercontent.com/emmo-repo/domain-electrochemistry/master/sphinx/assets/jsonld/example_electrochemical_cell.json"></iframe>


Check out these resources to get started!
-----------------------------------------
.. grid::

    .. grid-item-card::
        :link: getstarted.html

        :octicon:`rocket;1em;sd-text-info`  Get Started
        ^^^^^^^^^^^
        Let's go! Here is some information to help you get started

    .. grid-item-card::
        :link: electrochemistry.html

        :octicon:`book;1em;sd-text-info`  Class Index
        ^^^^^^^^^^^
        A complete list of terms and some human-readable annotations

.. grid::

    .. grid-item-card::
        :link: examples.html

        :octicon:`pencil;1em;sd-text-info`  Examples
        ^^^^^^^^
        Here are some examples that demonstrate basic usage of the ontology

    .. grid-item-card::
        :link: contribute.html

        :octicon:`thumbsup;1em;sd-text-info`  Contribute
        ^^^^^^^^^^
        Help us develop the ontology by following these guidelines