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
        :link: physical_functional_materials_active_material.html

        :octicon:`rocket;1em;sd-text-info`  Zinc
        ^^^^^^^^^^^
        An active material that is common in energy devices

    .. grid-item-card::
        :link: userguide/chapter3_physical_objects/physical_functional_materials_electrolyte_solution.html

        :octicon:`book;1em;sd-text-info`  Platinum
        ^^^^^^^^^^^
        An active material that is common in reference electrodes

    .. grid-item-card::
        :link: userguide/chapter3_physical_objects/physical_functional_materials_electrolyte_solution.html

        :octicon:`book;1em;sd-text-info`  Iridium Oxide
        ^^^^^^^^^^^
        An active material that is common in catalysis