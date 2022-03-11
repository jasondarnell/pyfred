
import os
from unittest import TestCase
from unittest.mock import patch

from pyfred import FredClient
from pyfred.ex import ApiKeyNotFound

TEST_API_KEY = "123"

class TestFredClient(TestCase):

    @patch.dict(os.environ, {"FRED_API_KEY": ""})
    def test_no_api_key_fails(self):
        with self.assertRaises(ApiKeyNotFound):
            FredClient()