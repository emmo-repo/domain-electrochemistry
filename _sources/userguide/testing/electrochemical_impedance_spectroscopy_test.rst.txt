Electrochemical Impedance Spectroscopy (EIS)
============================================

**EIS** measures the frequency-dependent response of an electrochemical system to a
small AC perturbation.  
It reveals information about **charge-transfer resistance**, **diffusion**, and
**electrode/electrolyte interfaces**.

Ontology Alignment
------------------
- Class: ``ElectrochemicalImpedanceSpectroscopy``
- Subclass of: ``ElectrochemicalTest``

Example
-------
.. code-block:: json

   {
     "@context": "https://w3id.org/emmo/domain/electrochemistry/context",
     "@type": "ElectrochemicalImpedanceSpectroscopy",
     "hasTestObject": { "@type": "BatteryCell" },
     "hasProperty": {
       "@type": "FrequencyRange",
       "hasNumericalPart": {
         "@type": "ArrayData",
         "hasNumberValue": [0.1, 100000]
       },
       "hasMeasurementUnit": "emmo:Hertz"
     },
     "hasResult": {
       "@type": "Dataset",
       "name": "EIS_Spectrum.csv",
       "encodingFormat": "text/csv",
       "variableMeasured": [
         "Frequency / Hz",
         "Impedance Real / Ohm",
         "Impedance Imaginary / Ohm"
       ]
     }
   }
