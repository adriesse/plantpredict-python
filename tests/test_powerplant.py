import mock
import unittest

from tests import plantpredict_unit_test_case, mocked_requests
from plantpredict.powerplant import PowerPlant
from plantpredict.enumerations import TrackingTypeEnum, ModuleOrientationEnum


class TestPowerPlant(plantpredict_unit_test_case.PlantPredictUnitTestCase):

    @mock.patch('plantpredict.plant_predict_entity.PlantPredictEntity.create')
    def test_create(self, mocked_create):
        self._make_mocked_api()
        powerplant = PowerPlant(api=self.mocked_api, project_id=7, prediction_id=77)

        powerplant.create()
        self.assertEqual(powerplant.create_url_suffix, "/Project/7/Prediction/77/PowerPlant")
        self.assertTrue(mocked_create.called)
        self.assertEqual(powerplant.power_factor, 1.0)

    @mock.patch('plantpredict.plant_predict_entity.PlantPredictEntity.delete')
    def test_delete(self, mocked_delete):
        self._make_mocked_api()
        powerplant = PowerPlant(api=self.mocked_api, project_id=7, prediction_id=77)

        powerplant.delete()
        self.assertEqual(powerplant.delete_url_suffix, "/Project/7/Prediction/77/PowerPlant")
        self.assertTrue(mocked_delete.called)

    @mock.patch('plantpredict.plant_predict_entity.PlantPredictEntity.get')
    def test_get(self, mocked_get):
        self._make_mocked_api()
        powerplant = PowerPlant(api=self.mocked_api, project_id=7, prediction_id=77)

        powerplant.get()
        self.assertEqual(powerplant.get_url_suffix, "/Project/7/Prediction/77/PowerPlant")
        self.assertTrue(mocked_get.called)

    @mock.patch('plantpredict.plant_predict_entity.PlantPredictEntity.update')
    def test_update(self, mocked_update):
        self._make_mocked_api()
        powerplant = PowerPlant(api=self.mocked_api, project_id=7, prediction_id=77)

        powerplant.update()
        self.assertEqual(powerplant.update_url_suffix, "/Project/7/Prediction/77/PowerPlant")
        self.assertTrue(mocked_update.called)

    def _init_powerplant_structure(self):
        self.powerplant.blocks = [
            {"id": 1, "name": 1, "arrays": [
                {"id": 11, "name": 1, "inverters": [{"id": 111, "name": "A", "dc_fields": [{"id": 1111, "name": 1}]}]}
            ]}
        ]

    def test_clone_block(self):
        self._make_mocked_api()
        self.powerplant = PowerPlant(api=self.mocked_api, project_id=7, prediction_id=77)
        self._init_powerplant_structure()
        cloned_block = self.powerplant.clone_block(block_id_to_clone=1)

        self.assertIsNotNone(cloned_block)
        self.assertEqual(cloned_block, {"id": 1, "name": 2, "arrays": [
                {"id": 11, "name": 1, "inverters": [{"id": 111, "name": "A", "dc_fields": [{"id": 1111, "name": 1}]}]}
            ]})
        self.assertEqual(len(self.powerplant.blocks), 2)
        self.assertEqual(self.powerplant.blocks[-1], {"id": 1, "name": 2, "arrays": [
                {"id": 11, "name": 1, "inverters": [{"id": 111, "name": "A", "dc_fields": [{"id": 1111, "name": 1}]}]}
            ]})

    def test_add_first_block(self):
        self._make_mocked_api()
        self.powerplant = PowerPlant(api=self.mocked_api, project_id=7, prediction_id=77)
        block_name = self.powerplant.add_block()

        self.assertEqual(len(self.powerplant.blocks), 1)
        self.assertEqual(block_name, 1)
        self.assertEqual(self.powerplant.blocks[0], {
            "name": 1,
            "use_energization_date": False,
            "energization_date": "",
            "arrays": []
        })

    def test_add_block_to_existing_plant(self):
        self._make_mocked_api()
        self.powerplant = PowerPlant(api=self.mocked_api, project_id=7, prediction_id=77)
        self._init_powerplant_structure()
        block_name = self.powerplant.add_block()

        self.assertEqual(len(self.powerplant.blocks), 2)
        self.assertEqual(block_name, 2)
        self.assertEqual(self.powerplant.blocks[-1], {
            "name": 2,
            "use_energization_date": False,
            "energization_date": "",
            "arrays": []
        })

    def test_add_array(self):
        self._make_mocked_api()
        self.powerplant = PowerPlant(api=self.mocked_api, project_id=7, prediction_id=77)
        self._init_powerplant_structure()
        array_name = self.powerplant.add_array(block_name=1, description="testing")

        self.assertEqual(len(self.powerplant.blocks[0]["arrays"]), 2)
        self.assertEqual(array_name, 2)
        self.assertEqual(self.powerplant.blocks[0]["arrays"][1], {
            "name": 2,
            "repeater": 1,
            "ac_collection_loss": 1,
            "das_load": 800,
            "cooling_load": 0,
            "additional_losses": 0,
            "transformer_enabled": True,
            "match_total_inverter_kva": True,
            "transformer_high_side_voltage": 34.5,
            "transformer_no_load_loss": 0.2,
            "transformer_full_load_loss": 0.7,
            "inverters": [],
            "description": "testing"
        })

    def test_add_inverter(self):
        self._make_mocked_api()
        self.powerplant = PowerPlant(api=self.mocked_api, project_id=7, prediction_id=77)
        self._init_powerplant_structure()
        inverter_name = self.powerplant.add_inverter(block_name=1, array_name=1, inverter_id=123, setpoint_kw=800)

        self.assertEqual(len(self.powerplant.blocks[0]["arrays"][0]["inverters"]), 2)
        self.assertEqual(inverter_name, "B")
        self.assertEqual(self.powerplant.blocks[0]["arrays"][0]["inverters"][1], {
            "name": "B",
            "repeater": 1,
            "inverter_id": 123,
            "setpoint_kw": 800,
            "power_factor": 1.0,
            "dc_fields": []
        })

    @mock.patch('plantpredict.plant_predict_entity.requests.get', new=mocked_requests.mocked_requests_get)
    @mock.patch('plantpredict.project.requests.get', new=mocked_requests.mocked_requests_get)
    def test_add_dc_field(self):
        self._make_mocked_api()
        self.powerplant = PowerPlant(api=self.mocked_api, project_id=7, prediction_id=77)
        self._init_powerplant_structure()

        dc_field_name = self.powerplant.add_dc_field(
            block_name=1,
            array_name=1,
            inverter_name="A",
            module_id=123,
            ground_coverage_ratio=0.40,
            number_of_series_strings_wired_in_parallel=400,
            field_dc_power=800,
            tracking_type=TrackingTypeEnum.FIXED_TILT,
            modules_high=4,
            modules_wired_in_series=10,
            module_tilt=30
        )

        self.assertEqual(len(self.powerplant.blocks[0]["arrays"][0]["inverters"][0]["dc_fields"][0]), 2)
        self.assertEqual(dc_field_name, 2)
        self.assertEqual(self.powerplant.blocks[0]["arrays"][0]["inverters"][0]["dc_fields"][1], {
            "name": 2,
            "module_id": 123,
            "tracking_type": TrackingTypeEnum.FIXED_TILT,
            "module_azimuth": 180.0,
            "module_tilt": 30,
            "dc_field_backtracking_type": None,
            "minimum_tracking_limit_angle_d": -60.0,
            "maximum_tracking_limit_angle_d": 60.0,
            "modules_high": 4,
            "modules_wired_in_series": 10,
            "number_of_rows": 400,
            "modules_wide": 10,
            "module_orientation": ModuleOrientationEnum.LANDSCAPE,
            "lateral_intermodule_gap": 0.02,
            "vertical_intermodule_gap": 0.02,
            "collector_bandwidth": 4.859999999999999,
            "post_to_post_spacing": 12.149999999999999,
            "planned_module_rating": 120,
            "field_dc_power": 800,
            "number_of_series_strings_wired_in_parallel": 400,
            "array_based_shading": False,
            "sandia_conductive_coef": 30.7,
            "sandia_convective_coef": 0.0,
            "cell_to_module_temp_diff": 3.0,
            "heat_balance_conductive_coef": -3.47,
            "heat_balance_convective_coef": -0.0594,
            "module_mismatch_coefficient": 1.0,
            "module_quality": 1.0,
            "light_induced_degradation": 1.0,
            "tracker_load_loss": 0.0,
            "dc_wiring_loss_at_stc": 0.0,
            "dc_health": 0.0
        })

    @mock.patch('plantpredict.plant_predict_entity.requests.get', new=mocked_requests.mocked_requests_get)
    @mock.patch('plantpredict.project.requests.get', new=mocked_requests.mocked_requests_get)
    def test_add_dc_field_fails_on_fixed_tilt_no_module_tilt(self):
        self._make_mocked_api()
        self.powerplant = PowerPlant(api=self.mocked_api, project_id=7, prediction_id=77)
        self._init_powerplant_structure()

        with self.assertRaises(ValueError):
            self.powerplant.add_dc_field(
                block_name=1,
                array_name=1,
                inverter_name="A",
                module_id=123,
                ground_coverage_ratio=0.40,
                number_of_series_strings_wired_in_parallel=400,
                field_dc_power=800,
                tracking_type=TrackingTypeEnum.FIXED_TILT,
                modules_high=4,
                modules_wired_in_series=10
            )

    @mock.patch('plantpredict.plant_predict_entity.requests.get', new=mocked_requests.mocked_requests_get)
    @mock.patch('plantpredict.project.requests.get', new=mocked_requests.mocked_requests_get)
    def test_add_dc_field_fails_on_tracker_no_backtracking_type(self):
        self._make_mocked_api()
        self.powerplant = PowerPlant(api=self.mocked_api, project_id=7, prediction_id=77)
        self._init_powerplant_structure()

        with self.assertRaises(ValueError):
            self.powerplant.add_dc_field(
                block_name=1,
                array_name=1,
                inverter_name="A",
                module_id=123,
                ground_coverage_ratio=0.40,
                number_of_series_strings_wired_in_parallel=400,
                field_dc_power=800,
                tracking_type=TrackingTypeEnum.HORIZONTAL_TRACKER,
                modules_high=4,
                modules_wired_in_series=10
            )

    def test_calculate_collector_bandwidth(self):
        collector_bandwidth = PowerPlant.calculate_collector_bandwidth(
            module_length=2000,
            module_width=1200,
            module_orientation=ModuleOrientationEnum.LANDSCAPE,
            modules_high=4,
            vertical_intermodule_gap=0.02
        )
        self.assertAlmostEqual(collector_bandwidth, 4.86, 2)

    def test_calculate_post_to_post_spacing_from_gcr(self):
        post_to_post_spacing = PowerPlant.calculate_post_to_post_spacing_from_gcr(
            collector_bandwidth=4.859999,
            ground_coverage_ratio=0.40
        )
        self.assertAlmostEqual(post_to_post_spacing, 12.1499975)

    def test_calculate_field_dc_power(self):
        field_dc_power = PowerPlant.calculate_field_dc_power(
            dc_ac_ratio=1.20,
            inverter_setpoint=800
        )
        self.assertEqual(field_dc_power, 960.0)

    def test_calculate_number_of_series_strings_wired_in_parallel(self):
        n = PowerPlant.calculate_number_of_series_strings_wired_in_parallel(
            field_dc_power=800,
            planned_module_rating=120,
            modules_wired_in_series=10
        )
        self.assertAlmostEqual(n, 666.666666666)

    def test_init(self):
        self._make_mocked_api()
        self.powerplant = PowerPlant(api=self.mocked_api, project_id=7, prediction_id=77)

        self.assertEqual(self.powerplant.project_id, 7)
        self.assertEqual(self.powerplant.prediction_id, 77)
        self.assertIsNone(self.powerplant.power_factor)
        self.assertIsNone(self.powerplant.blocks)


if __name__ == '__main__':
    unittest.main()
