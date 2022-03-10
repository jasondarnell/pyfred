
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


    seriess = fred.get_series(category_id=33735)
    pprint(seriess[0])

if __name__ == "__main__":
    main()