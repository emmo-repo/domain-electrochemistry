.. toctree::
   :hidden:
      
   ../../examples/example_zinc.ipynb

Active Material
---------------

The **active material**, also known as the **electrochemically active material**, is the material in an electrode that is oxidized or reduced in an electrode. 

Guidelines for Use 
~~~~~~~~~~~~~~~~~~

To represent an **Active Material** in the ontology, follow three key steps:

1. **Identify the Material**  
   Determine what the material is by combining terms for the chemical substance with the ``ActiveMaterial`` class.

2. **Assign Properties**  
   Define the material's attributes using annotation properties (e.g., ``molecularFormula``) and quantitative properties (e.g., ``Density``, ``SpecificCapacity``).

3. **Link the Material to a Functional Whole**  
   Use object properties like ``hasActiveMaterial`` to connect the material to an ``Electrode`` or ``ElectrodeCoating``.

.. tip:: Predefined Electrode Classes with Linked Active Materials

   For very common active material types, especially those covered by IEC designations, the ontology provides specific electrode classes where the type of active material is already linked. These predefined classes can save time if you just want to convey the type of active material used in a general way.

   For example, the ``ZincElectrode`` class in the ontology already links the active material ``Zinc`` to the electrode.

Examples
~~~~~~~~

Here is a simple example of a zinc foil active material with a few basic properties:

.. literalinclude:: ../../assets/jsonld/active_material_zinc.jsonld
   :language: json

In example above, we use multiple inheretance to say that we are something that is ``Zinc``, ``Foil``, and an ``ActiveMaterial``. It is associated to some properties using the ``hasProperty`` relationship. There are different types of properties in EMMO. In this case, we say that the ``Density`` is a ``ConventionalProperty`` because we don't measure it ourselves, rather we accept a value by convention, in this case from a data sheet. The value of the property is expressed according to the SI recommendations as a numerical part and a measurement unit. More information about ``Zinc``, including links to external sources of information like Wikidata and PubChem can be found in the ontology term documentation. 

More detailed examples are available:

.. grid::

    .. grid-item-card::
        :link: ../../examples/example_cobalt_oxide.ipynb

        :octicon:`rocket;1em;sd-text-info`  Cobalt Oxide
        ^^^^^^^^^^^
        An active material that is common in energy devices

    .. grid-item-card::
            :link: ../../examples/example_gold.ipynb

            :octicon:`rocket;1em;sd-text-info` Gold
            ^^^^^^^^^^^
            An active material that is common in energy devices

    .. grid-item-card::
            :link: ../../examples/example_iridium_oxide.ipynb

            :octicon:`rocket;1em;sd-text-info`  Iridium Oxide
            ^^^^^^^^^^^
            An active material that is common in energy devices

.. grid::

    .. grid-item-card::
        :link: ../../examples/example_manganese_dioxide.ipynb

        :octicon:`rocket;1em;sd-text-info`  Manganese Dioxide
        ^^^^^^^^^^^
        An active material that is common in energy devices

    .. grid-item-card::
            :link: ../../examples/example_nickel_oxyhydroxide.ipynb

            :octicon:`rocket;1em;sd-text-info` Nickel Oxyhydroxide
            ^^^^^^^^^^^
            An active material that is common in energy devices

    .. grid-item-card::
            :link: ../../examples/example_nickel.ipynb

            :octicon:`rocket;1em;sd-text-info`  Nickel
            ^^^^^^^^^^^
            An active material that is common in energy devices

.. grid::

    .. grid-item-card::
        :link: ../../examples/example_platinum.ipynb

        :octicon:`rocket;1em;sd-text-info`  Platinum
        ^^^^^^^^^^^
        An active material that is common in energy devices

    .. grid-item-card::
            :link: ../../examples/example_ruthenium_oxide.ipynb

            :octicon:`rocket;1em;sd-text-info` Ruthenium Oxide
            ^^^^^^^^^^^
            An active material that is common in energy devices

    .. grid-item-card::
            :link: ../../examples/example_silver_oxide.ipynb

            :octicon:`rocket;1em;sd-text-info`  Silver Oxide
            ^^^^^^^^^^^
            An active material that is common in energy devices

.. grid::

    .. grid-item-card::
        :link: ../../examples/example_silver.ipynb

        :octicon:`rocket;1em;sd-text-info`  Silver
        ^^^^^^^^^^^
        An active material that is common in energy devices

    .. grid-item-card::
            :link: ../../examples/example_titanium_dioxide.ipynb

            :octicon:`rocket;1em;sd-text-info` Titanium Dioxide
            ^^^^^^^^^^^
            An active material that is common in energy devices

    .. grid-item-card::
            :link: ../../examples/example_zinc_oxide.ipynb

            :octicon:`rocket;1em;sd-text-info`  Zinc Oxide
            ^^^^^^^^^^^
            An active material that is common in energy devices

.. grid::

    .. grid-item-card::
        :link: ../../examples/example_zinc.ipynb

        :octicon:`rocket;1em;sd-text-info`  Zinc
        ^^^^^^^^^^^
        An active material that is common in energy devices