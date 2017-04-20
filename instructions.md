Data Engineering Intern Project
===============================

Welcome! Attached you will find a csv file containing records from various data
sources, each row representing one of these records containing the attributes
first_name, last_name, and source (”source_1”, “source_2”, “source_3”). Your
job here is to take the data and attempt to match records to each other across
sources on the names. Assume that the data is formatted inconsistently across
sources, but that any two entries within a source are distinct. You will need
to do some data cleaning and make assessments on what you can comfortably
assume are the same name i.e. consider the following scenario:


| first_name | last_name      |   source |
|------------|----------------|---------:|
| jeff       | oreilly        | source_1 |
| Jeff       | O'Reilly, M.D. | source_2 |
| J          | OREILLY        | source_3 |


You will want to employ a method that can attempt to make matches across all
three sources in similar situations, not just one that handles matching exact
matches across sources with case insensitivity, etc.

Requirements
------------
Please complete this project using Python (2.7 or 3 preferred). Return to us:
* A file or module containing python code which reads in the file and produces
* a file where your matches are easily identified. Additionally,
* a short writeup (can just be in plaintext) briefly analyzing your solution,
  addressing the points below is required.
* Provide runtime on your machine using the timeit utility and explain your
  approach to ensuring your program executed efficiently. You may also want
  to profile your code.
* You should include unit tests to demonstrate that your code can reliably
  make connections between sources as in the example given above. We recommend
  pytest, but you may use any testing framework you like.

Code
----
* We'd prefer clean code, breaking up short functions, objects, modules, etc
  where appropriate. No particular programming paradigm required so long as
  your code is concise and readable.
* Any outside library you use is fair game, so long as you provide an
  explanation for its use, and it can be downloaded from PyPI using pip.

Writeup
-------
* Explain the method you took for matching, and why you chose that approach.
* Discuss runtime and performance considerations.
* Please provide an explanation for any outside libraries you incorporated
  and why you chose them.