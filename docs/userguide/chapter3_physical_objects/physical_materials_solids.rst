.. toctree::
   :hidden:
      
   ../../examples/materials/example_zinc.ipynb

Solid Materials
---------------

Here we explore defining materials that typically exist in the solid phase. This distinction is made purely for convenience of organizing the content; an EMMO material can be defined independent of its phase. 

Guidelines for Use 
~~~~~~~~~~~~~~~~~~

To represent a material using the ontology, follow three key steps:

1. **Identify the Material**  
   Determine what the material with the class ``Material`` or one of its more specific subclasses. Using multiple inheretance, the description of material can be further refined by combining it with a chemical substance (e.g. ``Zinc``) and a form (e.g. ``Powder``). 
 
2. **Assign Properties**  
   Define the material's attributes using annotation properties (e.g., ``molecularFormula``) and quantitative properties (e.g., ``Density``, ``SpecificCapacity``).

3. **Link the Material to another Object or Role**  
   Use object properties like ``hasActiveMaterial`` to connect the material to an ``Electrode`` or ``ElectrodeCoating``.

Examples
~~~~~~~~

Here is a simple example of a zinc foil active material with a few basic properties:

.. literalinclude:: ../../assets/jsonld/materials/material_zinc.jsonld
   :language: json

In example above, we use multiple inheretance to say that we are something that is ``Zinc`` and a ``Foil``. A ``Foil`` is defined as a more specific sub-class of ``Material`` in the ontology. The zinc foil is associated to some properties using the ``hasProperty`` relationship. There are different types of properties in EMMO. In this case, we say that the ``Density`` is a ``ConventionalProperty`` because we don't measure it ourselves, rather we accept a value by convention, in this case from a data sheet. The value of the property is expressed according to the SI recommendations as a numerical part and a measurement unit. More information about ``Zinc``, including links to external sources of information like Wikidata and PubChem can be found in the ontology term documentation. 

More detailed examples are available:

.. grid::

    .. grid-item-card::
        :link: ../../examples/materials/example_cobalt_oxide.ipynb

        :octicon:`rocket;1em;sd-text-info`  Cobalt Oxide
        ^^^^^^^^^^^
        An active material that is common in energy devices

    .. grid-item-card::
            :link: ../../examples/materials/example_gold.ipynb

            :octicon:`rocket;1em;sd-text-info` Gold
            ^^^^^^^^^^^
            An active material that is common in energy devices

    .. grid-item-card::
            :link: ../../examples/materials/example_iridium_oxide.ipynb

            :octicon:`rocket;1em;sd-text-info`  Iridium Oxide
            ^^^^^^^^^^^
            An active material that is common in energy devices

.. grid::

    .. grid-item-card::
        :link: ../../examples/materials/example_manganese_dioxide.ipynb

        :octicon:`rocket;1em;sd-text-info`  Manganese Dioxide
        ^^^^^^^^^^^
        An active material that is common in energy devices

    .. grid-item-card::
            :link: ../../examples/materials/example_nickel_oxyhydroxide.ipynb

            :octicon:`rocket;1em;sd-text-info` Nickel Oxyhydroxide
            ^^^^^^^^^^^
            An active material that is common in energy devices

    .. grid-item-card::
            :link: ../../examples/materials/example_nickel.ipynb

            :octicon:`rocket;1em;sd-text-info`  Nickel
            ^^^^^^^^^^^
            An active material that is common in energy devices

.. grid::

    .. grid-item-card::
        :link: ../../examples/materials/example_platinum.ipynb

        :octicon:`rocket;1em;sd-text-info`  Platinum
        ^^^^^^^^^^^
        An active material that is common in energy devices

    .. grid-item-card::
            :link: ../../examples/materials/example_ruthenium_oxide.ipynb

            :octicon:`rocket;1em;sd-text-info` Ruthenium Oxide
            ^^^^^^^^^^^
            An active material that is common in energy devices

    .. grid-item-card::
            :link: ../../examples/materials/example_silver_oxide.ipynb

            :octicon:`rocket;1em;sd-text-info`  Silver Oxide
            ^^^^^^^^^^^
            An active material that is common in energy devices

.. grid::

    .. grid-item-card::
        :link: ../../examples/materials/example_silver.ipynb

        :octicon:`rocket;1em;sd-text-info`  Silver
        ^^^^^^^^^^^
        An active material that is common in energy devices

    .. grid-item-card::
            :link: ../../examples/materials/example_titanium_dioxide.ipynb

            :octicon:`rocket;1em;sd-text-info` Titanium Dioxide
            ^^^^^^^^^^^
            An active material that is common in energy devices

    .. grid-item-card::
            :link: ../../examples/materials/example_zinc_oxide.ipynb

            :octicon:`rocket;1em;sd-text-info`  Zinc Oxide
            ^^^^^^^^^^^
            An active material that is common in energy devices

.. grid::

    .. grid-item-card::
        :link: ../../examples/materials/example_zinc.ipynb

        :octicon:`rocket;1em;sd-text-info`  Zinc
        ^^^^^^^^^^^
        An active material that is common in energy devices