
import os
import requests
import pandas as pd

from pyfred.ex import ApiKeyNotFound, FredItemNotFound


# API doc: https://fred.stlouisfed.org/docs/api/fred/


BASE_URL = "https://api.stlouisfed.org/fred"
FILE_TYPE = "json"
ROOT_CATEGORY_ID = 0
DEFAULT_LIMIT = 1000
DEFAULT_OFFSET = 0


class FredClient(object):

    def __init__(self, api_key=None):
        api_key = api_key or os.environ.get("FRED_API_KEY")
        if not api_key:
            raise ApiKeyNotFound("Please provide an api key to FredClient or "
                                 "set FRED_API_KEY as an environment variable.")
        self._api_key = api_key

    def _get(self, path, url_args={}):
        url_args["api_key"] = self._api_key
        url_args["file_type"] = FILE_TYPE
        args = "&".join([
            f"{key}={val}" for key, val in url_args.items() if val is not None
        ])
        url = f"{BASE_URL}/{path}?{args}"
        r = requests.get(url)
        # TODO: validate
        data = r.json()
        # print(f"\nURL: {url}")
        # print(data)
        # print("")
        return data

    # --------------------------------------------------------------------------
    # Categories

    def get_category(self, category_id):
        """Get a category.

        :param category_id: Category ID
        :type category_id: int
        :return: A dict with information about the category.
        :rtype: dict
        """

        data = self._get("category", url_args={"category_id": category_id})
        categories = data["categories"]
        if len(categories) == 0:
            raise FredItemNotFound(f"Category not found: {category_id}")
        return categories[0]

    def get_category_children(self, category_id, realtime_start=None,
                              realtime_end=None):
        """Get the child categories for a specified parent category.

        :param category_id: Category ID
        :type category_id: int
        :param realtime_start: YYYY-MM-DD formatted string
        :type realtime_start: string or None
        :param realtime_end: YYYY-MM-DD formatted string
        :type realtime_end: string or None
        :return: List of category dicts.
        :rtype: list
        """
        args = {
            "category_id": category_id,
            "realtime_start": realtime_start,
            "realtime_end": realtime_end
        }
        data = self._get("category/children", url_args=args)
        categories = data["categories"]
        return categories

    def get_root_categories(self):
        """Get the root categories.

        :return: List of root category dicts.
        :rtype: list
        """
        return self.get_category_children(category_id=ROOT_CATEGORY_ID)

    def get_related_categories(self, category_id, realtime_start=None,
                               realtime_end=None):
        """Get the related categories for a category.

        :param category_id: Category ID
        :type category_id: int
        :param realtime_start: YYYY-MM-DD formatted string
        :type realtime_start: string or None
        :param realtime_end: YYYY-MM-DD formatted string
        :type realtime_end: string or None
        :return: List of related category dicts
        :rtype: list
        """
        args = {
            "category_id": category_id,
            "realtime_start": realtime_start,
            "realtime_end": realtime_end
        }
        data = self._get("category/related", url_args=args)
        categories = data["categories"]
        return categories

    def get_category_series(self, category_id, realtime_start=None,
                            realtime_end=None, limit=DEFAULT_LIMIT,
                            offset=None, order_by=None,
                            sort_order=None, filter_variable=None,
                            filter_value=None, tag_names=[],
                            exclude_tag_names=[]):
        """Get the series in a category.

        :param category_id: Category ID
        :type category_id: int
        :param realtime_start: YYYY-MM-DD formatted string
        :type realtime_start: string or None
        :param realtime_end: YYYY-MM-DD formatted string
        :type realtime_end: string or None
        :param limit: The maximum number of results to return.
        :type limit: int, optional
        :param offset: Offset
        :type offset: int, optional
        :param order_by: Order results by values of the specified attribute.
        :type order_by: str, optional
        :param sort_order: Sort results is ascending or descending order for attribute values specified by order_by.
        :type sort_order: str, optional
        :param filter_variable: The attribute to filter results by.
        :type filter_variable: str, optional
        :param filter_value: The value of the filter_variable attribute to filter results by.
        :type filter_value: str, optional
        :param tag_names:  List of tag names that series match all of.
        :type tag_names: list of str, optional
        :param exclude_tag_names:  List of tag names that series match none of.
        :type exclude_tag_names: list of str, optional
        :return: List of series for the given category id.
        :rtype: list
        """
        args = {
            "category_id": category_id,
            "realtime_start": realtime_start,
            "realtime_end": realtime_end,
            "limit": limit,
            "offset": offset,
            "order_by": order_by,
            "sort_order": sort_order,
            "filter_variable": filter_variable,
            "filter_value": filter_value,
            "tag_names": ";".join(tag_names) or None,
            "exclude_tag_names": ";".join(exclude_tag_names) or None
        }
        data = self._get("category/series", url_args=args)
        return data["seriess"]


    # --------------------------------------------------------------------------
    # Releases

    # TODO

    # --------------------------------------------------------------------------
    # Series

    def get_series(self, series_id, realtime_start=None, realtime_end=None):
        """Get an economic data series.

        :param series_id: Series ID
        :type series_id: string
        :param realtime_start: YYYY-MM-DD formatted string
        :type realtime_start: string or None
        :param realtime_end: YYYY-MM-DD formatted string
        :type realtime_end: string or None
        :return: A dict with information about the series.
        :rtype: dict
        """
        args = {
            "series_id": series_id,
            "realtime_start": realtime_start,
            "realtime_end": realtime_end,
        }
        data = self._get("series", url_args=args)
        seriess = data["seriess"]
        if len(seriess) == 0:
            raise FredItemNotFound(f"Series not found: {seriess}")
        return seriess[0]

    def get_series_observations(self, series_id, realtime_start=None,
                                realtime_end=None, limit=DEFAULT_LIMIT,
                                offset=None, sort_order=None,
                                observation_start=None, observation_end=None,
                                units=None, frequency=None,
                                aggregation_method=None, output_type=None,
                                vintage_dates=None):
        """Get the observations or data values for an economic data series.


        :param series_id: Series ID
        :type series_id: string
        :param realtime_start: YYYY-MM-DD formatted string
        :type realtime_start: string or None
        :param realtime_end: YYYY-MM-DD formatted string
        :type realtime_end: string or None
        :param limit: The maximum number of results to return.
        :type limit: int, optional
        :param offset: Offset
        :type offset: int, optional
        :param sort_order: Sort results is ascending or descending observation_date order.
        :type sort_order: str, optional
        :param observation_start: The start of the observation period. YYYY-MM-DD formatted string.
        :type observation_start: str, optional
        :param observation_end: The end of the observation period. YYYY-MM-DD formatted string.
        :type observation_end: str, optional
        :param units: A key that indicates a data value transformation.
        :type units: str, optional
        :param frequency: A key that indicates a lower frequency to aggregate values to.
        :type frequency: str, optional
        :param aggregation_method: A key that indicates the aggregation method used for frequency aggregation.
        :type aggregation_method: str, optional
        :param output_type: An integer that indicates an output type.
        :type output_type: int, optional
        :return: A dict containing the observation values.
        :rtype: dict
        """

        args = {
            "series_id": series_id,
            "realtime_start": realtime_start,
            "realtime_end": realtime_end,
            "limit": limit,
            "offset": offset,
            "sort_order": sort_order,
            "observation_start": observation_start,
            "observation_end": observation_end,
            "units": units,
            "frequency": frequency,
            "aggregation_method": aggregation_method,
            "output_type": output_type,
            "vintage_dates": vintage_dates
        }
        data = self._get("series/observations", url_args=args)
        return data

    def get_series_observations_pd(self, series_id, realtime_start=None,
                                realtime_end=None, limit=DEFAULT_LIMIT,
                                offset=None, sort_order=None,
                                observation_start=None, observation_end=None,
                                units=None, frequency=None,
                                aggregation_method=None, output_type=None,
                                vintage_dates=None):
        """Get the observations or data values for an economic data series as a
        Pandas Series.


        :param series_id: Series ID
        :type series_id: string
        :param realtime_start: YYYY-MM-DD formatted string
        :type realtime_start: string or None
        :param realtime_end: YYYY-MM-DD formatted string
        :type realtime_end: string or None
        :param limit: The maximum number of results to return.
        :type limit: int, optional
        :param offset: Offset
        :type offset: int, optional
        :param sort_order: Sort results is ascending or descending observation_date order.
        :type sort_order: str, optional
        :param observation_start: The start of the observation period. YYYY-MM-DD formatted string.
        :type observation_start: str, optional
        :param observation_end: The end of the observation period. YYYY-MM-DD formatted string.
        :type observation_end: str, optional
        :param units: A key that indicates a data value transformation.
        :type units: str, optional
        :param frequency: A key that indicates a lower frequency to aggregate values to.
        :type frequency: str, optional
        :param aggregation_method: A key that indicates the aggregation method used for frequency aggregation.
        :type aggregation_method: str, optional
        :param output_type: An integer that indicates an output type.
        :type output_type: int, optional
        :return: A pandas Series for the Fred series.
        :rtype: pandas.Series
        """

        data = self.get_series_observations(
            series_id=series_id,
            realtime_start=realtime_start,
            realtime_end=realtime_end,
            limit=limit,
            offset=offset,
            sort_order=sort_order,
            observation_start=observation_start,
            observation_end=observation_end,
            units=units,
            frequency=frequency,
            aggregation_method=aggregation_method,
            output_type=output_type,
            vintage_dates=vintage_dates
        )
        index = []
        values = []
        for obs in data["observations"]:
            index.append(pd.to_datetime(obs["date"], format="%Y-%m-%d"))
            try:
                values.append(float(obs["value"]))
            except ValueError:
                values.append(float("NaN"))
        return pd.Series(values, index=index)

    # --------------------------------------------------------------------------
    # Sources

    # TODO

    # --------------------------------------------------------------------------
    # Tags

    # TODO

