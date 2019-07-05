import mock
import unittest

from plantpredict.inverter import Inverter
from tests import plantpredict_unit_test_case


class TestInverter(plantpredict_unit_test_case.PlantPredictUnitTestCase):
    @mock.patch('plantpredict.plant_predict_entity.PlantPredictEntity.create')
    def test_create(self, mocked_create):
        self._make_mocked_api()
        inverter = Inverter(api=self.mocked_api)

        inverter.create()
        self.assertEqual(inverter.create_url_suffix, "/Inverter")
        self.assertTrue(mocked_create.called)

    @mock.patch('plantpredict.plant_predict_entity.PlantPredictEntity.delete')
    def test_delete(self, mocked_delete):
        self._make_mocked_api()
        inverter = Inverter(api=self.mocked_api, id=808)

        inverter.delete()
        self.assertEqual(inverter.delete_url_suffix, "/Inverter/808")
        self.assertTrue(mocked_delete.called)

    @mock.patch('plantpredict.plant_predict_entity.PlantPredictEntity.get')
    def test_get(self, mocked_get):
        self._make_mocked_api()
        inverter = Inverter(api=self.mocked_api, id=808)

        inverter.get()
        self.assertEqual(inverter.get_url_suffix, "/Inverter/808")
        self.assertTrue(mocked_get.called)

    @mock.patch('plantpredict.plant_predict_entity.PlantPredictEntity.update')
    def test_update(self, mocked_update):
        self._make_mocked_api()
        inverter = Inverter(api=self.mocked_api, id=808)

        inverter.update()
        self.assertEqual(inverter.update_url_suffix, "/Inverter")
        self.assertTrue(mocked_update.called)


if __name__ == '__main__':
    unittest.main()
