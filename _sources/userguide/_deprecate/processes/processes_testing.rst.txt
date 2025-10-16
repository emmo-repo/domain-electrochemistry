Electrochemical Test
=================

What is an Electrochemical Test?
---------------

An **Electrochemical Test** is an experiment performed on an electrochemical device, component, or material with the aim to obtain some key performance characteristics.

In semantic data, we describe a test using a few key parts.

Basic Structure
---------------

Here are the most important properties you should include when describing a test:

- **`hasTestObject`**:  
  The thing being tested (e.g. a battery cell).

- **`hasTestEquipment`**:  
  The device used to perform the test (e.g. a battery cycler).

- **`hasOutput`**:  
  The result of the test, usually a dataset.

- **`hasTask`**:  
  The steps or actions that make up the test (e.g. charge, rest, discharge).

- **`precedes`**:  
  Used to show the order of the tasks.


Example
-------

.. code-block:: json

   {
     "@type": "ElectrochemicalTest",
     "hasTestObject": { "@id": "urn:uuid:cell-001" },
     "hasTestEquipment": { "@type": "BatteryCycler", "schema:manufacturer": "Arbin" },
     "hasOutput": { "@id": "urn:uuid:dataset-001" },
     "hasTask": [
       { "@id": "urn:uuid:step-1", "@type": "Charging" },
       { "@id": "urn:uuid:step-2", "@type": "Resting" },
       { "@id": "urn:uuid:step-3", "@type": "Discharging" }
     ]
   }

And the order of steps:

.. code-block:: json

   [
     { "@id": "urn:uuid:step-1", "precedes": "urn:uuid:step-2" },
     { "@id": "urn:uuid:step-2", "precedes": "urn:uuid:step-3" }
   ]

Summary
-------

To describe a test, just remember:

- What was tested (`hasTestObject`)
- What was used to test it (`hasTestEquipment`)
- What the result was (`hasOutput`)
- What steps were performed (`hasTask`)
- In what order (`precedes`)

That’s all you need to get started!
