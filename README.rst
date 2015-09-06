===========
Delete Old Data
===========

Deletes all data in an hourly partitioned hierarchy older than
some number of days.  <path> is the base location of the hourly
partitioned data.

Usage
-----
The client can be used directly from the command line (after installation)::

    delete-old-data --older-than-days 20 --dataset-name my_dataset


Installing
----------
To install the module from source::

    python setup.py install

Testing
-------
To run the unit tests::

    python setup.py test
