import json
import requests
import pandas
from operator import itemgetter
from itertools import groupby
from plantpredict.settings import BASE_URL, TOKEN
from plantpredict.plant_predict_entity import PlantPredictEntity
from plantpredict.utilities import convert_json, camel_to_snake, snake_to_camel, decorate_all_methods
from plantpredict.error_handlers import handle_refused_connection, handle_error_response


@decorate_all_methods(handle_refused_connection)
@decorate_all_methods(handle_error_response)
class Module(PlantPredictEntity):
    """
    The Module entity models all of the characteristics of a photovoltaic solar module (panel).
    """
    def create(self):
        """
        **POST** */Module*

        Creates a new :py:mod:`plantpredict.Module` entity in the PlantPredict database and automatically assigns
        the resulting :py:attr:`id` to the local object instance.

        :return: A dictionary containing the module id.
        :rtype: dict
        """
        self.create_url_suffix = "/Module"
        super(Module, self).create()

    def delete(self):
        """
        **DELETE** */Module/(int:self.id)*

        Deletes an existing :py:mod:`plantpredict.Module` entity in the PlantPredict database according to the
        :py:attr:`id` of the local object instance.

        :return: A dictionary {"is_successful": True}.
        :rtype: dict
        """
        self.delete_url_suffix = "/Module/{}".format(self.id)
        super(Module, self).delete()

    def get(self):
        """
        **GET** */Module/(int:self.id)*

        Retrieves an existing :py:mod:`plantpredict.Module` entity from the PlantPredict database according to the
        :py:attr:`id` of the local object instance, and automatically assigns all of its attributes to the local object
        instance.

        :return: A dictionary containing all of the retrieved Module attributes.
        :rtype: dict
        """
        self.get_url_suffix = "/Module/{}".format(self.id)
        super(Module, self).get()

    def update(self):
        """
        **PUT** */Module*

        Updates an existing :py:mod:`plantpredict.Module` entity in PlantPredict using the full attributes of the local
        object instance. Calling this method is most commonly preceded by instantiating a local instance of
        :py:mod:`plantpredict.Module` with a specified :py:atrr:`id`, calling :py:meth:`plantpredict.Module.get()`,
        and changing any attributes locally.

        :return: A dictionary {"is_successful": True}.
        :rtype: dict
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
            url=BASE_URL + "/Module/Generator/GenerateSingleDiodeParametersDefault",
            headers={"Authorization": "Bearer " + TOKEN},
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
            url=BASE_URL + "/Module/Generator/GenerateSingleDiodeParametersAdvanced",
            headers={"Authorization": "Bearer " + TOKEN},
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
            url=BASE_URL + "/Module/Generator/CalculateEffectiveIrradianceResponse",
            headers={"Authorization": "Bearer " + TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )

    @handle_refused_connection
    @handle_error_response
    def optimize_series_resistance(self):
        """
        POST /Module/Generator/OptimizeSeriesResistance
        """
        response = requests.post(
            url=BASE_URL + "/Module/Generator/OptimizeSeriesResistance",
            headers={"Authorization": "Bearer " + TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )

        self.__dict__.update(convert_json(json.loads(response.content), camel_to_snake))

        return response

    @staticmethod
    def _parse_key_iv_points_template(file_path, sheet_name=None):
        """
        Locally parses the PlantPredict standard template for Key IV Points input and returns a JSON-serializable
        data structure.
        :param file_path:
        :return:
        """
        xl = pandas.ExcelFile(file_path)
        sheet_idx = 0 if not sheet_name else xl.sheet_names.index(sheet_name)
        xls_data = xl.parse(xl.sheet_names[sheet_idx], index_col=None).to_dict('records')

        key_iv_points_data = []
        for d in xls_data:
            key_iv_points_data.append({
                "temperature": d["Temperature [deg-C]"],
                "irradiance": d["Irradiance [W/m2]"],
                "short_circuit_current": d["Isc [A]"],
                "mpp_current": d["Imp [A]"],
                "open_circuit_voltage": d["Voc [V]"],
                "mpp_voltage": d["Vmp [V]"],
                "max_power": d["Pmp [W]"],
            })

        return key_iv_points_data

    @handle_refused_connection
    @handle_error_response
    def process_key_iv_points(self, file_path=None, key_iv_points_data=None):
        """
        POST /Module/Generator/ProcessKeyIVPoints
        :param file_path: File path to the .xlsx template for Key IV Points
        :type file_path: str
        :param key_iv_points_data:
        :type key_iv_points_data: dict
        :return:
        :rtype:
        """
        # if the input is the .xlsx template, parse it
        if not file_path and not key_iv_points_data:
            raise ValueError(
                "Either a file path to the .xslx template for Key IV Points input or the properly formatted " 
                "JSON-serializable data structure for Key IV Points input must be assigned as input. See the Python "
                "SDK documentation (https://plantpredict-python.readthedocs.io/en/latest/) for more information."
            )
        elif file_path and key_iv_points_data:
            raise ValueError(
                "Only one input option may be specified."
            )

        # if the user specifies a file_path to the .xlsx template, parse it
        elif file_path:
            key_iv_points_data = self._parse_key_iv_points_template(file_path)

        response = requests.post(
            url=BASE_URL + "/Module/Generator/ProcessKeyIVPoints",
            headers={"Authorization": "Bearer " + TOKEN},
            json=[convert_json(d, snake_to_camel) for d in key_iv_points_data]
        )

        self.__dict__.update(convert_json(json.loads(response.content), camel_to_snake))

        return response

    @staticmethod
    def _parse_full_iv_curves_template(file_path, sheet_name=None):
        """
        Locally parses the PlantPredict standard template for Full IV Curves input and returns a JSON-serializable
        data structure.
        :param file_path:
        :return:
        """
        xl = pandas.ExcelFile(file_path)
        sheet_idx = 0 if not sheet_name else xl.sheet_names.index(sheet_name)
        xls_data = xl.parse(xl.sheet_names[sheet_idx], index_col=None).to_dict('records')

        grouper = itemgetter("Temperature [deg-C]", "Irradiance [W/m2]")
        full_iv_curves_data = []
        for key, grp in groupby(sorted(xls_data, key=grouper), grouper):
            temp_dict = dict(zip(["Temperature [deg-C]", "Irradiance [W/m2]"], key))

            iv_points = [(item["I [A]"], item["[V]"]) for item in grp]
            full_iv_curves_data.append({
                "temperature": temp_dict["Temperature [deg-C]"],
                "irradiance": temp_dict["Irradiance [W/m2]"],
                "data_points": [{"current": iv[0], "voltage": iv[1]} for iv in iv_points]
            })

        return full_iv_curves_data

    @handle_refused_connection
    @handle_error_response
    def process_iv_curves(self, file_path=None, full_iv_curve_data=None):
        """
        POST /Module/Generator/ProcessIVCurves
        :param file_path: File path to the .xlsx template for Full IV Curves
        :type file_path: str
        :param full_iv_curve_data:
        :type full_iv_curve_data: dict
        :return:
        :rtype:
        """
        # if the input is the .xlsx template, parse it
        if not file_path and not full_iv_curve_data:
            raise ValueError(
                "Either a file path to the .xslx template for Full IV Curves input or the properly formatted " 
                "JSON-serializable data structure for Key IV Points input must be assigned as input. See the Python "
                "SDK documentation (https://plantpredict-python.readthedocs.io/en/latest/) for more information."
            )
        elif file_path and full_iv_curve_data:
            raise ValueError(
                "Only one input option may be specified."
            )

        # if the user specifies a file_path to the .xlsx template, parse it
        elif file_path:
            full_iv_curve_data = self._parse_full_iv_curves_template(file_path)

        response = requests.post(
            url=BASE_URL + "/Module/Generator/ProcessIVCurves",
            headers={"Authorization": "Bearer " + TOKEN},
            json=[convert_json(d, snake_to_camel) for d in full_iv_curve_data]
        )

        return [convert_json(d, camel_to_snake) for d in json.loads(response.content)]

    @handle_refused_connection
    @handle_error_response
    def generate_iv_curve(self, num_iv_points=100):
        """
        POST /Module/Generator/GenerateIVCurve
        :return:
        :rtype:
        """
        self.num_iv_points = num_iv_points

        return requests.post(
            url=BASE_URL + "/Module/Generator/GenerateIVCurve",
            headers={"Authorization": "Bearer " + TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )
