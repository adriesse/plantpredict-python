import json
import requests
import pandas
from operator import itemgetter
from itertools import groupby
import plantpredict
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
                    length; float; Long side of the module. Must be between :py:data:`0.0` and :py:data:`10000.0` - units :py:data:`[mm]`.
                    width; float; Short side of the module. Must be between :py:data:`0.0` and :py:data:`10000.0` - units :py:data:`[mm]`.
                    cell_technology_type; int; Represents the cell technology type (CdTe, poly c-Si PERC, etc). Use :py:mod:`plantpredict.enumerations.cell_technology_type_enum`.
                    pv_model; int; Represents the 1-diode model type (1-Diode, 1-Diode with recombination). Use :py:mod:`plantpredict.enumerations.pv_model_type_enum`.
                    construction_type; int; Represents the module construction (Glass-Glass, Glass-Backsheet). Use :py:mod:`plantpredict.enumerations.construction_type_enum`.
                    stc_short_circuit_current; float; Must be between :py:data:`0.1` and :py:data:`100.0` - units :py:data:`[A]`.
                    stc_open_circuit_voltage; float; Must be between :py:data:`0.4` and :py:data:`1000.0` - units :py:data:`[V]`.
                    stc_mpp_current; float; Must be between :py:data:`0.1` and :py:data:`100.0` - units :py:data:`[A]`.
                    stc_mpp_voltage; float; Must be between :py:data:`0.4` and :py:data:`1000.0` - units :py:data:`[V]`.
                    stc_power_temp_coef; float; Must be between :py:data:`-3.0` and :py:data:`3.0` - units :py:data:`[%/deg-C]`.
                    stc_short_circuit_current_temp_coef; float; Must be between :py:data:`-0.3` and :py:data:`2.0` - units :py:data:`[%/deg-C]`.
                    stc_open_circuit_voltage_temp_coef; float; Must be between :py:data:`-3.0` and :py:data:`3.0` - units :py:data:`[%/deg-C]`.
                    saturation_current_at_stc; float; Must be between :py:data:`1e-13` and :py:data:`1e-6` - units :py:data:`[A]`.
                    diode_ideality_factor_at_stc; float; Must be between :py:data:`0.1` and :py:data:`5.0` - unitless.
                    linear_temp_dependence_on_gamma; float; Must be between :py:data:`-3.0` and :py:data:`3.0` - units :py:data:`[%/deg-C]`.
                    exponential_dependency_on_shunt_resistance; float; Must be between :py:data:`1.0` and :py:data:`100.0` - unitless.
                    series_resistance_at_stc; float; Must be between - units :py:data:`[Ohms]`
                    dark_shunt_resistance; float; Must be between :py:data:`100.0` and :py:data:`100000.0` - units :py:data:`[Ohms]`.
                    shunt_resistance_at_stc; float; Must be between :py:data:`0.0` and :py:data:`100000.0` - units :py:data:`[Ohms]`.
                    bandgap_voltage; float; Must be between :py:data:`0.5` and :py:data:`4.0` - units :py:data:`[V]`.
                    heat_absorption_coef_alpha_t; float; Must be between :py:data:`0.1` and :py:data:`1.0`.
                    reference_irradiance; float; Must be between :py:data:`400.0` and :py:data:`1361.0` - units :py:data:`[W/m^2]`.
                    built_in_voltage; float; Required only if :py:attr:`pv_model` is :py:data:`plantpredict.enumerations.pv_model_type_enum.ONE_DIODE_RECOMBINATION`. Must be between :py:data:`0.0` and :py:data:`3.0` - units :py:data:`[V]`.
                    recombination_parameter; float; Required only if :py:attr:`pv_model` is :py:data:`plantpredict.enumerations.pv_model_type_enum.ONE_DIODE_RECOMBINATION`. Must be between :py:data:`0.0` and :py:data:`30.0` - units :py:data:`[V]`

        .. container:: toggle

            .. container:: header

                **Example Code**

            .. container:: example_code

                First, import the plantpredict library and receive an authentication plantpredict.settings.TOKEN in your
                Python session, as shown in Step 3 of :ref:`authentication_oauth2`. Then instantiate a local Module
                object.

                .. code-block:: python

                    module_to_create = plantpredict.Module()

                Populate the Module's require attributes by either directly assigning them...

                .. code-block:: python
                    from plantpredict.enumerations import cell_technology_type_enum, pv_model_type_enum, construction_type_enum_type

                    module_to_create.name = "Test Module"
                    module_to_create.model = "Test Module"
                    module_to_create.manufacturer = "Solar Company"
                    module_to_create.length = 2009
                    module_to_create.width = 1232
                    module_to_create.cell_technology_type = cell_technology_type_enum.CDTE
                    module_to_create.pv_model = pv_model_type_enum.ONE_DIODE_RECOMBINATION
                    module_to_create.construction_type = construction_type_enum.GLASS_GLASS
                    module_to_create.stc_short_circuit_current = 2.54
                    module_to_create.stc_open_circuit_voltage = 219.2
                    module_to_create.stc_mpp_current = 2.355
                    module_to_create.stc_mpp_voltage = 182.55
                    module_to_create.stc_power_temp_coef = -0.32
                    module_to_create.stc_short_circuit_current_temp_coef = 0.04
                    module_to_create.stc_open_circuit_voltage_temp_coef = -0.28
                    module_to_create.saturation_current_at_stc = 2.415081e-12
                    module_to_create.diode_ideality_factor_at_stc = 1.17
                    module_to_create.linear_temp_dependence_on_gamma = -0.08
                    module_to_create.exponential_dependency_on_shunt_resistance = 5.5
                    module_to_create.series_resistance_at_stc = 5.277
                    module_to_create.dark_shunt_resistance = 6400
                    module_to_create.shunt_resistance_at_stc = 6400
                    module_to_create.bandgap_voltage = 1.5
                    module_to_create.heat_absorption_coef_alpha_t = 0.9
                    module_to_create.reference_irradiance = 1000

                    # required for modules with recombination
                    module_to_create.built_in_voltage = 0.9
                    module_to_create.recombination_parameter = 0.9

                ...OR via dictionary assignment.

                .. code-block:: python

                    module_to_create.__dict__ = {
                        "name": "Test Module",
                        "model": "Test Module",
                        "manufacturer": "Solar Company",
                        "length": 2009,
                        "width": 1232,
                        "cell_technology_type": cell_technology_type_enum.CDTE,
                        "pv_model": pv_model_type_enum.ONE_DIODE_RECOMBINATION,
                        "construction_type": construction_type_enum.GLASS_GLASS,
                        "stc_short_circuit_current": 2.54,
                        "stc_open_circuit_voltage": 219.2,
                        "stc_mpp_current": 2.355,
                        "stc_mpp_voltage": 182.55,
                        "stc_power_temp_coef": -0.32,
                        "stc_short_circuit_current_temp_coef": 0.04,
                        "stc_open_circuit_voltage_temp_coef": -0.28,
                        "saturation_current_at_stc": 2.415081e-12,
                        "diode_ideality_factor_at_stc": 1.17,
                        "linear_temp_dependence_on_gamma": -0.08,
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

                    module_to_create.create()

                    print module.id

        :return: A dictionary containing the module id.
        :rtype: dict
        """
        self.create_url_suffix = "/Module"

        # PlantPredict API requires 2 different fields for short circuit current to successfully create a Module.
        # this line of code streamlines Module creation by only requiring the user to define
        # "stc_short_circuit_current" (2018-09-21; things may have changed since then)
        self.short_circuit_current_at_stc = self.stc_short_circuit_current
        self.linear_temp_dependence_on_isc = self.stc_short_circuit_current_temp_coef

        # if values that are simply calculated from required parameters are not specified, calculate them
        if self.area is 0:
            self.area = (self.length/1000.0)*(self.width/1000.0)
        if self.stc_efficiency is 0:
            self.stc_efficiency = self.stc_max_power / (self.area * 1000.0)

        super(Module, self).create()

    def delete(self):
        """
        **DELETE** */Module/* :py:attr:`id`

        Deletes an existing :py:mod:`plantpredict.Module` entity in the PlantPredict database according to the
        :py:attr:`id` of the local object instance.

        .. container:: toggle

            .. container:: header

                **Example Code**

            .. container:: example_code

                First, import the plantpredict library and receive an authentication plantpredict.settings.TOKEN in your
                Python session, as shown in Step 3 of :ref:`authentication_oauth2`. Then instantiate a local Module
                object with the :py:attr:`id` of the target Module in the PlantPredict database.

                .. code-block:: python

                    module_to_delete = plantpredict.Module(id=99999)

                Delete the Module.

                .. code-block:: python

                    module_to_delete.delete()

        :return: A dictionary {"is_successful": True}.
        :rtype: dict
        """
        self.delete_url_suffix = "/Module/{}".format(self.id)
        super(Module, self).delete()

    def get(self):
        """
        **GET** */Module/* :py:attr:`id`

        Retrieves an existing :py:mod:`plantpredict.Module` entity from the PlantPredict database according to the
        :py:attr:`id` of the local object instance, and automatically assigns all of its attributes to the local object
        instance.

        .. container:: toggle

            .. container:: header

                **Example Code**

            .. container:: example_code

                First, import the plantpredict library and receive an authentication plantpredict.settings.TOKEN in your
                Python session, as shown in Step 3 of :ref:`authentication_oauth2`. Then instantiate a local Module
                object with the :py:attr:`id` of the target module in the PlantPredict database.

                .. code-block:: python

                    module_to_get = plantpredict.Module(id=99999)

                Retrieve the Module from the PlantPredict database.

                .. code-block:: python

                    module_to_get.get()

                This will automatically assign all of that Module's attributes to the local object instance. All of the
                attributes are now readily accessible in the local Python session.

                .. code-block:: python

                    module_name = module_to_get.name
                    Isc = module_to_get.stc_short_circuit_current

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

        .. container:: toggle

            .. container:: header

                **Example Code**

            .. container:: example_code

                First, import the plantpredict library and receive an authentication plantpredict.settings.TOKEN in your
                Python session, as shown in Step 3 of :ref:`authentication_oauth2`. Then instantiate a local Module
                object with the :py:attr:`id` of the target module in the PlantPredict database.

                .. code-block:: python

                    module_to_update = plantpredict.Module(id=99999)

                Retrieve the Module from the PlantPredict database.

                .. code-block:: python

                    module_to_update.get()

                This will automatically assign all of that Module's attributes to the local object instance. Any/all
                of the attributes can now be modified locally.

                .. code-block:: python

                    module.name = "New Name"
                    module.shunt_resistance_at_stc = 8000

                Persist (update) the local changes to the PlantPredict database.

                .. code-block:: python

                    module.update()

        :return: A dictionary {"is_successful": True}.
        :rtype: dict
        """
        self.update_url_suffix = "/Module/{}".format(self.id)
        super(Module, self).update()

    @handle_refused_connection
    @handle_error_response
    def generate_single_diode_parameters_default(self):
        """
        **POST** */Module/Generator/GenerateSingleDiodeParametersDefault*

        Generates single-diode parameters from module electrical characteristics available on any standard
        manufacturers' module datasheet. Detailed documentation on the algorithm and assumptions can be found
        `here <https://plantpredict.com/algorithm/module-file-generator/#756-2>`_. An example of using this method in
        practice can be found in :ref:`example_usage`.

        .. container:: toggle

            .. container:: header

                **Required Attributes**

            .. container:: required_attributes

                .. csv-table:: Minimum required attributes
                    :delim: ;
                    :header: Field, Type, Description
                    :stub-columns: 1

                    cell_technology_type; int; Represents the cell technology type (CdTe, poly c-Si PERC, etc). Use :py:mod:`plantpredict.enumerations.cell_technology_type_enum`.
                    pv_model; int; Represents the 1-diode model type (1-Diode, 1-Diode with recombination). Use :py:mod:`plantpredict.enumerations.pv_model_type_enum`.
                    number_of_cells_in_series; int; Number of cells in one string of cells - unitless
                    reference_irradiance; float; Must be between :py:data:`400.0` and :py:data:`1361.0` - units :py:data:`[W/m^2]`.
                    reference_temperature; float; Must be between :py:data:`-20.0` and :py:data:`80.0` - units :py:data:`[deg-C]`.
                    stc_max_power; float; Must be between :py:data:`0.0` and :py:data:`1000.0` - units :py:data:`[W]`.
                    stc_short_circuit_current; float; Must be between :py:data:`0.1` and :py:data:`100.0` - units :py:data:`[A]`.
                    stc_open_circuit_voltage; float; Must be between :py:data:`0.4` and :py:data:`1000.0` - units :py:data:`[V]`.
                    stc_mpp_current; float; Must be between :py:data:`0.1` and :py:data:`100.0` - units :py:data:`[A]`.
                    stc_mpp_voltage; float; Must be between :py:data:`0.4` and :py:data:`1000.0` - units :py:data:`[V]`.
                    stc_power_temp_coef; float; Must be between :py:data:`-3.0` and :py:data:`3.0` - units :py:data:`[%/deg-C]`.
                    stc_short_circuit_current_temp_coef; float; Must be between :py:data:`-0.3` and :py:data:`2.0` - units :py:data:`[%/deg-C]`.

        .. container:: toggle

            .. container:: header

                **Generated Parameters**

            .. container:: generated_parameters

                .. csv-table:: Generated Parameters
                    :delim: ;
                    :header: Field, Type, Description
                    :stub-columns: 1

                    series_resistance_at_stc; float; units :py:data:`[Ohms]`
                    maximum_series_resistance; float; units :py:data:`[Ohms]`
                    recombination_parameter; float; units :py:data:`[V]`
                    maximum_recombination_parameter; float; units :py:data:`[V]`
                    shunt_resistance_at_stc; float; units :py:data:`[Ohms]`
                    exponential_dependency_on_shunt_resistance; float; unitless
                    dark_shunt_resistnace; float; units :py:data:`[Ohms]`
                    saturation_current_at_stc; float; units :py:data:`[A]`
                    diode_ideality_factor_at_stc; float; unitless
                    linear_temp_dependence_on_gamma; float; units :py:data:`[%/deg-C]`
                    light_generated_current; float; units :py:data:`[A]`
                    power_at_stc; float; Model Calculated maximum power - units :py:data:`[W]`

        :return: Dictionary mirroring local module object with newly generated parameters.
        :rtype: dict
        """
        response = requests.post(
            url=plantpredict.settings.BASE_URL + "/Module/Generator/GenerateSingleDiodeParametersDefault",
            headers={"Authorization": "Bearer " + plantpredict.settings.TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )

        self.__dict__.update(convert_json(json.loads(response.content), camel_to_snake))

        return response

    @handle_refused_connection
    @handle_error_response
    def generate_single_diode_parameters_advanced(self):
        """
        **POST** */Module/Generator/GenerateSingleDiodeParametersAdvanced*

        :return:
        :rtype:
        """
        response = requests.post(
            url=plantpredict.settings.BASE_URL + "/Module/Generator/GenerateSingleDiodeParametersAdvanced",
            headers={"Authorization": "Bearer " + plantpredict.settings.TOKEN},
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
        **POST** */Module/Generator/CalculateEffectiveIrradianceResponse*

        """
        return requests.post(
            url=plantpredict.settings.BASE_URL + "/Module/Generator/CalculateEffectiveIrradianceResponse",
            headers={"Authorization": "Bearer " + plantpredict.settings.TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )

    @handle_refused_connection
    @handle_error_response
    def optimize_series_resistance(self):
        """
        **POST** */Module/Generator/OptimizeSeriesResistance*

        """
        response = requests.post(
            url=plantpredict.settings.BASE_URL + "/Module/Generator/OptimizeSeriesResistance",
            headers={"Authorization": "Bearer " + plantpredict.settings.TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )

        self.__dict__.update(convert_json(json.loads(response.content), camel_to_snake))

        return response

    @staticmethod
    def _parse_key_iv_points_template(file_path, sheet_name=None):
        """
        Parses the PlantPredict standard template for Key IV Points input and returns a JSON-serializable
        data structure.

        :param file_path:
        :type file_path: str
        :param sheet_name:
        :type sheet_name: str
        :return:
        :rtype:
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
        **POST** */Module/Generator/ProcessKeyIVPoints*

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
            url=plantpredict.settings.BASE_URL + "/Module/Generator/ProcessKeyIVPoints",
            headers={"Authorization": "Bearer " + plantpredict.settings.TOKEN},
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
        :type file_path: str
        :param sheet_name:
        :type sheet_name: str
        :return:
        :rtype:
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
        **POST** */Module/Generator/ProcessIVCurves*

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
            url=plantpredict.settings.BASE_URL + "/Module/Generator/ProcessIVCurves",
            headers={"Authorization": "Bearer " + plantpredict.settings.TOKEN},
            json=[convert_json(d, snake_to_camel) for d in full_iv_curve_data]
        )

        return [convert_json(d, camel_to_snake) for d in json.loads(response.content)]

    @handle_refused_connection
    @handle_error_response
    def generate_iv_curve(self, num_iv_points=100):
        """
        POST /Module/Generator/GenerateIVCurve
        
        :param num_iv_points:
        :type num_iv_points: int
        :return:
        :rtype:
        """
        self.num_iv_points = num_iv_points

        return requests.post(
            url=plantpredict.settings.BASE_URL + "/Module/Generator/GenerateIVCurve",
            headers={"Authorization": "Bearer " + plantpredict.settings.TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )
