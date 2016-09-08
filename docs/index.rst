.. Ini Handler documentation master file, created by
   sphinx-quickstart on Wed Sep  7 22:16:30 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Ini Handler's documentation!
=======================================

Contents:

.. toctree::
   :maxdepth: 2

   content/api.rst


Ini Handler is a simple and small Python library for reading and writing .ini
setting files.

Ini Handler makes implementing user customisable settings painless and simple. It
achieves this by limiting the number of methods you have to remember to be able to
do what you want to do.

For example::

   from ini_handler.vbini import Ini

   ini_file = Ini()
   ini_file['NewSetting'] = 'Simple!'

   print(ini_file['NewSetting'])

Output::

   'Simple!'

Just like that we have created and retrieved a new setting!


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
