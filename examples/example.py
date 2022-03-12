
from pprint import pprint
from pyfred import FredClient


def main():
    fred = FredClient()

    print("\nRoot categories:")
    data = fred.get_root_categories()
    pprint(data)

    print("\nCategory children:")
    results = fred.get_category_children(category_id=10)
    pprint(results)

    print("\nRelated categories:")
    related_cats = fred.get_related_categories(category_id=32073)
    pprint(related_cats)

    print("\nCategories seriess:")
    seriess = fred.get_category_seriess(category_id=33735)
    pprint(seriess[0])
    series_id = seriess[0]["id"]

    print("\nSeries info:")
    data = fred.get_series_info(series_id=series_id)
    pprint(data)

    print("\nSeries:")
    data = fred.get_series(series_id=series_id)
    pprint(data)



if __name__ == "__main__":
    main()