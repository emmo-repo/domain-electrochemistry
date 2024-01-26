Examples
========

Electrode
---------

.. code-block:: json
   :linenos:

   {
      "@context": "https://raw.githubusercontent.com/emmo-repo/domain-electrochemistry/master/context.json",
      "@type": ["Electrode", "Foil"],
      "hasActiveMaterial": {
         "@type": "Zinc"
      }, 
      "hasProperty": [
         {
            "@type": ["SpecificCapacity", "MeasuredProperty"],
            "hasNumericalPart": {
                  "@type": "Real",
                  "hasNumericalValue": 800
            },
            "hasMeasurementUnit": "emmo:MilliAmpereHourPerGram"
         }, 
         {
            "@type": ["Thickness", "ConventionalProperty"],
            "hasNumericalPart": {
                  "@type": "Real",
                  "hasNumericalValue": 250
            },
            "hasMeasurementUnit": "emmo:MicroMetre"
         }, 
         {
            "@type": ["Diameter", "MeasuredProperty"],
            "hasNumericalPart": {
                  "@type": "Real",
                  "hasNumericalValue": 2
            },
            "hasMeasurementUnit": "emmo:CentiMetre"
         }, 
         {
            "@type": ["Mass", "MeasuredProperty"],
            "hasNumericalPart": {
                  "@type": "Real",
                  "hasNumericalValue": 2.5
            },
            "hasMeasurementUnit": "emmo:Gram"
         }
      ]
   }

.. raw:: html
         
   <div style="position: relative; padding-top: 56.25%; height: 0;">
   <iframe src="https://json-ld.org/playground/#startTab=tab-table&json-ld=%7B%22%40context%22%3A%22https%3A%2F%2Fraw.githubusercontent.com%2Femmo-repo%2Fdomain-electrochemistry%2Fmaster%2Fcontext.json%22%2C%22%40type%22%3A%5B%22Electrode%22%2C%22Foil%22%5D%2C%22hasActiveMaterial%22%3A%7B%22%40type%22%3A%22Zinc%22%7D%2C%22hasProperty%22%3A%5B%7B%22%40type%22%3A%5B%22SpecificCapacity%22%2C%22MeasuredProperty%22%5D%2C%22hasNumericalPart%22%3A%7B%22%40type%22%3A%22Real%22%2C%22hasNumericalValue%22%3A800%7D%2C%22hasMeasurementUnit%22%3A%22emmo%3AMilliAmpereHourPerGram%22%7D%2C%7B%22%40type%22%3A%5B%22Thickness%22%2C%22ConventionalProperty%22%5D%2C%22hasNumericalPart%22%3A%7B%22%40type%22%3A%22Real%22%2C%22hasNumericalValue%22%3A250%7D%2C%22hasMeasurementUnit%22%3A%22emmo%3AMicroMetre%22%7D%2C%7B%22%40type%22%3A%5B%22Diameter%22%2C%22MeasuredProperty%22%5D%2C%22hasNumericalPart%22%3A%7B%22%40type%22%3A%22Real%22%2C%22hasNumericalValue%22%3A2%7D%2C%22hasMeasurementUnit%22%3A%22emmo%3ACentiMetre%22%7D%2C%7B%22%40type%22%3A%5B%22Mass%22%2C%22MeasuredProperty%22%5D%2C%22hasNumericalPart%22%3A%7B%22%40type%22%3A%22Real%22%2C%22hasNumericalValue%22%3A2.5%7D%2C%22hasMeasurementUnit%22%3A%22emmo%3AGram%22%7D%5D%7D" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" frameborder="0" allowfullscreen></iframe>
   </div>
   

