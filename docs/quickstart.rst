Quick Start
=====

.. _installation:

Installation
------------

To use PyFred, first install it using pip:

.. code-block:: console

   pip install pyfred

----------------

Usage
------------

.. code-block:: console

   from pyfred import FredClient

   fred = FredClient(api_key=<API_KEY>)

   debt_to_gdp_series = fred.get_series(series_id="GFDEGDQ188S")
   print(debt_to_gdp_series)

----------------


