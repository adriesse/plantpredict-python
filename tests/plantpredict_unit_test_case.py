import unittest
import mock

from plantpredict.prediction import Prediction


class PlantPredictUnitTestCase(unittest.TestCase):
    def _mock_geo_with_all_methods_called(self):
        # created for mocking project.Project.get_location_attributes
        self.mocked_api.geo().country = "United States"
        self.mocked_api.geo().country_code = "US"
        self.mocked_api.geo().locality = "Morrison"
        self.mocked_api.geo().region = "North America"
        self.mocked_api.geo().state_province = "Colorado"
        self.mocked_api.geo().state_province_code = "CO"

    @mock.patch('plantpredict.api.Api')
    def _make_mocked_api(self, mocked_api):
        self.mocked_api = mocked_api()
        self.mocked_api.base_url = "https://api.plantpredict.com"
        self.mocked_api.access_token = 'dummy_token'

        self.mocked_api.prediction.return_value = Prediction(self.mocked_api)

        self._mock_geo_with_all_methods_called()


