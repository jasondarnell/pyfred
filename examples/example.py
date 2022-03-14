
from pprint import pprint
from pyfred import FredClient


def main():
    fred = FredClient()

    print("\nget_root_categories:")
    data = fred.get_root_categories()
    pprint(data)

    print("\nget_category_children:")
    results = fred.get_category_children(category_id=10)
    pprint(results)


    print("\nget_related_categories:")
    related_cats = fred.get_related_categories(category_id=32073)
    pprint(related_cats)

    print("\nget_category_series (first one):")
    series = fred.get_category_series(category_id=33735)
    pprint(series[0])
    series_id = series[0]["id"]


    print("\nget_series:")
    data = fred.get_series(series_id=series_id)
    pprint(data)

    print("\nget_series_observations:")
    data = fred.get_series_observations(series_id=series_id)
    pprint(data)

    print("\nget_series_observations_pd:")
    data = fred.get_series_observations_pd(series_id=series_id)
    pprint(data)



if __name__ == "__main__":
    main()