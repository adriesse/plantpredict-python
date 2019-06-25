import unittest
import mock


class PlantPredictTestCase(unittest.TestCase):
    def _make_mocked_api(self):
        self.mocked_api = mock.Mock()
        self.mocked_api.base_url = "https://api.plantpredict.com"
        self.mocked_api.access_token = 'dummy_token'
