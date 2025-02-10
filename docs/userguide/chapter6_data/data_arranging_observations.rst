Arranging Observations
======================

We can arrange data into files as key-value pairs, tables or arrays.


Key-Value Pairs
~~~~~~~~~~~~~~~
Observations are listed as key-value pairs, where each key uniquely identifies a property and has an associated value. Key-value pairs are preferred when we have few observations, and each observation reports many properties. 
::
    Observation 1
    external-temperature: 25
    internal-temperature: 25
    oxygen-pressure: 1.05
    hydrogen-pressure: 1.05
    humidity: 0.67
    current: 1.98
    voltage: 0.45
    cycle: 2

Tabular
~~~~~~~
Data is organized into rows and columns, where each row represents an observation, and each column represents a property. Tabular arrangements are preferred when we have many observations, each reporting few properties.  

+------------+------------+------------+-----------+
|            | Time       | Current    | Voltage   |
+------------+------------+------------+-----------+
| 1          | 0.00       | 1.00       | 3.00      |
+------------+------------+------------+-----------+
| 2          | 0.50       | 1.00       | 3.02      |
+------------+------------+------------+-----------+
| 3          | 1.00       | 1.00       | 3.07      |
+------------+------------+------------+-----------+
| 4          | 1.50       | 1.00       | 3.15      |
+------------+------------+------------+-----------+

Arrays
~~~~~~~
Observations are stored in indexed positions within one-dimensional or multi-dimensional arrays, enabling efficient mathematical operations on the data. Arrays are preferred when both the number of properties and observations are large, and we need to perform complex mathematical operations that require fast access and manipulation of values. For example, a black and white image can be represented by an array of n columns and m rows, where each cell holds the greyscale value of the image at a position in the x and w coordinates of a plane. Images in this format can be efficiently manipulated, for instance, to apply filters, manipulate contrasts, and compute histograms.