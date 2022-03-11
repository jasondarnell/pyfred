# PyFred

![example workflow](https://github.com/jasondarnell/pyfred/actions/workflows/tests.yml/badge.svg)

Python client for the St. Louis Federal Reserve FRED API for economic data.

**This project is in under development.**

## Installation

```pip install pyfred```

## Documentation

The official documentation is hosted on Read the Docs: [https://pyfredclient.readthedocs.io/en/stable](https://pyfredclient.readthedocs.io/en/stable).

## Usage

```
    from pyfred import FredClient
    
    fred = FredClient(api_key=<YOUR_API_KEY>)

    debt_to_gdp_series = fred.get_series(series_id="GFDEGDQ188S")
    print(debt_to_gdp_series)
```

## Links

 - FRED: [https://fred.stlouisfed.org/](https://fred.stlouisfed.org/)
 - FRED API Documentation: [https://fred.stlouisfed.org/docs/api/fred/](https://fred.stlouisfed.org/docs/api/fred/)
 - PyFred Documentation[https://pyfredclient.readthedocs.io/en/stable](https://pyfredclient.readthedocs.io/en/stable)

## License

[MIT](https://opensource.org/licenses/MIT)

Copyright (c) 2022-present, Jason Darnell