
from pprint import pprint
from pyfred import FredClient


def main():
    fred = FredClient()
    data = fred.get_root_categories()
    pprint(data)

    results = fred.get_category_children(category_id=10)
    pprint(results)

    print("")

    results = fred.get_category_children(category_id=104)
    pprint(results)

    seriess = fred.get_category_seriess(category_id=33735)
    pprint(seriess[0])

    series_id = seriess[0]["id"]

    data = fred.get_series_info(series_id=series_id)
    pprint(data)

    data = fred.get_series(series_id=series_id)
    pprint(data)



if __name__ == "__main__":
    main()