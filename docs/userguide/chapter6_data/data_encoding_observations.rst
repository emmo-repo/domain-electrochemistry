Encoding Observations
======================

An encoding is a method of how data is represented digitally into a file, for storage, processing and exchange. A single data arrangement might support multiple encodings, each optimized for a purpose. Encodings are typically expressed using a media type in `MIME format <https://www.iana.org/assignments/media-types/media-types.xhtml>`_, which is a string representing a type of digital media as defined by the Internet Assigned Numbers Authority `(IANA) <https://www.iana.org/>`_ :

* *Tabular encodings*. Csv files, parquet files, feather files, are all encodings of tabular data.
* *Key-value pair encodings*. JSON and YAML are examples encodings supporting the listing and nesting of key-value pairs.
* *Array encodings*. HDF5, numpy array files and csv files all support the encoding of arrays.
* *Hierarchical encodings*. Organize multiple datasets into a hierarchy, stored in a single file. Example HDF5, Excel sheets. Given that key-value encodings support nesting, JSON and YAML also support hierarchies of data.

.. list-table:: Common file types and extensions.
   :header-rows: 1

   * - Arrangement
     - File type
     - File extension
     - MIME encoding
   * - Tabular
     - CSV
     - .csv
     - text/csv
   * - Tabular
     - TSV
     - .txt, .tsv
     - text/tab-separated-values
   * - Tabular
     - Parquet
     - .parquet
     - application/octet-stream
   * - Tabular
     - Feather
     - .feather
     - application/vnd.apache.arrow.file
   * - Key-values, hierarchical
     - JSON
     - .json
     - application/json
   * - Key-values, hierarchical
     - YAML
     - .yml, .yaml
     - application/yaml
   * - Key-values, arrays, hierarchical
     - HDF5
     - .hdf, .h4, .hdf4, .he2, .h5, .hdf5, .he
     - application/x-hdf, application/x-hdf5
   * - Key-values, arrays, hierarchical
     - Excel
     - .xls, .xlsx
     - application/vnd.ms-excel

In summary, most electrochemical data can be arranged in either tables or key-value pairs, and multiple observations can be nested into hierarchies. Each type of arrangement supports several file encodings. In the following sections, we will present guidelines on how to semantically describe the most common file encodings used in electrochemistry.  

In the following sections we will show how to describe several file types along with examples.