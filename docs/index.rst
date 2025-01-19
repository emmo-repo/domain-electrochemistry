
.. toctree::
   :includehidden:
   :hidden:

   Get Started <pages/getstarted>
   Examples <pages/examples>
   Class Index <pages/electrochemistry>
   About <pages/about>
   FAQ <pages/faq>

Electrochemistry Ontology
================================

Welcome to the **EMMO Electrochemistry Domain Ontology**, a semantic resource with essential terms and relationships to describe electrochemical systems, materials, methods, and data. **Here's a simple example:**

.. tab-set::

   .. tab-item:: JSON

      .. literalinclude:: ../examples/snippets/example_alkaline_zinc_electrochemical_cell.json
         :language: json
         :linenos:
         
   .. tab-item:: JSON-LD Playground

      .. raw:: html
            
         <div style="position: relative; padding-top: 56.25%;">  <!-- Aspect ratio of 16:9 -->
            <iframe src="https://json-ld.org/playground/#startTab=tab-expanded&json-ld=" + encodeURIComponent(JSON.stringify(require("../examples/snippets/example_alkaline_zinc_electrochemical_cell.json"))) + " style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" frameborder="0" allowfullscreen></iframe>
         </div>



Check out these resources to get started!
-----------------------------------------
.. grid::

    .. grid-item-card::
        :link: pages/getstarted.html

        :octicon:`rocket;1em;sd-text-info`  Get Started
        ^^^^^^^^^^^
        Let's go! Here is some information to help you get started

    .. grid-item-card::
        :link: pages/electrochemistry.html

        :octicon:`book;1em;sd-text-info`  Class Index
        ^^^^^^^^^^^
        A complete list of terms and some human-readable annotations

.. grid::

    .. grid-item-card::
        :link: pages/examples.html

        :octicon:`pencil;1em;sd-text-info`  Examples
        ^^^^^^^^
        Here are some examples that demonstrate basic usage of the ontology

    .. grid-item-card::
        :link: pages/contribute.html

        :octicon:`thumbsup;1em;sd-text-info`  Contribute
        ^^^^^^^^^^
        Help us develop the ontology by following these guidelines
