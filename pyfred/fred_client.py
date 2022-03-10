
import os
import requests
import pandas as pd

from pyfred.ex import ApiKeyNotFound, FredItemNotFound


BASE_URL = "https://api.stlouisfed.org/fred"
FILE_TYPE = "json"
ROOT_CATEGORY_ID = 0


class FredClient(object):

    def __init__(self, api_key=None):
        api_key = api_key or os.environ.get("FRED_API_KEY")
        if not api_key:
            raise ApiKeyNotFound("Please provide an api key to FredClient or "
                                 "set FRED_API_KEY as an environment variable.")
        self._api_key = api_key

    def get(self, path, url_args={}):
        url_args["api_key"] = self._api_key
        url_args["file_type"] = FILE_TYPE
        args = "&".join([
            f"{key}={val}" for key, val in url_args.items() if val is not None
        ])
        url = f"{BASE_URL}/{path}?{args}"
        r = requests.get(url)
        # TODO: validate
        data = r.json()
        return data

    # --------------------------------------------------------------------------

    def get_category(self, category_id):
        data = self.get("category", url_args={"category_id": category_id})
        categories = data["categories"]
        if len(categories) == 0:
            raise FredItemNotFound(f"Category not found: {category_id}")
        return categories[0]

    def get_category_children(self, category_id):
        data = self.get("category/children",
                        url_args={"category_id": category_id})
        categories = data["categories"]
        return categories

    def get_root_categories(self):
        return self.get_category_children(category_id=ROOT_CATEGORY_ID)

    def get_category_seriess(self, category_id):
        data = self.get("category/series",
                        url_args={"category_id": category_id})
        seriess = data["seriess"]
        return seriess

