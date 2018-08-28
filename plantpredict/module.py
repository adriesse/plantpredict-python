import json
import requests
from plantpredict import settings
from plantpredict.plant_predict_entity import PlantPredictEntity
from plantpredict.utilities import convert_json, camel_to_snake, snake_to_camel
from plantpredict.error_handlers import handle_refused_connection, handle_error_response


class Module(PlantPredictEntity):
    """
    Module represents the model for a photovoltaic solar module (panel).

    The full contents of the Weather database entity (in JSON) can be found under
    "GET /Module/{Id}" in `the general PlantPredict API documentation
    <http://app.plantpredict.com/swagger/ui/index#!/Module/Weather_Get>`_.
    """
    def create(self):
        """
        POST /Module

        """
        self.create_url_suffix = "/Module"
        super(Module, self).create()

    def delete(self):
        """
        DELETE /Module/{Id}

        """
        self.delete_url_suffix = "/Module/{}".format(self.id)
        super(Module, self).delete()

    def get(self):
        """
        GET /Module/{Id}

        """
        self.get_url_suffix = "/Module/{}".format(self.id)
        super(Module, self).get()

    def update(self):
        """
        PUT /Module

        """
        self.update_url_suffix = "/Module/{}".format(self.id)
        super(Module, self).update()

    @handle_refused_connection
    @handle_error_response
    def generate_single_diode_parameters_default(self):
        """
        POST /Module/Generator/GenerateSingleDiodeParametersDefault

        first stab at required inputs from unit test....
        module.number_of_cells_in_series = 264
        module.cell_technology_type = cell_technology_type_enum.CDTE
        module.stc_max_power = 400.0
        module.stc_short_circuit_current = 2.51
        module.stc_open_circuit_voltage = 216.1
        module.stc_mpp_current = 2.27
        module.stc_mpp_voltage = 175.95
        module.reference_temperature = 25
        module.reference_irradiance = 1000

        #TODO need to verify and turn into documentation

        :return:
        :rtype:
        """
        response = requests.post(
            url=settings.BASE_URL + "/Module/Generator/GenerateSingleDiodeParametersDefault",
            headers={"Authorization": "Bearer " + settings.TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )
        # TODO can switch this back, Jesse fixed
        """r = convert_json(json.loads(response.content), camel_to_snake)
        self.__dict__.update({
            "shunt_resistance_at_stc": r["shunt_resistance_at_stc"],
            "dark_shunt_resistance": r["dark_shunt_resistance"],
            "series_resistance_at_stc": r["series_resistance_at_stc"],
            "recombination_parameter": r["recombination_parameter"],
            "diode_ideality_factor_at_stc": r["diode_ideality_factor_at_stc"],
            "saturation_current_at_stc": r["saturation_current_at_stc"],
            "linear_temp_dependence_on_gamma": r["linear_temp_dependence_on_gamma"]
        })"""

        self.__dict__.update(convert_json(json.loads(response.content), camel_to_snake))

        return response

    @handle_refused_connection
    @handle_error_response
    def generate_single_diode_parameters_advanced(self):
        """
        POST /Module/Generator/GenerateSingleDiodeParametersAdvanced

        :return:
        :rtype:
        """
        response = requests.post(
            url=settings.BASE_URL + "/Module/Generator/GenerateSingleDiodeParametersAdvanced",
            headers={"Authorization": "Bearer " + settings.TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )

        # TODO can switch this back, Jesse fixed
        """r = convert_json(json.loads(response.content), camel_to_snake)
        self.__dict__.update({
            "series_resistance_at_stc": r["series_resistance_at_stc"],
            "diode_ideality_factor_at_stc": r["diode_ideality_factor_at_stc"],
            "saturation_current_at_stc": r["saturation_current_at_stc"],
            "linear_temp_dependence_on_gamma": r["linear_temp_dependence_on_gamma"]
        })"""

        self.__dict__.update(convert_json(json.loads(response.content), camel_to_snake))

        return response

    @handle_refused_connection
    @handle_error_response
    def calculate_effective_irradiance_response(self):
        """
        POST /Module/Generator/CalculateEffectiveIrradianceResponse

        """
        return requests.post(
            url=settings.BASE_URL + "/Module/Generator/CalculateEffectiveIrradianceResponse",
            headers={"Authorization": "Bearer " + settings.TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )

    @handle_refused_connection
    @handle_error_response
    def optimize_series_resistance(self):
        """
        POST /Module/Generator/OptimizeSeriesResistance

        """
        response = requests.post(
            url=settings.BASE_URL + "/Module/Generator/OptimizeSeriesResistance",
            headers={"Authorization": "Bearer " + settings.TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )

        self.__dict__.update(convert_json(json.loads(response.content), camel_to_snake))

        return response

    @handle_refused_connection
    @handle_error_response
    def process_key_iv_points(self,  module_points):
        """
        POST /Module/Generator/ProcessKeyIVPoints

        :param module_points:
        :type module_points:

        :return:
        :rtype:
        """
        response = requests.post(
            url=settings.BASE_URL + "/Module/Generator/ProcessKeyIVPoints",
            headers={"Authorization": "Bearer " + settings.TOKEN},
            json=[convert_json(m, snake_to_camel) for m in module_points]
        )

        self.__dict__.update(convert_json(json.loads(response.content), camel_to_snake))

        return response

    @handle_refused_connection
    @handle_error_response
    def process_iv_curves(self, iv_curves):
        """
        POST /Module/Generator/ProcessIVCurves

        :param iv_curves:
        :type iv_curves:

        :return:
        :rtype
        """
        # TODO

    @handle_refused_connection
    @handle_error_response
    def generate_iv_curve(self):
        """
        POST /Module/Generator/GenerateIVCurve

        :return:
        :rtype:
        """
        return requests.post(
            url=settings.BASE_URL + "/Module/Generator/GenerateIVCurve",
            headers={"Authorization": "Bearer " + settings.TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )

    def init(self):
        """This class initializes with the attributes (with set to null) required to successfully create a new module
        via Module.create()."""

        super(Module, self).__init__()
