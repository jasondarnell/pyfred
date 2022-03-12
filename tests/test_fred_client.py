
import os
from unittest import TestCase
from unittest.mock import patch

from pyfred import FredClient
from pyfred.ex import ApiKeyNotFound

from .mock_response import get_mock_response, MOCK_CATEGORY_CHILDREN_RESP


MOCK_CATEGORY_ID = 1


class TestFredClientNoKey(TestCase):
    @patch.dict(os.environ, {"FRED_API_KEY": ""})
    def test_no_api_key_fails(self):
        with self.assertRaises(ApiKeyNotFound):
            FredClient()


@patch.dict(os.environ, {"FRED_API_KEY": "123"})
class TestFredClient(TestCase):

    @patch("requests.get", side_effect=get_mock_response)
    def test_get_categories(self, mock_requests_get):
        client = FredClient()
        res = client.get_category_children(category_id=MOCK_CATEGORY_ID)
        expected_length = len(MOCK_CATEGORY_CHILDREN_RESP["categories"])
        self.assertEqual(expected_length, len(res))
        mock_requests_get.assert_called_once()


    @patch("requests.get", side_effect=get_mock_response)
    def test_get_root_categories(self, mock_requests_get):
        client = FredClient()
        res = client.get_root_categories()
        expected_length = len(MOCK_CATEGORY_CHILDREN_RESP["categories"])
        self.assertEqual(expected_length, len(res))
        mock_requests_get.assert_called_once()
