import json
import requests
import pandas
from operator import itemgetter
from itertools import groupby
from plantpredict.settings import BASE_URL, TOKEN
from plantpredict.plant_predict_entity import PlantPredictEntity
from plantpredict.utilities import convert_json, camel_to_snake, snake_to_camel
from plantpredict.error_handlers import handle_refused_connection, handle_error_response


class Module(PlantPredictEntity):
    """
    The Module entity models all of the characteristics of a photovoltaic solar module (panel).
    """
    def create(self):
        """
        **POST** */Module*

        Creates a new :py:mod:`plantpredict.Module` entity in the PlantPredict database using the attributes assigned to
        the local object instance. Automatically assigns the resulting :py:attr:`id` to the local object instance.
        See the minimum required attributes (below) necessary to successfully create a new
        :py:mod:`plantpredict.Module`. Note that the full scope of attributes is not limited to the minimum required set.

        .. container:: toggle

            .. container:: header

                **Required Attributes**

            .. container:: required_attributes

                .. csv-table:: Minimum required attributes for successful Module creation
                    :delim: ;
                    :header: Field, Type, Description
                    :stub-columns: 1

                    name; str; Name of module file
                    model; str; Model number/name of module (can be the same as :py:attr:`name`)
                    manufacturer; str; Module manufacturer
                    cell_technology_type; int; Represents the cell technology type (CdTe, poly c-Si PERC, etc). Use :py:mod:`plantpredict.enumerations.cell_technology_type_enum`.
                    pv_model; int; Represents the 1-diode model type (1-Diode, 1-Diode with recombination). Use :py:mod:`plantpredict.enumerations.pv_model_type_enum`.
                    stc_short_circuit_current; float; Must be between :py:data:`0.1` and :py:data:`100.0` - units :py:data:`[A]`.
                    stc_open_circuit_voltage; float; Must be between :py:data:`0.4` and :py:data:`1000.0` - units :py:data:`[V]`.
                    stc_mpp_current; float; Must be between :py:data:`0.1` and :py:data:`100.0` - units :py:data:`[A]`.
                    stc_mpp_voltage; float; Must be between :py:data:`0.4` and :py:data:`1000.0` - units :py:data:`[V]`.
                    saturation_current_at_stc; float; Must be between :py:data:`1e-13` and :py:data:`1e-6` - units :py:data:`[A]`.
                    diode_ideality_factor_at_stc; float; Must be between :py:data:`0.1` and :py:data:`5.0` - unitless.
                    exponential_dependency_on_shunt_resistance; float; Must be between :py:data:`1.0` and :py:data:`100.0` - unitless.
                    dark_shunt_resistance; float; Must be between :py:data:`100.0` and :py:data:`100000.0` - units :py:data:`[Ohms]`.
                    shunt_resistance_at_stc; float; Must be between :py:data:`0.0` and :py:data:`100000.0` - units :py:data:`[Ohms]`.
                    bandgap_voltage; float; Must be between :py:data:`0.5` and :py:data:`4.0` - units :py:data:`[V]`.
                    heat_absorption_coef_alpha_t; float; Must be between :py:data:`0.1` and :py:data:`1.0`.
                    reference_irradiance; float; Must be between :py:data:`400.0` and :py:data:`1361.0` - units [W/m :superscript:`2`].
                    built_in_voltage; float; Required only if :py:attr:`pv_model` is :py:data:`plantpredict.enumerations.pv_model_type_enum.ONE_DIODE_RECOMBINATION`. Must be between :py:data:`0.0` and :py:data:`3.0` - units :py:data:`[V]`.
                    recombination_parameter; float; Required only if :py:attr:`pv_model` is :py:data:`plantpredict.enumerations.pv_model_type_enum.ONE_DIODE_RECOMBINATION`. Must be between :py:data:`0.0` and :py:data:`30.0` - units :py:data:`[V]`

        .. container:: toggle

            .. container:: header

                **Example Code**

            .. container:: example_code

                First, import the plantpredict library and receive an authentication token in your
                Python session, as shown in Step 3 of :ref:`authentication_oauth2`. Then instantiate a local Module
                object.

                .. code-block:: python

                    new_module = plantpredict.Module()

                Populate the Module's require attributes by either directly assigning them...

                .. code-block:: python

                    m.model = "Test Module"
                    m.cell_technology_type = cell_technology_type_enum.CDTE
                    m.manufacturer = "Solar Company"
                    m.pv_model = pv_model_type_enum.ONE_DIODE_RECOMBINATION
                    m.stc_short_circuit_current = 2.54
                    m.stc_open_circuit_voltage = 219.2
                    m.stc_mpp_current = 2.355
                    m.stc_mpp_voltage = 182.55
                    m.saturation_current_at_stc = 2.415081e-12
                    m.diode_ideality_factor_at_stc = 1.17
                    m.exponential_dependency_on_shunt_resistance = 5.5
                    m.dark_shunt_resistance = 6400
                    m.shunt_resistance_at_stc = 6400
                    m.bandgap_voltage = 1.5
                    m.heat_absorption_coef_alpha_t = 0.9
                    m.reference_irradiance = 1000

                    # required for modules with recombination
                    m.built_in_voltage = 0.9
                    m.recombination_parameter = 0.9

                ...OR via dictionary assignment.

                .. code-block:: python

                    module.__dict__ = {
                        "model": "Test Module",
                        "cell_technology_type": cell_technology_type_enum.CDTE,
                        "manufacturer": "Solar Company",
                        "pv_model": pv_model_type_enum.ONE_DIODE_RECOMBINATION,
                        "stc_short_circuit_current": 2.54,
                        "stc_open_circuit_voltage": 219.2,
                        "stc_mpp_current": 2.355,
                        "stc_mpp_voltage": 182.55,
                        "saturation_current_at_stc": 2.415081e-12,
                        "diode_ideality_factor_at_stc": 1.17,
                        "exponential_dependency_on_shunt_resistance": 5.5,
                        "dark_shunt_resistance": 6400,
                        "shunt_resistance_at_stc": 6400,
                        "bandgap_voltage": 1.5,
                        "heat_absorption_coef_alpha_t": 0.9,
                        "reference_irradiance": 1000,
                        "built_in_voltage": 0.9,
                        "recombination_parameter": 0.9
                    }


                Create a new module in the PlantPredict database, and observe that the Module now has a unique database
                identifier.

                .. code-block:: python
                
                    module.create()

                    print module.id

        :return: A dictionary containing the module id.
        :rtype: dict
        """
        self.create_url_suffix = "/Module"

        # PlantPredict API requires 2 different fields for short circuit current to successfully create a Module.
        # this line of code streamlines Module creation by only requiring the user to define
        # "stc_short_circuit_current" (2018-09-21; things may have changed since then)
        self.short_circuit_current_at_stc = self.stc_short_circuit_current

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
        :py:mod:`plantpredict.Module` with a specified :py:attr:`id`, calling :py:meth:`plantpredict.Module.get()`,
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
