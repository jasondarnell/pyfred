# PyFred

![Unit Tests](https://github.com/jasondarnell/pyfred/actions/workflows/tests.yml/badge.svg)

Python client for the St. Louis Federal Reserve FRED API for economic data.

PyFred is not endorsed or certified by the Federal Reserve Bank of St. Louis.

**This project is in under development.**

## Installation

```pip install pyfred```

## Documentation

The official documentation is hosted on Read the Docs: [https://pyfredclient.readthedocs.io/en/stable](https://pyfredclient.readthedocs.io/en/stable).

## Usage

### API Key

FRED requires an API key which is available for free [here](https://fredaccount.stlouisfed.org/apikey).

To set the API key as an environment variable:
```
$ export FRED_API_KEY=<your-api-key>
```

To set the API key using the FredClient constructor:
```
from pyfred import FredClient
fred = FredClient(api_key=<your-api-key>)
```

### Using FredClient

Create client
```
from pyfred import FredClient
fred = FredClient(api_key=<your-api-key>)
```

Get series observations as a Pandas series.
```
>>> fred.get_series_observations_pd(series_id="GFDEGDQ188S")
1966-01-01     40.33999
1966-04-01     39.26763
1966-07-01     39.62091
1966-10-01     39.51977
1967-01-01     39.20383
                ...    
2020-10-01    129.19415
2021-01-01    127.65351
2021-04-01    125.45397
2021-07-01    122.52606
2021-10-01    123.36152
Length: 224, dtype: float64
```

For a list of all FredClient methods, see [PyFred Read the Docs API](https://pyfredclient.readthedocs.io/en/stable/api.html).

## Links

 - FRED: [https://fred.stlouisfed.org/](https://fred.stlouisfed.org/)
 - FRED API Documentation: [https://fred.stlouisfed.org/docs/api/fred/](https://fred.stlouisfed.org/docs/api/fred/)
 - PyFred Documentation[https://pyfredclient.readthedocs.io/en/stable](https://pyfredclient.readthedocs.io/en/stable)

## License

[MIT](https://opensource.org/licenses/MIT)

Copyright (c) 2022-present, Jason Darnell