
.. toctree::
   :includehidden:
   :hidden:

   Get Started <pages/getstarted>
   Examples <pages/examples>
   Class Index <pages/electrochemistry>
   About <pages/about>
   FAQ <pages/faq>

================================
Electrochemistry Ontology
================================

Welcome to the **EMMO Electrochemistry Domain Ontology (ECHO)**, a formal representation of knowledge about electrochemical systems. ECHO describes concepts as classes, connected to each other via links or edges called object properties.   

The figure below illustrates how the concept of ``ElectrochemicalReaction`` is represented as a class, linked to a parent class ``ChemicalReaction`` and to several subclasses using the ``isA`` object property.

.. image:: /assets/img/example_network.png

Classes and object properties form a network of nodes and edges, which is represented in a machine-readable format using the Resource Description Framework (RDF), and serialized in `Turtle syntax <https://www.w3.org/TR/turtle/>`_ into text files with ``.ttl`` extension.


------------------------------------
Representing concepts as Classes
------------------------------------

Each class must have a unique identifier, an elucidation, and may have additional attributes such as alternative labels and references to other sources describing the same concept. See the concept of `ElectrochemicalReaction <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a6a69e90_06b5_45b1_83cf_7c0bf39b2914>`_ illustrated below.

.. image:: /assets/img/class_example.png
   :scale: 50 %
   :align: center

ECHO rarely define classes from scratch; most classes inherit from complementary ontologies, and branch from few high-level concepts: 

* `Electrode <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0f007072_a8dd_4798_b865_1bf9363be627>`_
* `Electrolyte <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_fb0d9eef_92af_4628_8814_e065ca255d59>`_
* `ElectrochemicalCell <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6f2c88c9_5c04_4953_a298_032cc3ab9b77>`_
* `ElectrochemicalPhenomenon <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_19abaccd_43be_4048_965c_e4fb63c5951b>`_
* `ElectrochemicalMeasurementProcess <https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f4ce4df2_d7e6_470f_8eab_3a911adaaf0f>`_ 

See Ontology Structure (LINK TO SECTION) for more details.


--------------
Intended usage
--------------

ECHO serves as a foundational resource for harmonizing the representation of electrochemical knowledge, as it provides:  


**1. A formal vocabulary** to annotate materials, data, devices and systems in electrochemistry. Annotated resources become discoverable and can be interoperated across software systems and applications. Here's a simple example of an annotation describing a Zinc Air cell using ontology concepts:

.. tab-set::

   .. tab-item:: JSON

      .. code-block:: json
         :linenos:

         {
            "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
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
            
         <div style="position: relative; padding-top: 56.25%;">  <!-- Aspect ratio of 16:9 -->
            <iframe src="https://json-ld.org/playground/#startTab=tab-expanded&json-ld=%7B%22%40context%22%3A%22https%3A%2F%2Fraw.githubusercontent.com%2Femmo-repo%2Fdomain-electrochemistry%2Fmaster%2Fcontext.json%22%2C%22%40type%22%3A%22ElectrochemicalCell%22%2C%22hasNegativeElectrode%22%3A%7B%22%40type%22%3A%22ZincElectrode%22%7D%2C%22hasPositiveElectrode%22%3A%7B%22%40type%22%3A%22ManganeseDioxideElectrode%22%7D%2C%22hasElectrolyte%22%3A%7B%22%40type%22%3A%22AlkalineElectrolyte%22%7D%7D" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" frameborder="0" allowfullscreen></iframe>
         </div>


**2. A glossary of concepts** with definitions from authoritative sources, which improve communication between human agents across laboratories, countries, languages and subfields in electrochemistry.

**3. A logically consistent and machine-readable representation of electrochemistry knowledge**, supporting symbolic reasoning, knowledgebases and actions from AI agents.


--------------
Governance
--------------

ECHO started as an initiative of the `BIG-MAP consortium <https://www.big-map.eu/>`_ , with the initial goals of enhancing data interoperability and supporting autonomous AI-driven research workflows in the discovery and design of battery materials and processes. Given its broad applicability, ECHO has transcended its initial goals and it is now maintained and governed by a multidisciplinary team of electrochemistry and ontology experts supported by several EU-funded projects:  

* BIG-MAP
* Battery2030+


-----------------------------------------
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