Materials
=========

In the Electrochemistry Domain Ontology, **materials** represent physical matter that has a defined composition, structure, and form. This includes solids, liquids, and gases — but in this section we focus primarily on *solid materials* for convenience.

Materials can be raw substances (like copper or graphite), processed forms (like foils, powders, or coatings), or engineered composites (like polymer electrolytes or catalyst inks).

A material can exist as part of a larger object (for example, as the active material in an electrode) or as an independent entity (for example, a powder in a storage container).

Conceptual overview
-------------------

In EMMO, the class `Material` sits between the purely chemical (`ChemicalSubstance`) and the physical (`PhysicalObject`) perspectives:

- **ChemicalSubstance** – describes *what* the material is made of, chemically.  
- **Material** – describes the *physical realization* of that substance, including phase, morphology, and form.  
- **PhysicalObject** – describes a *specific instance* of a material existing in space and time.

You can think of `Material` as the bridge between *chemistry* and *physics*: it connects chemical identity to physical form.

.. admonition:: Material vs. Substance vs. Component
   :class: tip

   - **Material** → A physical manifestation of matter with properties (e.g., a zinc foil, a powder, a polymer film).  
   - **ChemicalSubstance** → The abstract chemical identity (e.g., Zinc, LiFePO₄, H₂O).  
   - **Component** → A role that a material plays *as part of something larger* (e.g., “the binder component” in a coating).  

   In practice, you describe **what** it is (substance), **how** it exists (material), and **what it does** (component or role).

Guidelines for Use
------------------

To represent a material using the ontology, follow three key steps:

1. **Identify the Material**  
   Choose the appropriate subclass of `Material` or use multiple inheritance to refine meaning.  
   For example, something that is both `Zinc` (chemical substance) and `Foil` (material form) can be declared as both.

2. **Assign Properties**  
   Attach quantitative or qualitative properties using `hasProperty`.  
   These may include conventional, measured, or modelled properties such as density, porosity, or conductivity.

3. **Link the Material to its Role or Context**  
   Use domain-specific object properties like `hasActiveMaterial`, `hasBinder`, or `hasAdditive` to connect the material to another entity (for example, an `ElectrodeCoating`).

Representation Patterns
-----------------------

**1. Pure Substance in a Defined Form**

A simple zinc foil material with basic properties.

.. literalinclude:: ../../assets/jsonld/active_materials/zinc_simple.jsonld
   :language: json

Here we combine multiple inheritance (`Zinc` and `Foil`) to indicate *what it is* and *in what form*. The density is expressed as a conventional property — taken from a datasheet rather than directly measured.

**2. Material in Context — Used as an Active Material**

This shows the same zinc foil linked as an **active material** in an electrode.

.. literalinclude:: ../../assets/jsonld/electrodes/zinc_electrode_simple.jsonld
   :language: json

Here, the same material description is reused in a different context through the role relation `hasActiveMaterial`.

**3. Composite Material or Mixture**

An electrolyte composed of multiple constituents.

.. literalinclude:: ../../assets/jsonld/electrolytes/electrolyte_lp50.jsonld
   :language: json

The solvent is a mixture of two chemical substances with a lithium salt solute.

Reasoning and Reuse
-------------------

Because the ontology defines `ActiveMaterial`, `Binder`, and `Additive` as subclasses of `Material`, any description that uses those roles can be automatically inferred to involve materials.

For example, a reasoner will infer:

::
   If A hasActiveMaterial B → A hasPart B  
   and B is a Material.

This consistency allows generic SPARQL queries for `hasPart` or `Material` to still return domain-specific relations.

Best Practices
--------------

- Use **multiple inheritance** to express both chemical identity and physical form.  
- Attach properties (e.g., `Density`, `ElectricalConductivity`) using `hasProperty`.  
- Use **domain-specific part relations** (`hasActiveMaterial`, `hasBinder`, etc.) whenever possible.  
- When referencing datasheet or literature values, classify the property as a `ConventionalProperty`.  
- Reuse material nodes rather than duplicating them — this improves linking and consistency across datasets.

More Examples
--------------

Detailed notebooks are available for common electrochemical materials:

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

