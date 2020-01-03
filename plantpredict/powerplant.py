import copy

from plantpredict.plant_predict_entity import PlantPredictEntity
from plantpredict.error_handlers import handle_refused_connection, handle_error_response
from plantpredict.enumerations import ModuleOrientationEnum, TrackingTypeEnum


class PowerPlant(PlantPredictEntity):
    """
    Represents the hierarchical structure of a power plant in PlantPredict. There is a one-to-one relationship between a
    :py:class:`~plantpredict.powerplant.PowerPlant` and :py:class:`~plantpredict.prediction.Prediction`. It is linked to
    that prediction via the attributes :py:attr:`project_id` and :py:attr:`prediction_id`.

    All classes that inherit from :py:class:`~plantpredict.plant_predict_entity.PlantPredictEntity` follow the same
    general usage pattern. The core class methods (:py:class:`~plantpredict.powerplant.PowerPlant.get`,
    :py:class:`~plantpredict.powerplant.PowerPlant.create`, :py:class:`~plantpredict.powerplant.PowerPlant.update`, and
    :py:class:`~plantpredict.powerplant.PowerPlant.delete`) require that certain attributes be assigned to the instance
    of the class in order to run successfully, rather than requiring direct variable inputs to the method call itself.
    For methods beyond these four, the input requirements might be either attribute assignments or variable inputs to
    the method.

    .. container:: toggle

        .. container:: header

            **Power Plant Attributes & Structure**

        .. container:: powerplant

            .. csv-table:: Power Plant Top-Level Attributes
                :file: ../docs/_static/csv_tables/powerplant.csv
                :header-rows: 1
                :stub-columns: 1
                :widths: 20 5 75
                :align: center

            .. csv-table:: Contents of # TODO blocks is a list :py:attr:`blocks`
                :file: ../docs/_static/csv_tables/powerplant_blocks.csv
                :header-rows: 1
                :stub-columns: 1
                :widths: 20 5 75
                :align: center
    |
    """
    def create(self):
        """
        **POST** */Project/* :py:attr:`project_id` */Prediction/* :py:attr:`prediction_id` */PowerPlant*

        :return:
        """
        self.power_factor = 1.0

        self.create_url_suffix = "/Project/{}/Prediction/{}/PowerPlant".format(self.project_id, self.prediction_id)
        return super(PowerPlant, self).create()

    def delete(self):
        """
        **DELETE** */Project/* :py:attr:`project_id` */Prediction/* :py:attr:`prediction_id` */PowerPlant*

        :return:
        """
        self.delete_url_suffix = "/Project/{}/Prediction/{}/PowerPlant".format(self.project_id, self.prediction_id)
        super(PowerPlant, self).delete()

    def get(self):
        """
        **GET** */Project/* :py:attr:`project_id` */Prediction/* :py:attr:`prediction_id` */PowerPlant*

        :return:
        """
        self.get_url_suffix = "/Project/{}/Prediction/{}/PowerPlant".format(self.project_id, self.prediction_id)
        return super(PowerPlant, self).get()

    def update(self):
        """
        **PUT** */Project/* :py:attr:`project_id` */Prediction/* :py:attr:`prediction_id` */PowerPlant*

        :return:
        """
        self.update_url_suffix = "/Project/{}/Prediction/{}/PowerPlant".format(self.project_id, self.prediction_id)
        return super(PowerPlant, self).update()

    def add_transformer(self, rating, high_side_voltage, no_load_loss, full_load_loss, ordinal):
        """
        Add a transformer to model the system-level of a power plant.

        :param float rating: Transformer rating. Must be between :py:data:`0.1` and :py:data:`10000.0` - units
                             :py:data:`[MVA]`.
        :param float high_side_voltage: Transformer voltage. Must be between :py:data:`1.0` and :py:data:`1000.0` -
                                        units :py:data:`[kV]`.
        :param float no_load_loss: Transformer loss at no load. Must be between :py:data:`0.0` and :py:data:`10.0` -
                                   units :py:data:`[%]`.
        :param float full_load_loss: Transformer loss at full load. Must be between :py:data:`0.0` and :py:data:`10.0` -
                                     units :py:data:`[%]`.
        :param int ordinal: Order in sequence of :py:attr:`transformers` and :py:attr:`transmission_lines` where
                            :py:data:`1` represents the closest entity to the power plant/farthest entity from the
                            energy meter (1-indexed).
        """
        transformer = {
            "rating": rating,
            "high_side_voltage": high_side_voltage,
            "no_load_loss": no_load_loss,
            "full_load_loss": full_load_loss,
            "ordinal": ordinal
        }

        try:
            self.transformers.append(transformer)
        except AttributeError:
            self.transformers = [transformer]

    def add_transmission_line(self, length, resistance, number_of_conductors_per_phase, ordinal):
        """
        Add a transmission line to model the system-level of a power plant.

        :param float length: Length of transmission line. Must be between :py:data:`0.1` and :py:data:`100.0` - units
                     :py:data:`[km]`.
        :param float resistance: Transmission line resistivity (per 300m). Must be between :py:data:`0.001` and
                                 :py:data:`2` - units :py:data:`[Ohms/300m]`.
        :param int number_of_conductors_per_phase: Number of conductors per phase. Must be between :py:data:`1` and
                                                   :py:data:`10`.
        :param ordinal: Order in sequence of :py:attr:`transformers` and :py:attr:`transmission_lines` where
                        :py:data:`1` represents the closest entity to the power plant/farthest entity from the
                        energy meter (1-indexed).
        """
        transmission_line = {
            "length": length,
            "resistance": resistance,
            "number_of_conductors_per_phase": number_of_conductors_per_phase,
            "ordinal": ordinal
        }

        try:
            self.transmission_lines.append(transmission_line)
        except AttributeError:
            self.transmission_lines = [transmission_line]

    @handle_refused_connection
    @handle_error_response
    def clone_block(self, block_id_to_clone):
        """
        Clones (copies) an existing block and appends it to `self.blocks`.

        :param int block_id_to_clone: Unique identifier of the block. Accessible on a given block with key `id`.
        :return: Name of newly cloned block.
        :rtype: int
        """
        block_to_clone = [b for b in self.blocks if b['id'] == block_id_to_clone][0]
        block_copy = copy.deepcopy(block_to_clone)
        block_copy["name"] = len(self.blocks) + 1
        self.blocks.append(block_copy)
        self.update()

        return self.blocks[-1]["name"]

    @handle_refused_connection
    @handle_error_response
    def add_block(self, use_energization_date=False, energization_date=""):
        """
        Creates a new block and appends it to `self.blocks`. Block naming is sequential - for instance, if there are 2
        existing blocks with names `1` and `2` (accessible via key `name` on each block in list), the next block created
        by `add_block` will automatically have `name` equal to `3`. This method does not currently account for the
        situation in which an existing power plant has block named non-sequentially.

        :param bool use_energization_date: Enables use of energization date in power plant block. Defaults to `False`.
        :param str energization_date: Timestamp representing energization date of block. Uses format
                                      `2019-12-26T16:43:55.867Z` and defaults to an empty string.
        :return: Name of newly added block
        :rtype: int
        """
        block = {
            "name": 1 if not self.blocks else len(self.blocks) + 1,
            "use_energization_date": use_energization_date,
            "energization_date": energization_date,
            "arrays": []
        }

        # if blocks list does not exit, create new list instead of appending
        try:
            self.blocks.append(block)
        except AttributeError:
            self.blocks = [block]

        return self.blocks[-1]["name"]

    def _validate_block_name(self, block_name):
        """
        Checks that a given block name exists in power plant and raises `ValueError` if not.

        :param int block_name: Value for key `name` in a single item of list `self.blocks`.
        """
        if block_name not in [b['name'] for b in self.blocks]:
            raise ValueError("{} is not a valid block name in the existing power plant structure.".format(block_name))

    @handle_refused_connection
    @handle_error_response
    def add_array(self, block_name, transformer_enabled=True, match_total_inverter_kva=True,
                  transformer_kva_rating=None, repeater=1, ac_collection_loss=1, das_load=800, cooling_load=0.0,
                  additional_losses=0.0, transformer_high_side_voltage=34.5, transformer_no_load_loss=0.2,
                  transformer_full_load_loss=0.7, description=""):
        """
        Adds an array to the block specified by :py:attr:`block_name` on the local instance of
        :py:class:`~plantpredict.powerplant.PowerPlant`.

        :param int block_name:
        :param bool transformer_enabled:
        :param bool match_total_inverter_kva:
        :param float transformer_kva_rating: Only used if :py:data:`match_total_inverter_kva` is set to :py:data:`False`.
        :param int repeater:
        :param float ac_collection_loss: - units :py:data:`[%]`
        :param float das_load: - units :py:data:`[W]`
        :param float cooling_load: - units :py:data:`[W]`
        :param float additional_losses: Additional night time losses - units :py:data:`[W]`
        :param float transformer_high_side_voltage:
        :param float transformer_no_load_loss:
        :param float transformer_full_load_loss:
        :param float str description:
        :return: The name of the newly added array.
        :rtype: int
        """
        self._validate_block_name(block_name)

        array = {
            "name": len(self.blocks[block_name - 1]["arrays"]) + 1,
            "repeater": repeater,
            "ac_collection_loss": ac_collection_loss,
            "das_load": das_load,
            "cooling_load": cooling_load,
            "additional_losses": additional_losses,
            "transformer_enabled": transformer_enabled,
            "match_total_inverter_kva": match_total_inverter_kva,
            "transformer_high_side_voltage": transformer_high_side_voltage,
            "transformer_no_load_loss": transformer_no_load_loss,
            "transformer_full_load_loss": transformer_full_load_loss,
            "inverters": [],
            "description": description
        }
        if not match_total_inverter_kva:
            array.update({"transformer_kva_rating": transformer_kva_rating})

        self.blocks[block_name - 1]["arrays"].append(array)

        return self.blocks[block_name - 1]["arrays"][-1]["name"]

    @handle_refused_connection
    @handle_error_response
    def _get_inverter_power_rated(self, inverter_id):
        """

        :param inverter_id:
        :return:
        """
        inverter = self.api.inverter(id=inverter_id)
        inverter.get()

        return inverter.power_rated

    @handle_refused_connection
    @handle_error_response
    def get_inverter_kva_rating(self, inverter_id):
        """
        Gets the inverters kVA rating based on

        :param int inverter_id: Unique identifier of inverter in PlantPredict Inverter database to calculate kVa rating
                                for.
        :return: kVa rating #TODO units
        :rtype: float
        """
        project = self.api.project(id=self.project_id)
        project.get()
        prediction = self.api.prediction(id=self.prediction_id, project_id=self.project_id)
        prediction.get()
        ashrae = self.api.ashrae(
            latitude=project.latitude,
            longitude=project.longitude,
            station_name=prediction.ashrae_station
        )
        ashrae.get_station()

        inverter = self.api.inverter(id=inverter_id)
        response = inverter.get_kva(
            elevation=project.elevation,
            temperature=ashrae.cool_996,
            use_cooling_temp=self.use_cooling_temp
        )

        return response['kva']

    def _validate_array_name(self, block_name, array_name):
        """

        :param int block_name:
        :param int array_name:
        :return:
        :rtype
        """
        self._validate_block_name(block_name)

        if array_name not in [a['name'] for a in self.blocks[block_name - 1]['arrays']]:
            raise ValueError("{} is not a valid array name in block {}.".format(array_name, block_name))

    @handle_refused_connection
    @handle_error_response
    def add_inverter(self, block_name, array_name, inverter_id, setpoint_kw=None, power_factor=1.0, repeater=1,
                     kva_rating=0.0):
        """

        :param block_name:
        :param array_name:
        :param inverter_id:
        :param setpoint_kw:
        :param power_factor:
        :param repeater:
        :param kva_rating:
        :return:
        """
        self._validate_array_name(block_name, array_name)

        self.blocks[block_name - 1]["arrays"][array_name - 1]["inverters"].append({
            "name": chr(ord("A") + len(self.blocks[block_name - 1]["arrays"][array_name - 1]["inverters"])),
            "repeater": repeater,
            "inverter_id": inverter_id,
            "setpoint_kw": setpoint_kw if setpoint_kw else self._get_inverter_power_rated(inverter_id),
            "power_factor": power_factor,
            "dc_fields": [],
            "kva_rating": self.get_inverter_kva_rating(inverter_id) if self.use_cooling_temp else kva_rating
        })

        return self.blocks[block_name - 1]["arrays"][array_name - 1]["inverters"][-1]["name"]

    def get_default_module_azimuth_from_latitude(self):
        """
        Plant is oriented south if above equator. The convention is 0.0 for North-facing arrays.

        :return: Default azimuth, :py:data:`180.0` if latitude is above equator, otherwise :py:data:`0.0`.
        :rtype: float
        """
        p = self.api.project(id=self.project_id)
        p.get()
        azimuth = 180.0 if p.latitude >= 0.0 else 0.0

        return azimuth

    @staticmethod
    def calculate_collector_bandwidth(module_width, module_length, module_orientation, modules_high,
                                      vertical_intermodule_gap):
        """

        :param module_width:
        :param module_length:
        :param module_orientation:
        :param modules_high:
        :param vertical_intermodule_gap:
        :return:
        """
        module_bandwidth = module_width if module_orientation == ModuleOrientationEnum.LANDSCAPE else module_length

        return modules_high * module_bandwidth / 1000 + (modules_high - 1) * vertical_intermodule_gap

    @staticmethod
    def calculate_table_length(modules_wide, module_orientation, module_length, module_width, lateral_intermodule_gap):
        """

        :param modules_wide:
        :param module_orientation:
        :param module_length:
        :param module_width:
        :param lateral_intermodule_gap:
        :return:
        """
        module_dimension = module_length if module_orientation == ModuleOrientationEnum.LANDSCAPE else module_width
        table_length = modules_wide*module_dimension + lateral_intermodule_gap*(modules_wide - 1)

        return table_length

    @staticmethod
    def calculate_tables_per_row(field_dc_power, planned_module_rating, modules_high, modules_wide,
                                 tables_removed_for_pcs, number_of_rows):
        """

        :param field_dc_power:
        :param planned_module_rating:
        :param modules_high:
        :param modules_wide:
        :param tables_removed_for_pcs:
        :param number_of_rows:
        :return:
        """
        module_count = 1000*field_dc_power / planned_module_rating
        modules_per_table = modules_high * modules_wide            # note: only a frontend value
        total_tables = module_count / modules_per_table            # note: only a frontend value
        tables_per_row = (total_tables + tables_removed_for_pcs) / number_of_rows

        return tables_per_row

    @staticmethod
    def _calculate_dc_field_size_by_collector_bandwidth(number_of_rows, post_to_post_spacing, collector_bandwidth):
        """

        :param number_of_rows:
        :param post_to_post_spacing:
        :param collector_bandwidth:
        :return:
        """
        return post_to_post_spacing*(number_of_rows - 1) + collector_bandwidth

    @staticmethod
    def _calculate_dc_field_size_by_tables_per_row(tables_per_row, module_orientation, module_length, module_width,
                                                   lateral_intermodule_gap, modules_wide):
        """

        :param tables_per_row:
        :param module_orientation:
        :param module_length:
        :param module_width:
        :param lateral_intermodule_gap:
        :param modules_wide:
        :return:
        """
        module_size = module_length / 1000.0 if module_orientation == ModuleOrientationEnum.LANDSCAPE \
            else module_width / 1000.0

        return (modules_wide * tables_per_row * (module_size + lateral_intermodule_gap)) - lateral_intermodule_gap

    def _calculate_dc_field_length(self, tables_per_row, module_orientation, module_length, module_width,
                                   lateral_intermodule_gap, modules_wide, tracking_type, number_of_rows,
                                   post_to_post_spacing, collector_bandwidth):
        """

        :param tables_per_row:
        :param module_orientation:
        :param module_length:
        :param module_width:
        :param lateral_intermodule_gap:
        :param modules_wide:
        :param tracking_type:
        :param number_of_rows:
        :param post_to_post_spacing:
        :param collector_bandwidth:
        :return:
        """
        if tracking_type == TrackingTypeEnum.HORIZONTAL_TRACKER:
            return self._calculate_dc_field_size_by_tables_per_row(tables_per_row, module_orientation, module_length,
                                                                   module_width, lateral_intermodule_gap, modules_wide)

        return self._calculate_dc_field_size_by_collector_bandwidth(number_of_rows, post_to_post_spacing,
                                                                    collector_bandwidth)

    def _calculate_dc_field_width(self, tracking_type, number_of_rows, post_to_post_spacing, collector_bandwidth,
                                  tables_per_row, module_orientation, module_length, module_width,
                                  lateral_intermodule_gap, modules_wide):
        """

        :param tracking_type:
        :param number_of_rows:
        :param post_to_post_spacing:
        :param collector_bandwidth:
        :param tables_per_row:
        :param module_orientation:
        :param module_length:
        :param module_width:
        :param lateral_intermodule_gap:
        :param modules_wide:
        :return:
        """
        if tracking_type == TrackingTypeEnum.HORIZONTAL_TRACKER:
            return self._calculate_dc_field_size_by_collector_bandwidth(number_of_rows, post_to_post_spacing,
                                                                        collector_bandwidth)

        return self._calculate_dc_field_size_by_tables_per_row(tables_per_row, module_orientation, module_length,
                                                               module_width, lateral_intermodule_gap, modules_wide)

    @staticmethod
    def _validate_dc_field_sizing(field_dc_power, number_of_series_strings_wired_in_parallel, planned_module_rating,
                                  modules_wired_in_series):
        """

        :param field_dc_power:
        :param number_of_series_strings_wired_in_parallel:
        :param planned_module_rating:
        :param modules_wired_in_series:
        :return:
        """
        if (field_dc_power is not None) and (number_of_series_strings_wired_in_parallel is not None):
            raise ValueError("Both field_dc_power and number_of_series_strings_wired_in_parallel are not None. Only "
                             "one of these values can be specified (and the other will be calculated).")
        elif (field_dc_power is not None) and (number_of_series_strings_wired_in_parallel is None):
            number_of_series_strings_wired_in_parallel = 1000 * field_dc_power / \
                                                         (planned_module_rating * modules_wired_in_series)
        elif (number_of_series_strings_wired_in_parallel is not None) and (field_dc_power is None):
            field_dc_power = number_of_series_strings_wired_in_parallel * \
                             (planned_module_rating * modules_wired_in_series) / 1000.0
        else:
            raise ValueError("Both field_dc_power and number_of_series_strings_wired_in_parallel are None. One "
                             "of these variables must be specified, and the other will be calculated.")

        return field_dc_power, number_of_series_strings_wired_in_parallel

    @staticmethod
    def calculate_post_to_post_spacing_from_gcr(collector_bandwidth, ground_coverage_ratio):
        """

        :param collector_bandwidth:
        :param ground_coverage_ratio:
        :return:
        """
        return collector_bandwidth / ground_coverage_ratio

    @staticmethod
    def calculate_field_dc_power(dc_ac_ratio, inverter_setpoint):
        """

        :param dc_ac_ratio:
        :param inverter_setpoint:
        :return:
        """
        return dc_ac_ratio*inverter_setpoint

    @staticmethod
    def _validate_mounting_structure_parameters(tracking_type, module_tilt, tracking_backtracking_type):
        """

        :param tracking_type:
        :param module_tilt:
        :param tracking_backtracking_type:
        :return:
        """
        if (tracking_type == TrackingTypeEnum.FIXED_TILT) and not module_tilt:
            raise ValueError("The input module_tilt is required for a fixed tilt DC field.")
        elif (tracking_type == TrackingTypeEnum.HORIZONTAL_TRACKER) and (tracking_backtracking_type is None):
            raise ValueError("The input tracking_backtracking_type is required for a horizontal tracker DC field.")

    def _validate_inverter_name(self, block_name, array_name, inverter_name):
        """

        :param int block_name:
        :param int array_name:
        :param str inverter_name:
        :return:
        """
        self._validate_block_name(block_name)
        self._validate_array_name(block_name, array_name)

        if inverter_name not in [i['name'] for i in self.blocks[block_name - 1]['arrays'][array_name - 1]['inverters']]:
            raise ValueError(
                "'{}' is not a valid inverter name in array {} of block {}.".format(inverter_name, array_name,
                                                                                    block_name))

    @handle_refused_connection
    @handle_error_response
    def add_dc_field(self, block_name, array_name, inverter_name, module_id, tracking_type, modules_high,
                     modules_wired_in_series, post_to_post_spacing, number_of_rows=1, modules_wide=None,
                     field_dc_power=None, number_of_series_strings_wired_in_parallel=None, module_tilt=None,
                     seasonal_tilt=False, seasonal_tilt_monthly_factors=None, module_orientation=None,
                     module_azimuth=None, tracking_backtracking_type=None, minimum_tracking_limit_angle_d=-60.0,
                     maximum_tracking_limit_angle_d=60.0, lateral_intermodule_gap=0.02, vertical_intermodule_gap=0.02,
                     array_based_shading=False, table_to_table_spacing=0.0, tables_removed_for_pcs=0,
                     module_quality=None, module_mismatch_coefficient=None, light_induced_degradation=None,
                     dc_wiring_loss_at_stc=1.5, dc_health=1.0, heat_balance_conductive_coef=None,
                     heat_balance_convective_coef=None, sandia_conductive_coef=None, sandia_convective_coef=None,
                     cell_to_module_temp_diff=None, tracker_load_loss=0.0):
        """
        Adds a DC field to an inverter on the instance of :py:class:`~plantpredict.powerplant.PowerPlant`. Location in
        the plant hierarchy is specified :py:attr:`block_name`, :py:attr:`array_name`, and :py:attr:`inverter_name` in
        the inputs of this method. Note: Calling this method only helps construct the local object and does not update
        the power plant in PlantPredict. In order to persist this change, call
        :py:meth`~plantpredict.powerplant.PowerPlant.update` after constructing a complete power plant.

        :param int block_name: Name (1-indexed integer) corresponding to the block upon which the DC field should be
                               added. This value is returned for a new block when you create one with `add_block`.
        :param int array_name: Name (1-indexed integer) corresponding to the array upon which the DC field should be
                               added. This value is returned for a new array when you create one with `add_array`.
        :param str inverter_name: Name (letter) corresponding to the inverter upon which the DC
                                  field should be built. This value is returned for a new array when you create one
                                  with `add_inverter`.
        :param int module_id: Unique identifier of the module to be used in the DC field.
        :param int tracking_type: Represents the cell tracking type (Fixed Tilt, Tracking, etc) of the DC Field. Use
                                  :py:mod:`plantpredict.enumerations.TrackingTypeEnum`. The options are documented
                                  `here <https://plantpredict-python.readthedocs.io/en/latest/sdk_reference.html#plantpredict.enumerations.TrackingTypeEnum>`_.
        :param int modules_high: The number of "ranks" (the number of modules deep) for each table.
        :param int modules_wired_in_series: The number of modules electrically connected in series in a string.
        :param float post_to_post_spacing: Row spacing; must be between :py:data:`0.0` and :py:data:`50.0` - units
                                           :py:data:`[m]`.
        :param float number_of_rows: The total number of rows in the DC field. Defaults to 1 if not provided as a
                                     keyword argument.
        :param int modules_wide: The width of each table in terms of numbers of modules. Defaults to
                                 `modules_wired_in_series` if not provided as a keyword argument.
        :param float field_dc_power:
        :param float number_of_series_strings_wired_in_parallel:
        :param float module_tilt:
        :param bool seasonal_tilt:
        :param dict seasonal_tilt_monthly_factors:
        :param module_orientation:
        :param module_azimuth:
        :param tracking_backtracking_type:
        :param minimum_tracking_limit_angle_d:
        :param maximum_tracking_limit_angle_d:
        :param lateral_intermodule_gap:
        :param vertical_intermodule_gap:
        :param array_based_shading:
        :param table_to_table_spacing:
        :param tables_removed_for_pcs:
        :param module_quality:
        :param module_mismatch_coefficient:
        :param light_induced_degradation:
        :param dc_wiring_loss_at_stc:
        :param dc_health:
        :param heat_balance_conductive_coef:
        :param heat_balance_convective_coef:
        :param sandia_conductive_coef:
        :param sandia_convective_coef:
        :param cell_to_module_temp_diff:
        :param tracker_load_loss:
        :return:
        """
        # validate inputs
        self._validate_inverter_name(block_name=block_name, array_name=array_name, inverter_name=inverter_name)
        self._validate_mounting_structure_parameters(tracking_type, module_tilt, tracking_backtracking_type)

        # calculate parameters typically calculated in the UI
        m = self.api.module(id=module_id)
        m.get()
        field_dc_power, number_of_series_strings_wired_in_parallel = self._validate_dc_field_sizing(
            field_dc_power=field_dc_power,
            number_of_series_strings_wired_in_parallel=number_of_series_strings_wired_in_parallel,
            planned_module_rating=m.stc_max_power,
            modules_wired_in_series=modules_wired_in_series,
        )
        module_orientation = module_orientation if module_orientation is not None else m.default_orientation
        modules_wide = modules_wide if modules_wide is not None else modules_wired_in_series
        collector_bandwidth = self.calculate_collector_bandwidth(
            module_width=m.width,
            module_length=m.length,
            module_orientation=module_orientation,
            vertical_intermodule_gap=vertical_intermodule_gap,
            modules_high=modules_high
        )
        table_length = self.calculate_table_length(
            modules_wide=modules_wide,
            module_width=m.width,
            module_length=m.length,
            module_orientation=module_orientation,
            lateral_intermodule_gap=lateral_intermodule_gap
        )
        tables_per_row = self.calculate_tables_per_row(
            field_dc_power=field_dc_power,
            planned_module_rating=m.stc_max_power,
            modules_high=modules_high,
            modules_wide=modules_wide,
            tables_removed_for_pcs=tables_removed_for_pcs,
            number_of_rows=number_of_rows
        )
        self.blocks[block_name - 1]["arrays"][array_name - 1]["inverters"][ord(inverter_name) - 65]["dc_fields"].append({
            "name": len(
                self.blocks[block_name - 1]["arrays"][array_name - 1]["inverters"][ord(inverter_name) - 65]["dc_fields"]
            ) + 1,
            "module_id": module_id,
            "tracking_type": tracking_type,
            "module_tilt": module_tilt,
            "seasonal_tilt": seasonal_tilt,
            "seasonal_tilt_monthly_factors": seasonal_tilt_monthly_factors,
            "tracking_backtracking_type": tracking_backtracking_type,
            "minimum_tracking_limit_angle_d": minimum_tracking_limit_angle_d,
            "maximum_tracking_limit_angle_d": maximum_tracking_limit_angle_d,
            "module_orientation": module_orientation,
            "modules_high": modules_high,
            "module_azimuth": (module_azimuth if module_azimuth is not None
                               else self.get_default_module_azimuth_from_latitude()),
            "collector_bandwidth": collector_bandwidth,
            "post_to_post_spacing": post_to_post_spacing,
            # Electrical
            "planned_module_rating": m.stc_max_power,
            "modules_wired_in_series": modules_wired_in_series,
            "field_dc_power": field_dc_power,
            "number_of_series_strings_wired_in_parallel": number_of_series_strings_wired_in_parallel,
            "module_count": 1000*field_dc_power/m.stc_max_power,    # confirmed calculation in PlantPredict backend
            # Losses
            "module_quality": module_quality if module_quality is not None else m.module_quality,
            "module_mismatch_coefficient": (module_mismatch_coefficient if module_mismatch_coefficient is not None else
                                            m.module_mismatch_coefficient),
            "light_induced_degradation": (light_induced_degradation if light_induced_degradation is not None else
                                          m.light_induced_degradation),
            "dc_wiring_loss_at_stc": dc_wiring_loss_at_stc,
            "dc_health": dc_health,
            "heat_balance_conductive_coef": (heat_balance_conductive_coef if heat_balance_conductive_coef is not None
                                             else m.heat_balance_conductive_coef),
            "heat_balance_convective_coef": (heat_balance_convective_coef if heat_balance_convective_coef is not None
                                             else m.heat_balance_convective_coef),
            "sandia_conductive_coef": (sandia_conductive_coef if sandia_conductive_coef is not None
                                       else m.sandia_conductive_coef),
            "cell_to_module_temp_diff": (cell_to_module_temp_diff if cell_to_module_temp_diff is not None else
                                         m.cell_to_module_temp_diff),
            "sandia_convective_coef": (sandia_convective_coef if sandia_convective_coef is not None
                                       else m.sandia_convective_coef),
            "tracker_load_loss": tracker_load_loss,
            # Advanced Fields
            "lateral_intermodule_gap": lateral_intermodule_gap,
            "vertical_intermodule_gap": vertical_intermodule_gap,
            "modules_wide": modules_wide,
            "table_to_table_spacing": table_to_table_spacing,
            "array_based_shading": array_based_shading,
            "number_of_rows": number_of_rows,
            "table_length": table_length,
            "tables_per_row": tables_per_row,
            "tables_removed_for_pcs": tables_removed_for_pcs,
            "field_length": self._calculate_dc_field_length(tables_per_row, module_orientation, m.length, m.width,
                                                            lateral_intermodule_gap, modules_wide, tracking_type,
                                                            number_of_rows, post_to_post_spacing, collector_bandwidth),
            "field_width": self._calculate_dc_field_width(tracking_type, number_of_rows, post_to_post_spacing,
                                                          collector_bandwidth, tables_per_row, module_orientation,
                                                          m.length, m.width, lateral_intermodule_gap, modules_wide)
        })

        return self.blocks[
            block_name - 1]["arrays"][array_name - 1]["inverters"][ord(inverter_name) - 65]["dc_fields"][-1]["name"]

    def __init__(self, api, project_id=None, prediction_id=None, use_cooling_temp=True):
        self.project_id = project_id
        self.prediction_id = prediction_id
        self.use_cooling_temp = use_cooling_temp

        self.power_factor = None
        self.blocks = None
        self.transformers = None
        self.transmission_lines = None

        super(PowerPlant, self).__init__(api)
