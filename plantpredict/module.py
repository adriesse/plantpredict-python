import json
import requests
from plantpredict import settings
from plantpredict.plant_predict_entity import PlantPredictEntity
from plantpredict.utilities import convert_json, camel_to_snake, snake_to_camel, decorate_all_methods
from plantpredict.error_handlers import handle_refused_connection, handle_error_response


@decorate_all_methods(handle_refused_connection)
@decorate_all_methods(handle_error_response)
class Module(PlantPredictEntity):
    """
    """
    def create(self):
        """POST /Module"""
        self.create_url_suffix = "/Module"
        super(Module, self).create()

    def delete(self):
        """DELETE /Module/{Id}"""
        self.delete_url_suffix = "/Module/{}".format(self.id)
        super(Module, self).delete()

    def get(self):
        """GET /Module/{Id}"""
        self.get_url_suffix = "/Module/{}".format(self.id)
        super(Module, self).get()

    def update(self):
        """PUT /Module"""
        self.update_url_suffix = "/Module/{}".format(self.id)
        super(Module, self).update()

    def get_all_modules(self):
        """GET /Module"""
        """"""

    def generate_single_diode_parameters_advanced(self):
        """POST /Module/Generator/GenerateSingleDiodeParametersAdvanced"""

        response = requests.post(
            url=settings.BASE_URL + "/Module/Generator/GenerateSingleDiodeParametersAdvanced",
            headers={"Authorization": "Bearer " + settings.TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )

        self.__dict__.update(convert_json(json.loads(response.content), camel_to_snake))

        return response

    def process_key_iv_points(self,  module_points):
        """POST /Module/Generator/ProcessKeyIVPoints"""

        response = requests.post(
            url=settings.BASE_URL + "/Module/Generator/ProcessKeyIVPoints",
            headers={"Authorization": "Bearer " + settings.TOKEN},
            json=[convert_json(m, snake_to_camel) for m in module_points]
        )

        self.__dict__.update(convert_json(json.loads(response.content), camel_to_snake))

        return response

    def calculate_effective_irradiance_response(self):
        """POST /Module/Generator/CalculateEffectiveIrradianceResponse"""

        response = requests.post(
            url=settings.BASE_URL + "/Module/Generator/CalculateEffectiveIrradianceResponse",
            headers={"Authorization": "Bearer " + settings.TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )

        return [convert_json(eir, camel_to_snake) for eir in json.loads(response.content)]

    def optimize_series_resistance(self):
        """POST /Module/Generator/OptimizeSeriesResistance"""

        response = requests.post(
            url=settings.BASE_URL + "/Module/Generator/OptimizeSeriesResistance",
            headers={"Authorization": "Bearer " + settings.TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )

        self.__dict__.update(convert_json(json.loads(response.content), camel_to_snake))

    def init(self):
        """This class initializes with the attributes (with set to null) required to successfully create a new module
        via Module.create()."""

        super(Module, self).__init__()
        self.__dict__.update({
            "model": "",
            "manufacturer": "",
            "length": 0,
            "width": 0,
            "stc_short_circuit_current": 0,
            "stc_open_circuit_voltage": 0,
            "stc_mpp_current": 0,
            "stc_mpp_voltage": 0,
            "stc_max_power": 0,
            "stc_power_temp_coef": 0,
            "stc_short_circuit_current_temp_coef": 0,
            "stc_open_circuit_voltage_temp_coef": 0,
            "stc_efficiency": 0,
            "cell_technology_type": 0,
            "construction_type": 0,
            "light_induced_degradation": 0,
            "module_quality": 0,
            "module_mismatch_coefficient": 0,
            "heat_balance_convective_coef": 0,
            "heat_balance_conductive_coef": 0,
            "sandia_conductive_coef": 0,
            "sandia_convective_coef": 0,
            "cell_to_module_temp_diff": 0,
            "saturation_current_at_stc": 0,
            "series_resistance_at_stc": 0,
            "shunt_resistance_at_stc": 0,
            "diode_ideality_factor_at_stc": 0,
            "exponential_dependency_on_shunt_resistance": 0,
            "dark_shunt_resistance": 0,
            "linear_temp_dependence_on_gamma": 0,
            "short_circuit_current_at_stc": 0,
            "recombination_parameter": 0,
            "built_in_voltage": 0,
            "bandgap_voltage": 0,
            "linear_temp_dependence_on_isc": 0,
            "heat_absorption_coef_alpha_t": 0,
            "reference_irradiance": 0,
            "reference_temperature": 0,
            "spectral_response": 0,
            "pv_model": 0,
            "ashrae_iam_b0": 0,
            "linear_degradation_rate": 0,
        })
