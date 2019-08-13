import copy

from plantpredict.plant_predict_entity import PlantPredictEntity
from plantpredict.error_handlers import handle_refused_connection, handle_error_response
from plantpredict.enumerations import ModuleOrientationEnum, TrackingTypeEnum


class PowerPlant(PlantPredictEntity):
    """
    """
    def create(self, power_factor=1.0):
        """
        **POST** */Project/ :py:attr:`project_id` /Prediction/ :py:attr:`prediction_id` /PowerPlant*

        """
        self.create_url_suffix = "/Project/{}/Prediction/{}/PowerPlant".format(self.project_id, self.prediction_id)

        self.power_factor = power_factor

        return super(PowerPlant, self).create()

    def delete(self):
        """DELETE /Project/{ProjectId}/Prediction/{PredictionId}/PowerPlant"""
        self.delete_url_suffix = "/Project/{}/Prediction/{}/PowerPlant".format(self.project_id, self.prediction_id)
        super(PowerPlant, self).delete()

    def get(self):
        """"GET /Project/{ProjectId}/Prediction/{PredictionId}/PowerPlant"""
        self.get_url_suffix = "/Project/{}/Prediction/{}/PowerPlant".format(self.project_id, self.prediction_id)

        return super(PowerPlant, self).get()

    def update(self):
        """PUT /Project/{ProjectId}/Prediction/{PredictionId}/PowerPlant"""
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
        Add a transformer to model the system-level of a power plant.

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

        :param block_id_to_clone:
        :return:
        """
        block_to_clone = [b for b in self.blocks if b['id'] == block_id_to_clone][0]
        block_copy = copy.deepcopy(block_to_clone)
        block_copy["name"] = len(self.blocks) + 1
        self.blocks.append(block_copy)
        self.update()

        return self.blocks[-1]

    # TODO none of this stuff accounts for duplicate names, or out of order names, etc
    @handle_refused_connection
    @handle_error_response
    def add_block(self, use_energization_date=False, energization_date=""):
        """

        :param bool use_energization_date:
        :param str energization_date:
        :return: Block name, which is an integer identifier.
        :rtype: int
        """
        block = {
            "name": 1 if not self.blocks else len(self.blocks) + 1,
            "use_energization_date": use_energization_date,
            "energization_date": energization_date,
            "arrays": []
        }

        try:
            self.blocks.append(block)
        except AttributeError:
            self.blocks = [block]

        return self.blocks[-1]["name"]

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
    def _get_inverter_kva_rating(self, inverter_id):
        """

        :param inverter_id:
        :return:
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
        self.blocks[block_name - 1]["arrays"][array_name - 1]["inverters"].append({
            "name": chr(ord("A") + len(self.blocks[block_name - 1]["arrays"][array_name - 1]["inverters"])),
            "repeater": repeater,
            "inverter_id": inverter_id,
            "setpoint_kw": setpoint_kw if setpoint_kw else self._get_inverter_power_rated(inverter_id),
            "power_factor": power_factor,
            "dc_fields": [],
            "kva_rating": self._get_inverter_kva_rating(inverter_id) if self.use_cooling_temp else kva_rating
        })

        return self.blocks[block_name - 1]["arrays"][array_name - 1]["inverters"][-1]["name"]

    @handle_refused_connection
    @handle_error_response
    def add_dc_field(self, block_name, array_name, inverter_name, module_id, ground_coverage_ratio,
                     number_of_series_strings_wired_in_parallel, field_dc_power,
                     tracking_type, modules_high, modules_wired_in_series, module_azimuth=None, number_of_rows=None,
                     lateral_intermodule_gap=0.02, vertical_intermodule_gap=0.02, module_orientation=None,
                     module_tilt=None, dc_field_backtracking_type=None, minimum_tracking_limit_angle_d=-60.0,
                     maximum_tracking_limit_angle_d=60.0, sandia_conductive_coef=None, sandia_convective_coef=None,
                     cell_to_module_temp_diff=None, heat_balance_conductive_coef=None,
                     heat_balance_convective_coef=None, module_mismatch_coefficient=None, module_quality=None,
                     light_induced_degradation=None, tracker_load_loss=0.0, dc_wiring_loss_at_stc=0.0,
                     dc_health=0.0, array_based_shading=False):

        # if tracking type is fixed tilt module tilt is required
        if (tracking_type == TrackingTypeEnum.FIXED_TILT) and not module_tilt:
            raise ValueError("The input module_tilt is required for a fixed tilt DC field.")
        elif (tracking_type == TrackingTypeEnum.HORIZONTAL_TRACKER) and not dc_field_backtracking_type:
            raise ValueError("The input dc_field_backtracking_type is required for a horizontal tracker DC field.")

        m = self.api.module(id=module_id)
        m.get()
        module_orientation = module_orientation if module_orientation else m.default_orientation
        collector_bandwidth = self.calculate_collector_bandwidth(
            m.width, m.length, module_orientation, modules_high, vertical_intermodule_gap
        )
        post_to_post_spacing = self.calculate_post_to_post_spacing_from_gcr(collector_bandwidth, ground_coverage_ratio)
        number_of_rows = number_of_rows if number_of_rows else number_of_series_strings_wired_in_parallel

        # azimuth faces south if project is above equator
        p = self.api.project(id=self.project_id)
        p.get()
        module_azimuth = module_azimuth if module_azimuth else (
            180.0 if p.latitude >= 0.0 else 0.0
        )

        self.blocks[block_name - 1]["arrays"][array_name - 1]["inverters"][ord(inverter_name) - 65]["dc_fields"].append({
            "name": len(
                self.blocks[block_name - 1]["arrays"][array_name - 1]["inverters"][ord(inverter_name) - 65]["dc_fields"]
            ) + 1,
            "module_id": module_id,
            "tracking_type": tracking_type,
            "module_azimuth": module_azimuth,
            "module_tilt": module_tilt,
            "dc_field_backtracking_type": dc_field_backtracking_type,
            "minimum_tracking_limit_angle_d": minimum_tracking_limit_angle_d,
            "maximum_tracking_limit_angle_d": maximum_tracking_limit_angle_d,
            "modules_high": modules_high,
            "modules_wired_in_series": modules_wired_in_series,
            "number_of_rows": number_of_rows,
            "modules_wide": int(number_of_series_strings_wired_in_parallel*modules_wired_in_series/float(number_of_rows)),
            "module_orientation": module_orientation if module_orientation else m.default_orientation,
            "lateral_intermodule_gap": lateral_intermodule_gap,
            "vertical_intermodule_gap": vertical_intermodule_gap,
            "collector_bandwidth": collector_bandwidth,
            "post_to_post_spacing": post_to_post_spacing,
            "planned_module_rating": m.stc_max_power,
            "field_dc_power": field_dc_power,
            "number_of_series_strings_wired_in_parallel": number_of_series_strings_wired_in_parallel,
            "array_based_shading": array_based_shading,
            "sandia_conductive_coef": sandia_conductive_coef if sandia_conductive_coef else m.sandia_conductive_coef,
            "sandia_convective_coef": sandia_convective_coef if sandia_convective_coef else m.sandia_convective_coef,
            "cell_to_module_temp_diff": (
                cell_to_module_temp_diff if cell_to_module_temp_diff else m.cell_to_module_temp_diff
            ),
            "heat_balance_conductive_coef": (
                heat_balance_conductive_coef if heat_balance_conductive_coef else m.heat_balance_conductive_coef
            ),
            "heat_balance_convective_coef": (
                heat_balance_convective_coef if heat_balance_convective_coef else m.heat_balance_convective_coef
            ),
            "module_mismatch_coefficient": (
                module_mismatch_coefficient if module_mismatch_coefficient else m.module_mismatch_coefficient
            ),
            "module_quality": module_quality if module_quality else m.module_quality,
            "light_induced_degradation": (
                light_induced_degradation if light_induced_degradation else m.light_induced_degradation
            ),
            "tracker_load_loss": tracker_load_loss,
            "dc_wiring_loss_at_stc": dc_wiring_loss_at_stc,
            "dc_health": dc_health
        })

        return self.blocks[
            block_name - 1]["arrays"][array_name - 1]["inverters"][ord(inverter_name) - 65]["dc_fields"][-1]["name"]

    @staticmethod
    @handle_refused_connection
    @handle_error_response
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
    @handle_refused_connection
    @handle_error_response
    def calculate_post_to_post_spacing_from_gcr(collector_bandwidth, ground_coverage_ratio):
        """

        :param collector_bandwidth:
        :param ground_coverage_ratio:
        :return:
        """
        return collector_bandwidth / ground_coverage_ratio

    @staticmethod
    @handle_refused_connection
    @handle_error_response
    def calculate_field_dc_power(dc_ac_ratio, inverter_setpoint):
        """

        :param dc_ac_ratio:
        :param inverter_setpoint:
        :return:
        """
        return dc_ac_ratio*inverter_setpoint

    @staticmethod
    @handle_refused_connection
    @handle_error_response
    def calculate_number_of_series_strings_wired_in_parallel(field_dc_power, planned_module_rating,
                                                             modules_wired_in_series):
        """

        :param field_dc_power:
        :param planned_module_rating:
        :param modules_wired_in_series:
        :return:
        """
        # convert field dc power from kW to W
        return 1000 * field_dc_power / (planned_module_rating * modules_wired_in_series)

    def __init__(self, api, project_id=None, prediction_id=None, use_cooling_temp=True):
        self.project_id = project_id
        self.prediction_id = prediction_id
        self.use_cooling_temp = use_cooling_temp

        self.power_factor = None
        self.blocks = None
        self.transformers = None
        self.transmission_lines = None

        super(PowerPlant, self).__init__(api)
