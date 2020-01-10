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

    :param plantpredict.api.Api api:
    :param int project_id:
    :param int prediction_id:
    :param bool use_cooling_temp:
    :param list blocks:
    :param list transformers:
    :param list transmission_lines:
    :param power_factor:
    :param lgia_limitation:
    :param availability_loss:
    :param use_cooling_temp:
    :param total_module_area:
    :param max_mv_transformer_voltage:
    :param maximum_plant_output:
    :param int id:

    .. container:: toggle

        .. container:: header

            **Contents of `blocks`**

        .. container:: blocks

            .. code-block:: python

                [{
                    "name": 0,
                    "energization_date": "2019-12-26T16:43:55.867Z",
                    "use_energization_date": True,
                    "number_of_modules": 0,
                    "total_module_area": 0,
                    "repeater": 0,
                    "id": 0,
                    "description": "string"
                    "arrays": [{
                        "name": 0,
                        "inverters": [{
                            "name": "string",
                            "dc_fields": [{
                                "name": 0,
                                "module_id": 0,
                                "module": SEE MODULE
                                "tracking_type": plantpredict.enumerations.TrackingTypeEnum.FIXED_TILT,
                                "module_orientation": plantpredict.enumerations.ModuleOrientationEnum,
                                "tables_removed_for_pcs": 0,
                                "ground_slope": 0,
                                "ground_slope_azimuth": 0,
                                "transverse_slope": 0,
                                "baseline_slope": 0,
                                "modules_high": 0,
                                "modules_wide": 0,
                                "lateral_intermodule_gap": 0,
                                "vertical_intermodule_gap": 0,
                                "field_length": 0,
                                "field_width": 0,
                                "collector_bandwidth": 0,
                                "table_length": 0,
                                "tables_per_row": 0,
                                "post_to_post_spacing": 0,
                                "number_of_rows": 0,
                                "table_to_table_spacing": 0,
                                "module_azimuth": 0,
                                "module_tilt": 0,
                                "tracking_backtracking_type": "None",
                                "tracker_pitch_angle_d": 0,
                                "minimum_tracking_limit_angle_d": 0,
                                "maximum_tracking_limit_angle_d": 0,
                                "tracker_stow_angle": 0,
                                "post_height": 0,
                                "structure_shading": 0,
                                "backside_mismatch": 0,
                                "field_dc_power": 0,
                                "modules_wired_in_series": 0,
                                "number_of_series_strings_wired_in_parallel": 0,
                                "planned_module_rating": 0,
                                "sandia_conductive_coef": 0,
                                "sandia_convective_coef": 0,
                                "cell_to_module_temp_diff": 0,
                                "heat_balance_conductive_coef": 0,
                                "heat_balance_convective_coef": 0,
                                "module_mismatch_coefficient": 0,
                                "module_quality": 0,
                                "light_induced_degradation": 0,
                                "tracker_load_loss": 0,
                                "dc_wiring_loss_at_stc": 0,
                                "dc_health": 0,
                                "effective_resistance_at_stc": 0,
                                "total_module_area": 0,
                                "uiam_d": 0,
                                "uiam_g": 0,
                                "ush_d": 0,
                                "ush_g": 0,
                                "repeater": 0,
                                "id": 0,
                                "description": "string"
                            }],
                            "inverter_id": 0,
                            "inverter": SEE INVERTER
                            "setpoint_kw": 0,
                            "power_factor": 0,
                            "kva_rating": 0,
                            "total_module_area": 0,
                            "repeater": 0,
                            "id": 0,
                            "description": "string"
                      }],
                      "ac_collection_loss": 0,
                      "das_load": 0,
                      "cooling_load": 0,
                      "additional_losses": 0,
                      "match_total_inverter_kva": true,
                      "transformer_enabled": true,
                      "array_based_shading": true,
                      "array_shading_number_of_rows": 0,
                      "transformer_kva_rating": 0,
                      "transformer_high_side_voltage": 0,
                      "transformer_no_load_loss": 0,
                      "transformer_full_load_loss": 0,
                      "total_modules": 0,
                      "total_module_area": 0,
                      "tracker_motor_losses": 0,
                      "repeater": 0,
                      "id": 0,
                      "description": "string"
                    }],
                }]

            .. csv-table:: Contents of blocks

                :file: ../docs/_static/csv_tables/powerplant_blocks.csv
                :header-rows: 1
                :stub-columns: 1
                :widths: 20 5 75
                :align: center

    .. container:: toggle

        .. container:: header

            **Contents of `transformers`**

        .. container:: transformers

            .. code-block:: python

                [{
                    "id": 0,
                    "rating": 0,
                    "high_side_voltage": 0,
                    "no_load_loss": 0,
                    "full_load_loss": 0,
                    "ordinal": 0
                }]

    .. container:: toggle

        .. container:: header

            **Contents of `transmission_lines`**

        .. container:: transmission_lines

            .. code-block:: python

                [{
                    "id": 0,
                    "length": 0,
                    "resistance": 0,
                    "number_of_conducters_per_phase": 0,
                    "ordinal: 0,
                }]
    |
    """
    def create(self):
        """
        **POST** */Project/* :py:attr:`project_id` */Prediction/* :py:attr:`prediction_id` */PowerPlant*

        Creates a new power plant in the PlantPredict database with the attributes assigned to the instance of
        :py:class:`~plantpredict.powerplant.PowerPlant`. Automatically attaches it to a project/prediction existing in
        PlantPredict associated with the assigned values for :py:attr:`self.project_id` and
        :py:attr:`self.prediction_id`. See :py:class:`~plantpredict.powerplant.PowerPlant` documentation attributes
        required to successfully call this method.

        :return: `{'is_successful': True}`
        :rtype: dict
        """
        self.power_factor = 1.0

        self.create_url_suffix = "/Project/{}/Prediction/{}/PowerPlant".format(self.project_id, self.prediction_id)
        return super(PowerPlant, self).create()

    def get(self):
        """
        **GET** */Project/* :py:attr:`project_id` */Prediction/* :py:attr:`prediction_id` */PowerPlant*

        Retrieves an existing :py:class:`~plantpredict.powerplant.PowerPlant` from the PlantPredict database
        according to the values assigned for :py:attr:`self.project_id` and :py:attr:`self.prediction_id`, and
        automatically assigns all of its attributes to the local object instance.

        :return: A dictionary containing all of the retrieved :py:class:`~plantpredict.powerplant.PowerPlant`
                 attributes. (Matches the result of calling `self.__dict__` after calling this method).
        :rtype: dict
        """
        self.get_url_suffix = "/Project/{}/Prediction/{}/PowerPlant".format(self.project_id, self.prediction_id)
        return super(PowerPlant, self).get()

    def update(self):
        """
        **PUT** */Project/* :py:attr:`project_id` */Prediction/* :py:attr:`prediction_id` */PowerPlant*

        Updates an existing :py:class:`~plantpredict.powerplant.PowerPlant` entity in PlantPredict using the full
        attributes of the object instance. Calling this method is most commonly preceded by instantiating an
        :py:class:`~plantpredict.powerplant.PowerPlant` object with a particular :py:attr:`self.project_id` and
        :py:attr:`self.prediction_id` and calling :py:meth:`~plantpredict.powerplant.PowerPlant.get`, and changing any
        attributes locally.

        :return: `{'is_successful': True}`
        :rtype: dict
        """
        self.update_url_suffix = "/Project/{}/Prediction/{}/PowerPlant".format(self.project_id, self.prediction_id)
        return super(PowerPlant, self).update()

    def add_transformer(self, rating, high_side_voltage, no_load_loss, full_load_loss, ordinal):
        """
        Adds a transformer to the list :py:attr:`self.transformers` to model the system-level of the power plant.

        :param float rating: Transformer rating. Must be between :py:data:`0.1` and :py:data:`10000.0` - units `[MVA]`.
        :param float high_side_voltage: Transformer voltage. Must be between :py:data:`1.0` and :py:data:`1000.0` -
                                        units `[kV]`.
        :param float no_load_loss: Transformer loss at no load. Must be between :py:data:`0.0` and :py:data:`10.0` -
                                   units `[%]`.
        :param float full_load_loss: Transformer loss at full load. Must be between :py:data:`0.0` and :py:data:`10.0` -
                                     units `[%]`.
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
        Add a transmission line to the list :py:attr:`self.transmission_lines` to model the system-level of the power
        plant.

        :param float length: Length of transmission line. Must be between :py:data:`0.1` and :py:data:`100.0` - units
                     `[km]`.
        :param float resistance: Transmission line resistivity (per 300m). Must be between :py:data:`0.001` and
                                 :py:data:`2` - units `[Ohms/300m]`.
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

    def _validate_block_name(self, block_name):
        """
        Checks that a given block with name `block_name` exists the power plant structure.

        :param int block_name: Name of block. Can be found as key `name` in each dictionary item of list `self.blocks`.
        :raises ValueError: Raised if no blocks in `self.blocks` have the name `block_name`.
        """
        if block_name not in [b['name'] for b in self.blocks]:
            raise ValueError("{} is not a valid block name in the existing power plant structure.".format(block_name))

    def _validate_array_name(self, block_name, array_name):
        """
        Checks that a given block with name `block_name` exists the power plant structure, and if so, that a given array
        with name `array_name` is a valid array in the block.

        :param int block_name: Name of block. Can be found as key `name` in each dictionary item of list `self.blocks`.
        :param int array_name: Name of array. Can be found as key `name` in each dictionary item of list
                               `self.blocks[i]["arrays"]`, where `i` is some valid integer index.
        :raises ValueError: Raised if no blocks in `self.blocks` have the name `block_name`. Also raised if `block_name`
                            is valid but there is no array in the block with name `array_name`.
        """
        self._validate_block_name(block_name)

        if array_name not in [a['name'] for a in self.blocks[block_name - 1]['arrays']]:
            raise ValueError("{} is not a valid array name in block {}.".format(array_name, block_name))

    def _validate_inverter_name(self, block_name, array_name, inverter_name):
        """
        Checks that a given block with name `block_name` exists the power plant structure, and if so, that a given array
        with name `array_name` is a valid array in the block, and if so that a given inverter with name `inverter_name`
        is a valid inverter in the array.

        :param int block_name: Name of block. Can be found as key `name` in each dictionary item of list `self.blocks`.
        :param int array_name: Name of array. Can be found as key `name` in each dictionary item of list
                               `self.blocks[i]["arrays"]`, where `i` is a valid integer index.
        :param str inverter_name: Name of inverter. Can be found as key `name` in each dictionary item of list
                                  `self.blocks[i]["arrays"][j]["inverters"]` where `i` and `j` are valid integer
                                  indices.
        :raises ValueError: Raised if no blocks in `self.blocks` have the name `block_name`. Also raised if `block_name`
                            is valid but there is no array in the block with name `array_name`.
        """
        self._validate_block_name(block_name)
        self._validate_array_name(block_name, array_name)

        if inverter_name not in [i['name'] for i in self.blocks[block_name - 1]['arrays'][array_name - 1]['inverters']]:
            raise ValueError(
                "'{}' is not a valid inverter name in array {} of block {}.".format(inverter_name, array_name,
                                                                                    block_name))

    @handle_refused_connection
    @handle_error_response
    def add_block(self, use_energization_date=False, energization_date=""):
        """
        A "power plant builder" helper method that creates a new block and appends it to :py:attr:`self.blocks`. Block
        naming is sequential (numerically) - for instance, if there are 2 existing blocks with names `1` and `2`
        (accessible via key `name` on each block in list), the next block created by
        :py:meth:`~plantpredict.PowerPlant.powerplant.add_block` will automatically have `name` equal to `3`. This
        method does not currently account for the situation in which an existing power plant has blocks named
        non-sequentially.

        Note that this addition is not persisted to PlantPredict unless
        :py:meth:`~plantpredict.powerplant.PowerPlant.update` is subsequently called.

        :param bool use_energization_date: Enables use of energization date in power plant block. Defaults to `False`.
        :param str energization_date: Timestamp representing energization date of block. Uses format
                                      `2019-12-26T16:43:55.867Z` and defaults `""`.
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

    @handle_refused_connection
    @handle_error_response
    def clone_block(self, block_id_to_clone):
        """
        A "power plant builder" helper method that clones (copies) an existing block (and all of its children
        arrays/inverters/DC fields) and appends it to :py:attr:`self.blocks`. Particularly useful when you want to
        create a new block that is similar to an existing block. Block naming is sequential (numerically) - for
        instance, if there are 2 existing blocks with names `1` and `2` (accessible via key `name` on each block in
        list), the next block created by py:meth:`~plantpredict.powerplant.PowerPlant.clone_block` will automatically
        have `name` equal to `3`. This method does not currently account for the situation in which an existing power
        plant has blocks named non-sequentially.

        Note that this addition is not persisted to PlantPredict unless
        :py:meth:`~plantpredict.powerplant.PowerPlant.update` is subsequently called.

        :param int block_id_to_clone: Unique identifier of the block you wis you clone. Can be found in the relevant
                                      block dictionary (in list :py:attr:`self.blocks`) with key `id`.
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
    def add_array(self, block_name, transformer_enabled=True, match_total_inverter_kva=True,
                  transformer_kva_rating=None, repeater=1, ac_collection_loss=1, das_load=800, cooling_load=0.0,
                  additional_losses=0.0, transformer_high_side_voltage=34.5, transformer_no_load_loss=0.2,
                  transformer_full_load_loss=0.7, description=""):
        """
        A "power plant builder" helper method that adds an array to the block specified by :py:data:`block_name` on the
        :py:class:`~plantpredict.powerplant.PowerPlant`. Array naming is sequential (numerically) - for instance, if
        there are 2 existing arrays with names `1` and `2` (accessible via key `name` for a given array dictionary), the
        next array created by :py:meth:`~plantpredict.powerplant.PowerPlant.add_array` will automatically have `name`
        equal to `3`. This method does not currently account for the situation in which an existing power plant has
        arrays named non-sequentially.

        Note that this addition is not persisted to PlantPredict unless
        :py:meth:`~plantpredict.powerplant.PowerPlant.update` is subsequently called.
        :param int block_name: Name (1-indexed integer) of the parent block to add the array to. Can be found in the
                               relevant block dictionary (in list :py:attr:`self.blocks`) with key `id`.  This value is
                               returned for a new block when you create one with
                               :py:meth:`~plantpredict.powerplant.PowerPlant.add_block`. Must be between :py:data:`1`
                               and :py:data:`99`.
        :param bool transformer_enabled: If `True`, enables a medium-voltage (MV) transformer for the array. Defaults to
                                         `True`.
        :param bool match_total_inverter_kva: If `True`, the transformer size will match the total inverter kVA of the
                                              inverter behind the transformer, and the input `transformer_kva_rating`
                                              won't be used. Defaults to :py:data:`True`.
        :param float, None transformer_kva_rating: User-specified transformer kVA rating. Only used if
                                             :py:data:`match_total_inverter_kva` is set to :py:data:`False`. Must be
                                             between :py:data:`0` and :py:data:`20000` - units `[kVA]`. Defaults to
                                             `None`.
        :param int repeater: Number of identical arrays of this type in the parent block. Must be between :py:data:`1`
                             and :py:data:`10000`. Defaults to :py:data:`1`.
        :param float ac_collection_loss: Accounts for ohmic losses in the AC wiring between the array and parent block.
                                         Must be between :py:data:`0` and :py:data:`30` - units `[%]`. Defaults to
                                         :py:data:`1`.
        :param float das_load: Accounts for parasitic losses due to the data acquisition system (DAS). Can also be used
                               for general time-constant parasitic loss accounting. Must be between :py:data:`0` and
                               :py:data:`5000` - units :py:data:`[W]`. Defaults to :py:data:`800`.
        :param float cooling_load: Accounts for losses from the power conditioning system (PCS) shelter cooling system.
                                   Must be between :py:data:`0` and :py:data:`5000` - units :py:data:`[W]`. Defaults to
                                   :py:data:`0.0`.
        :param float additional_losses: Additional night time losses. Must be between :py:data:`0` and :py:data:`20000`
                                        - units :py:data:`[W]`. Defaults to :py:data:`0`.
        :param float transformer_high_side_voltage: Transformer high side voltage (the AC collection line voltage defines
                                                    the high-side of a MV inverter). Must be between :py:data:`0` and
                                                    :py:data:`66` - units `[V]`. Defaults to :py:data:`34.5`.
        :param float transformer_no_load_loss: Accounts for transformer losses with no load. Must be between
                                               :py:data:`0` and :py:data:`10` - units `[%]`. Defaults to :py:data:`0.2`.
        :param float transformer_full_load_loss: Accounts for transformer losses with full load. Must be between
                                               :py:data:`0` and :py:data:`10` - units `[%]`. Defaults to :py:data:`0.7`.
        :param float str description: Description of the array. Must be :py:data:`250` characters or less.
                                      Defaults to `""`.
        :raises ValueError: Raised if `block_name` is not a valid block name in the existing power plant.
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
        Returns the power rating of an inverter specified by its unique identifier.

        :param int inverter_id: Unique identifier of an Inverter in the PlantPredict Inverter database.
        :return: Power rating of inverter
        :rtype: float
        """
        inverter = self.api.inverter(id=inverter_id)
        inverter.get()

        return inverter.power_rated

    @handle_refused_connection
    @handle_error_response
    def _get_inverter_kva_rating(self, inverter_id):
        """
        Gets the inverters kVA rating based on the elevation and 99.6 Cooling Temperature (which comes
        from the ASHRAE station nearest to the latitude and longitude) of the :py:class:`~plantpredict.project.Project`
        corresponding to `self.project_id`.

        :param int inverter_id: Unique identifier of an Inverter in the PlantPredict Inverter database.
        :return: Kilovolt-Ampere rating, used to rate/size the transformer of a power plant - units py:data:`[kVA]`.
        :rtype: float
        """
        # retrieve ASHRAE station based on latitude and longitude of project associated with power plant
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

        # use the kVA endpoint to calculate the kVA with elevation and 99.6 cooling temp of nearest ASHRAE station
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
        A "power plant builder" helper method that adds an inverter to an array specified by :py:data:`array_name`,
        which is a child of a block specified by :py:data:`block_name` on the
        :py:class:`~plantpredict.powerplant.PowerPlant`. Inverter naming is sequential (alphabetically) - for instance,
        if there are 2 existing inverters with names `"A"` and `"B"` (accessible via key `name` for a given inverter
        dictionary), the next array created by :py:meth:`~plantpredict.powerplant.PowerPlant.add_inverter` will
        automatically have `name` equal to `"C"`. This method does not currently account for the situation in which an
        existing power plant has inverters named non-sequentially.

        Note that this addition is not persisted to PlantPredict unless
        :py:meth:`~plantpredict.powerplant.PowerPlant.update` is subsequently called.

        :param int block_name: Name (1-indexed integer) of the parent block to add the inverter to. Can be found in the
                               relevant block dictionary (in list :py:attr:`self.blocks`) with key `id`.  This value is
                               returned for a new block when you create one with
                               :py:meth:`~plantpredict.powerplant.PowerPlant.add_block`. Must be between :py:data:`1`
                               and :py:data:`99`.
        :param int array_name: Name (1-indexed integer) of the parent array to add the inverter to. This value is
                               returned for a new array when you create one with
                               :py:meth:`~plantpredict.powerplant.PowerPlant.add_array`. Must be between :py:data:`1`
                               and :py:data:`99`.
        :param int inverter_id: Unique identifier of an inverter model in the PlantPredict Inverter database to use.
        :param float, None setpoint_kw: Inverter setpoint. Must be between :py:data:`1` and :py:data:`10000` - units
                                        `[kW]`. If left as default (`None`), the `power_rated` of the inverter model
                                        specified (by :py:data:`inverter_id`) will be used as the inverter setpoint.
        :param float power_factor: The ratio of the power that can be used and the product of the operating current and
                                   voltage. Must be between :py:data:`0` and :py:data:`1`, where `1` is a "unity" power
                                    factor. Defaults to :py:data:`1.0`.
        :param int repeater: Number of identical inverters of this type in the parent array. Must be between
                             :py:data:`1` and :py:data:`10000`. Defaults to :py:data:`1`.
        :param float kva_rating: If :py:attr:`self.use_cooling_temp` is `True`, this value is calculated based on the
                                 99.6 cooling temperature of the nearest ASHARE station to the corresponding
                                 :py:class:`~plantpredict.project.Project` (as specified by :py:attr:`self.project_id`),
                                 the elevation of the :py:class:`~plantpredict.project.Project`, and the
                                 elevation/temperature curves of the inverter model specified by :py:data:`inverter_id`.
                                 Otherwise, defaults to :py:data:`0.0`.
        :raises ValueError: Raised if :py:data:`block_name` is not a valid block name in the existing power plant, or if
                            the :py:data:`block_name` is valid but :py:data:`array_name` is not a valid array name in
                            the block.
        :return: The name of the newly added inverter.
        :rtype: str
        """
        self._validate_array_name(block_name, array_name)

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

    def _get_default_module_azimuth_from_latitude(self):
        """
        Determines the default module azimuth (the orientation of the entire DC field) based on the latitude of the
        :py:class:`~plantpredict.project.Project` associated with the :py:class:`~plantpredict.powerplant.PowerPlant`
        (using :py:attr:`self.project_id`). By default, the DC field is set to be oriented south if above equator. The
        convention is 0.0 degrees for North-facing arrays.

        :return: Default azimuth, :py:data:`180.0` if latitude is above equator, otherwise :py:data:`0.0` - units
                 `[degrees]`.
        :rtype: float
        """
        p = self.api.project(id=self.project_id)
        p.get()
        azimuth = 180.0 if p.latitude >= 0.0 else 0.0

        return azimuth

    @staticmethod
    def _calculate_collector_bandwidth(module_width, module_length, module_orientation, modules_high,
                                       vertical_intermodule_gap):
        """
        Calculates the total width/depth of each table/row of modules in the DC field. The collector bandwidth is
        calculated by multiplying the number of modules high (number of ranks) by each module's vertical dimension,
        which is dependent on if the modules is oriented in portrain or landscape, and then adding the vertical space
        between each module.

        :param float module_width: Width of each individual module in DC field. Must be between :py:data:`0` and
                                   :py:data:`10000` - units `[mm]`.
        :param float module_length: Length of each individual module in DC field. Must be between :py:data:`0` and
                                    :py:data:`10000` - units `[mm]`.
        :param int module_orientation: Represents the orientation (portrait or landscape) of modules in the DC field.
                                       Use :py:class:`~plantpredict.enumerations.ModuleOrientationEnum`.
        :param int modules_high: Number of modules high per table (number of ranks). Must be between :py:data:`1` and
                                 :py:data:`50`.
        :param vertical_intermodule_gap: vertical gap between each module on the mounting structure. Must be between
                                         :py:data:`0` and py:data:`1` - units `[m]'.
        :return: Collector bandwidth for a table in the DC field - units `[m]`.
        :rtype: float
        """
        module_bandwidth = module_width if module_orientation == ModuleOrientationEnum.LANDSCAPE else module_length

        return modules_high * module_bandwidth / 1000.0 + (modules_high - 1) * vertical_intermodule_gap

    @staticmethod
    def _calculate_table_length(modules_wide, module_orientation, module_length, module_width, lateral_intermodule_gap):
        """
        Calculates the length of each table (mounting structure) in meters, for a particular DC field.

        :param int modules_wide: Number of modules across per table. Must be between :py:data:`1` and :py:data:`100`.
        :param int module_orientation: Represents the orientation (portrait or landscape) of modules in the DC field.
                                       Use :py:class:`~plantpredict.enumerations.ModuleOrientationEnum`.
        :param float module_length: Length of each individual module in DC field. Must be between :py:data:`0` and
                                    :py:data:`10000` - units `[mm]`.
        :param float module_width: Width of each individual module in DC field. Must be between :py:data:`0` and
                                   :py:data:`10000` - units `[mm]`.
        :param float lateral_intermodule_gap: Lateral gap between each module on the mounting structure. Must be between
                                              :py:data:`0` and py:data:`1` - units `[m]'.
        :return: Length of each table (mounting structure) for DC field - units `[m]`.
        :rtype: float
        """
        # choose the relevant module dimension (length or width) based on the module orientation
        module_dimension = module_length / 1000.0 if module_orientation == ModuleOrientationEnum.LANDSCAPE \
            else module_width / 1000.0

        return modules_wide*module_dimension + lateral_intermodule_gap*(modules_wide - 1)

    @staticmethod
    def _calculate_tables_per_row(field_dc_power, planned_module_rating, modules_high, modules_wide,
                                  tables_removed_for_pcs, number_of_rows):
        """
        Calculates the number of tables (mounting structures) across per row of a DC field.

        :param float field_dc_power: DC capacity of the DC field. Must be between :py:data:`1` and :py:data:`20000` -
                                     units `[kW]`.
        :param float planned_module_rating: Nameplate rating of each individual module in the DC field. Must be between
                                            :py:data:`10` and :py:data:`1000` - units `[W]`.
        :param int modules_high: Number of modules high per table (number of ranks). Must be between :py:data:`1` and
                                 :py:data:`50`.
        :param int modules_wide: Number of modules across per table. Must be between :py:data:`1` and :py:data:`100`.
        :param float tables_removed_for_pcs: Number of tables removed in DC field to make room for its power
                                             conditioning system (PCS). Must be between :py:data:`0` and :py:data:`50`.
        :param float number_of_rows: Number of rows of tables in DC field. Must be between :py:data:`0.1` and
                                     :py:data:`10000`.
        :return: Number of tables across per row of DC field.
        :rtype: float
        """
        module_count = 1000*field_dc_power / planned_module_rating
        modules_per_table = modules_high * modules_wide            # note: only a frontend value
        total_tables = module_count / modules_per_table            # note: only a frontend value
        tables_per_row = (total_tables + tables_removed_for_pcs) / number_of_rows

        return tables_per_row

    @staticmethod
    def _calculate_dc_field_size_by_collector_bandwidth(number_of_rows, post_to_post_spacing, collector_bandwidth):
        """
        Calculates the DC field dimension from the front of the first table to the back of the last table (the first
        row to the last row).

        :param float number_of_rows: Number of rows of tables in DC field. Must be between :py:data:`0.1` and
                                     :py:data:`10000`.
        :param float post_to_post_spacing: Row spacing. Must be between :py:data:`0.0` and :py:data:`50.0` - units
                                           :py:data:`[m]`.
        :param float collector_bandwidth: The total width/depth of each table/row of modules in the DC field. Must be
                                          between :py:data:`0` and :py:data:`30` - units `[m]`.
        :return: Dimension of DC field in the "front to back" direction - units `[m]`.
        :rtype: float
        """
        return post_to_post_spacing*(number_of_rows - 1) + collector_bandwidth

    @staticmethod
    def _calculate_dc_field_size_by_tables_per_row(tables_per_row, module_orientation, module_length, module_width,
                                                   lateral_intermodule_gap, modules_wide):
        """
        Calculates the DC field dimension along each row of tables/modules.

        :param float tables_per_row: Number of tables wide per row in the DC field.
        :param int module_orientation: Represents the orientation (portrait or landscape) of modules in the DC field.
                                       Use :py:class:`~plantpredict.enumerations.ModuleOrientationEnum`.
        :param float module_length: Length of each individual module in DC field. Must be between :py:data:`0` and
                                    :py:data:`10000` - units `[mm]`.
        :param float module_width: Width of each individual module in DC field. Must be between :py:data:`0` and
                                   :py:data:`10000` - units `[mm]`.
        :param float lateral_intermodule_gap: Lateral gap between each module on the mounting structure. Must be between
                                              :py:data:`0` and py:data:`1` - units `[m]'.
        :param int modules_wide: Number of modules across per table. Must be between :py:data:`1` and :py:data:`100`.
        :return: Dimension of DC field in the "side to side" direction - units `[m]`.
        :rtype: float
        """
        module_size = module_length / 1000.0 if module_orientation == ModuleOrientationEnum.LANDSCAPE \
            else module_width / 1000.0

        return (modules_wide * tables_per_row * (module_size + lateral_intermodule_gap)) - lateral_intermodule_gap

    def _calculate_dc_field_length(self, tables_per_row, module_orientation, module_length, module_width,
                                   lateral_intermodule_gap, modules_wide, tracking_type, number_of_rows,
                                   post_to_post_spacing, collector_bandwidth):
        """
        Calculates the DC field length dimension, which is the "side to side" dimension across each row for a horizontal
        tracker array, and the "front to back" dimension from the front row to the back row of tables for a fixed tilt
        array.

        :param float tables_per_row: Number of tables wide per row in the DC field.
        :param int module_orientation: Represents the orientation (portrait or landscape) of modules in the DC field.
                                       Use :py:class:`~plantpredict.enumerations.ModuleOrientationEnum`.
        :param float module_length: Length of each individual module in DC field. Must be between :py:data:`0` and
                                    :py:data:`10000` - units `[mm]`.
        :param float module_width: Width of each individual module in DC field. Must be between :py:data:`0` and
                                   :py:data:`10000` - units `[mm]`.
        :param float lateral_intermodule_gap: Lateral gap between each module on the mounting structure. Must be between
                                              :py:data:`0` and py:data:`1` - units `[m]'.
        :param int modules_wide: Number of modules across per table. Must be between :py:data:`1` and :py:data:`100`.
        :param int tracking_type: Represents the tracking type/mounting structure (Fixed Tilt, Tracker, etc.) of the DC
                                  field. Use :py:class:`~plantpredict.enumerations.TrackingTypeEnum`.
        :param float number_of_rows: Number of rows of tables in DC field. Must be between :py:data:`0.1` and
                                     :py:data:`10000`.
        :param float post_to_post_spacing: Row spacing. Must be between :py:data:`0.0` and :py:data:`50.0` - units
                                           :py:data:`[m]`.
        :param float collector_bandwidth: The total width/depth of each table/row of modules in the DC field. Must be
                                          between :py:data:`0` and :py:data:`30` - units `[m]`.
        :return: DC field length - units `[m]`.
        :rtype: float
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
        Calculates the DC field width dimension, which is the "side to side" dimension across each row for a horizontal
        fixed tilt array, and the "front to back" dimension from the front row to the back row of tables for a tracker
        array.

        :param int tracking_type: Represents the tracking type/mounting structure (Fixed Tilt, Tracker, etc.) of the DC
                                  field. Use :py:class:`~plantpredict.enumerations.TrackingTypeEnum`.
        :param float number_of_rows: Number of rows of tables in DC field. Must be between :py:data:`0.1` and
                                     :py:data:`10000`.
        :param float post_to_post_spacing: Row spacing. Must be between :py:data:`0.0` and :py:data:`50.0` - units
                                           :py:data:`[m]`.
        :param float collector_bandwidth: The total width/depth of each table/row of modules in the DC field. Must be
                                          between :py:data:`0` and :py:data:`30` - units `[m]`.
        :param float tables_per_row: Number of tables wide per row in the DC field.
        :param int module_orientation: Represents the orientation (portrait or landscape) of modules in the DC field.
                                       Use :py:class:`~plantpredict.enumerations.ModuleOrientationEnum`.
        :param float module_length: Length of each individual module in DC field. Must be between :py:data:`0` and
                                    :py:data:`10000` - units `[mm]`.
        :param float module_width: Width of each individual module in DC field. Must be between :py:data:`0` and
                                   :py:data:`10000` - units `[mm]`.
        :param float lateral_intermodule_gap: Lateral gap between each module on the mounting structure. Must be between
                                              :py:data:`0` and py:data:`1` - units `[m]'.
        :param int, float modules_wide: Number of modules across per table. Must be between :py:data:`1` and
                                       :py:data:`100`.
        :return: DC field width - units `[m]`.
        :rtype: float
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
        Calculates equivalent number of strings in parallel for a given DC capacity, or calculates an equivalent DC
        capacity for a given number of strings in parallel for the DC field. Returns both the provided and calculated
        values.

        :param float, None field_dc_power: DC capacity of the DC field. Must be `None` if
                                     `number_of_seres_strings_wired_in_parallel` is not `None`, otherwise must be
                                     between :py:data:`1` and :py:data:`20000` - units `[kW]`.
        :param float, None number_of_series_strings_wired_in_parallel: Number of strings of modules electrically connected in
                                                                 parallel in the DC field. Must be `None` if
                                                                 `field_dc_power` is not `None`, otherwise must be
                                                                 between :py:data:`1` and :py:data`10000`.
        :param float planned_module_rating: Nameplate rating of each individual module in the DC field. Must be between
                                    :py:data:`10` and :py:data:`1000` - units `[W]`.
        :param int modules_wired_in_series: The number of modules electrically connected in series in a string. Must be
                                            be between :py:data:`1` and :py:data:`100`.
        :raises ValueError: Raised if both `field_dc_power` and `number_of_series_strings_wired_in_parallel` are `None`
                            or are both not `None`.
        :return: Field DC Power (units `[kW]`) and equivalent number of series strings wired in parallel in DC field.
        :rtype: tuple
        """
        if (field_dc_power is not None) and (number_of_series_strings_wired_in_parallel is not None):
            raise ValueError("Both field_dc_power and number_of_series_strings_wired_in_parallel are not None. Only "
                             "one of these values can be specified (and the other will be calculated).")

        # calculates number of strings from field dc power if field dc power specified
        elif (field_dc_power is not None) and (number_of_series_strings_wired_in_parallel is None):
            number_of_series_strings_wired_in_parallel = 1000 * field_dc_power / \
                                                         (planned_module_rating * modules_wired_in_series)

        # calculates field dc power from number of strings if number of strings specified
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
        Useful helper method for calculating :py:attr:`post_to_post_spacing` based on a desired ground coverage ratio
        (GCR). :py:attr:`post_to_post_spacing` is a required input for
        :py:meth:`~plantpredict.powerplant.PowerPlant.add_dc_field`.

        :param float collector_bandwidth: The total width/depth of each table/row of modules in the DC field. Must be
                                          between :py:data:`0` and :py:data:`30` - units `[m]`.
        :param ground_coverage_ratio: Ratio of collector bandwidth to row spacing - units `[decimal]`.
        :return: Post to post spacing (row spacing) of DC field - units `[m]`.
        :rtype: float
        """
        return collector_bandwidth / ground_coverage_ratio

    @staticmethod
    def calculate_field_dc_power_from_dc_ac_ratio(dc_ac_ratio, inverter_setpoint):
        """
        Useful helper method for sizing the DC field capacity (:py:attr:`field_dc_power`) based on a desired DC AC ratio
        and known inverter setpoint. :py:attr:`field_dc_power` is a required input for
        :py:meth:`~plantpredict.powerplant.PowerPlant.add_dc_field`.

        :param float dc_ac_ratio: Ratio of DC capacity of DC field to the AC capacity/inverter setpoint.
        :param float inverter_setpoint: Setpoint of parent inverter to the DC field. Can be found with key `setpoint_kw`
                                        in the dictionary representing the inverter. Must be between :py:data:`1` and
                                        :py:data:`10000` - units `[kW]`.
        :return: DC capacity for a DC field - units `[kW]`.
        :rtype: float
        """
        return dc_ac_ratio*inverter_setpoint

    @staticmethod
    def _validate_mounting_structure_parameters(tracking_type, module_tilt, tracking_backtracking_type):
        """
        Ensures that if the DC field uses a fixed tilt mounting structure, that a tilt angle is provided, and if it
        uses a horizontal tracker mounting structure, that a backtracking type is provided.

        :param int tracking_type: Represents the tracking type/mounting structure (Fixed Tilt, Tracker, etc.) of the DC
                                  field. Use :py:class:`~plantpredict.enumerations.TrackingTypeEnum`.
        :param float, None module_tilt: Tilt angle of modules in DC Field for a fixed tilt array. Must be between
                                        :py:data:`0` and :py:data:`90` - units `[degrees]`.
        :param int, None tracking_backtracking_type: Represents the backtracking algorithm (True-Tracking or
                                                     Backtracking) used in DC Field. Use
                                               :py:class:`~plantpredict.enumerations.BacktrackingTypeEnum`.
        :raises ValueError: Raised if the `tracking_type` is
                            :py:attr:`~plantpredict.enumerations.TrackingTypeEnum.FIXED_TILT` and `module_tilt` is
                            `None`, or if `tracking_type` is
                            `~plantpredict.enumerations.TrackingTypeEnum.HORIZONTAL_TRACKER` and
                            `tracking_backtracking_type` is `None`.
]        """
        if (tracking_type == TrackingTypeEnum.FIXED_TILT) and (module_tilt is None):
            raise ValueError("The input module_tilt is required for a fixed tilt DC field.")
        elif (tracking_type == TrackingTypeEnum.HORIZONTAL_TRACKER) and (tracking_backtracking_type is None):
            raise ValueError("The input tracking_backtracking_type is required for a horizontal tracker DC field.")

    @handle_refused_connection
    @handle_error_response
    def add_dc_field(self, block_name, array_name, inverter_name, module_id, tracking_type, modules_high,
                     modules_wired_in_series, post_to_post_spacing, number_of_rows=1, modules_wide=None,
                     field_dc_power=None, number_of_series_strings_wired_in_parallel=None, module_tilt=None,
                     module_orientation=None, module_azimuth=None, tracking_backtracking_type=None,
                     minimum_tracking_limit_angle_d=-60.0, maximum_tracking_limit_angle_d=60.0,
                     lateral_intermodule_gap=0.02, vertical_intermodule_gap=0.02, array_based_shading=False,
                     table_to_table_spacing=0.0, tables_removed_for_pcs=0, module_quality=None,
                     module_mismatch_coefficient=None, light_induced_degradation=None, dc_wiring_loss_at_stc=1.5,
                     dc_health=1.0, heat_balance_conductive_coef=None, heat_balance_convective_coef=None,
                     sandia_conductive_coef=None, sandia_convective_coef=None, cell_to_module_temp_diff=None,
                     tracker_load_loss=0.0):
        """
        A "power plant builder" helper method that adds a DC field to an inverter specified by :py:data:`inverter_name`,
        which is a child of the array  :py:data:`array_name`, which is a child of a block specified by
        :py:data:`block_name` on the :py:class:`~plantpredict.powerplant.PowerPlant`. DC field naming is sequential
        (numerically) - for instance, if there are 2 existing DC fields with names `1` and `2` (accessible via key
        `name` for a given DC field dictionary), the next array created by
        :py:meth:`~plantpredict.powerplant.PowerPlant.add_dc_field` will automatically have `name` equal to `3`. This
        method does not currently account for the situation in which an existing power plant has DC fields named
        non-sequentially.

        Note that this addition is not persisted to PlantPredict unless
        :py:meth:`~plantpredict.powerplant.PowerPlant.update` is subsequently called.

        :param int block_name: Name (1-indexed integer) of the parent block to add DC field to. Can be found in the
                               relevant block dictionary (in list :py:attr:`self.blocks`) with key `id`.  This value is
                               returned for a new block when you create one with
                               :py:meth:`~plantpredict.powerplant.PowerPlant.add_block`. Must be between :py:data:`1`
                               and :py:data:`99`.
        :param int array_name: Name (1-indexed integer) of the parent array to add DC field to. This value is
                               returned for a new array when you create one with
                               :py:meth:`~plantpredict.powerplant.PowerPlant.add_array`. Must be between :py:data:`1`
                               and :py:data:`99`.
        :param str inverter_name: Name (letter) of the parent array to add the DC field to. This value is returned for
                                  a new array when you create one with
                                  :py:meth:`~plantpredict.powerplant.PowerPlant.add_inverter`. Must be only `1`
                                  character.
        :param int module_id: Unique identifier of the module to be used in the DC field.
        :param int tracking_type: Represents the tracking type/mounting structure (Fixed Tilt, Tracker, etc.) of the DC
                                  field. Use :py:class:`~plantpredict.enumerations.TrackingTypeEnum`. (Seasonal Tilt
                                  currently not supported in this package).
        :param int modules_high: Number of modules high per table (number of ranks). Must be between :py:data:`1` and
                                 :py:data:`50`.
        :param int modules_wired_in_series: The number of modules electrically connected in series in a string.
        :param float post_to_post_spacing: Row spacing. Must be between :py:data:`0.0` and :py:data:`50.0` - units
                                           :py:data:`[m]`.
        :param float, None number_of_rows: Number of rows of tables in DC field. Must be between :py:data:`0.1` and
                                           :py:data:`10000`. Defaults to :py:data:`1`.
        :param int, None modules_wide: Number of modules across per table. Must be between :py:data:`1` and
                                       :py:data:`100`. If left as default (`None`) will be assigned value equal to
                                       :py:data`modules_wired_in_series`.
        :param float, None field_dc_power: DC capacity of the DC field. Defaults to `None`. Non-null value required if
                                           :py:data:`number_of_series_strings_wired_in_parallel` is `None` and  must be
                                           between :py:data:`1` and :py:data:`20000` - units `[kW]`.
        :param float, None number_of_series_strings_wired_in_parallel: Number of strings of modules electrically
                                                                       connected in parallel in the DC field. Defaults
                                                                       to `None`. Non-null value required if
                                                                       :py:data:`field_dc_power` is `None`, and must be
                                                                       between :py:data:`1` and :py:data`10000`.
        :param float, None module_tilt: Tilt angle of modules in DC Field for a fixed tilt array. Defaults to `None`.
                                        Non-null value required required if :py:data:`tracking_type` is equal to
                                        :py:attr:`~plantpredict.enumerations.TrackingTypeEnum.FIXED_TILT`, and must be
                                        between :py:data:`0` and :py:data:`90` - units `[degrees]`.
        :param int, None module_orientation: Represents the orientation (portrait or landscape) of modules in the DC
                                             field. If left as default (`None`), is automatically set as the
                                            :py:attr:`module_orientation` of the module model specified by
                                            :py:data:`module_id`. Use
                                            :py:class:`~plantpredict.enumerations.ModuleOrientationEnum`.
        :param float, None module_azimuth: Orientation of the entire DC field. The convention is 0.0 degrees for
                                           North-facing arrays. If left as default (`None`), is set to :py:data:`180.0`.
                                           Must be between :py:data:`0` and :py:data:`360` - units `[degrees]`.
        :param int, None tracking_backtracking_type: Represents the backtracking algorithm (True-Tracking or
                                                     Backtracking) used in DC Field. Use
                                                     :py:class:`~plantpredict.enumerations.BacktrackingTypeEnum`.
        :param float minimum_tracking_limit_angle_d: Minimum tracking angle for horizontal tracker array. Defaults to
                                                     :py:data:`-60.0`. Must be between :py:data:`-90` and :py:data:`0` -
                                                     units `[degrees]`.
        :param float maximum_tracking_limit_angle_d: Maximum tracking angle for horizontal tracker array. Defaults to
                                                     :py:data:`60.0`. Must be between :py:data:`0` and :py:data:`90` -
                                                     units `[degrees]`.
        :param float lateral_intermodule_gap: Lateral gap between each module on the mounting structure. Must be between
                                              :py:data:`0` and py:data:`1` - units `[m]'.
        :param float vertical_intermodule_gap: Vertical gap between each module on the mounting structure. Must be
                                               between :py:data:`0` and py:data:`1` - units `[m]'.
        :param bool array_based_shading: If `True`, arrays will be modeled as infinite rows, and therefore edge-based
                                         shading effects will be ignored. Defaults to `False`.
        :param float table_to_table_spacing: Space between tables in each row. Defaults to `0.0`. Must be between
                                             :py:data:`0` and :py:data:`50`.
        :param float tables_removed_for_pcs: Number of tables removed in DC field to make room for its power
                                             conditioning system (PCS). Must be between :py:data:`0` and :py:data:`50`.
        :param float, None module_quality: Accounts for any discrepancy between manufacturer nameplate rating of module
                                           and actual performance. If left as default (`None`), is automatically set as
                                           the :py:attr:`module_quality` of the module model specified by
                                           :py:data:`module_id`. Must be between :py:data:`-200` and :py:data:`99` -
                                           units `[%]`.
        :param float, None module_mismatch_coefficient: Accounts for losses due to mismatch in electrical
                                                        characteristics among modules in the strings of the DC fields
                                                        (and between strings in the DC field). If left as default
                                                        (`None`), is automatically set as the
                                                        :py:attr:`module_mismatch_coefficient` of the module model
                                                        specified by :py:data:`module_id`. Must be between :py:data:`0`
                                                        and :py:data:`30` - units `[%]`.
        :param float, None light_induced_degradation: Accounts for losses due to light induced degradation.
                                                      If left as default (`None`), is automatically set as the
                                                      :py:attr:`light_induced_degradation` of the module model specified
                                                      by :py:data:`module_id`. Must be between :py:data:`0` and
                                                      :py:data:`30` - units `[%]`.
        :param float dc_wiring_loss_at_stc: Accounts for losses across all electrical wiring in the DC field. Defaults
                                            to :py:data:`1.5`. Must be between :py:data:`0` and :py:data:`30` - units
                                            `[%]`.
        :param float dc_health: Accounts for any losses related to DC health. Defaults to :py:data:`1.0`. Must be
                                between :py:data:`-10` and :py:data:`10` - units `[%]`.
        :param float, None heat_balance_conductive_coef: Thermal loss factor (constant component) of heat balance module
                                                         surface temperature model. If left as default (`None`), is
                                                         automatically set as the
                                                         :py:attr:`heat_balance_conductive_coef` of the module model
                                                         specified by :py:data:`module_id`. Must be between :py:data:`0`
                                                         and :py:data:`100`. This value is only used if
                                                         :py:attr:`model_temp_model` is set to
                                                         :py:attr:`~plantpredict.enumerations.ModuleTemperatureModelEnum.HEAT_BALANCE`
                                                         for the :py:class:`~plantpredict.prediction.Prediction`
                                                         associated with the power plant by :py:attr:`self.project_id`
                                                         and :py:attr:`self.prediction_id`.
        :param float, None heat_balance_convective_coef: Thermal loss factor (wind speed component) of heat balance
                                                         module surface temperature model. If left as default (`None`),
                                                         is automatically set as the
                                                         :py:attr:`heat_balance_convective_coef` of the module model
                                                         specified by :py:data:`module_id`. Must be between :py:data:`0`
                                                         and :py:data:`100`. This value is only used if
                                                         :py:attr:`model_temp_model` is set to
                                                         :py:attr:`~plantpredict.enumerations.ModuleTemperatureModelEnum.HEAT_BALANCE`
                                                         for the :py:class:`~plantpredict.prediction.Prediction`
                                                         associated with the power plant by :py:attr:`self.project_id`
                                                         and :py:attr:`self.prediction_id`.
        :param float, None sandia_conductive_coef: Coefficient `a` for the Sandia module surface temperature model. If
                                                   left as default (`None`), is automatically set as the
                                                   :py:attr:`sandia_conductive_coef` of the module model specified by
                                                   :py:data:`module_id`. Must be between :py:data:`-5` and :py:data:`0`.
                                                   This value is only used if :py:attr:`model_temp_model` is set to
                                                   :py:attr:`~plantpredict.enumerations.ModuleTemperatureModelEnum.SANDIA`
                                                   for the :py:class:`~plantpredict.prediction.Prediction` associated
                                                   with the power plant by :py:attr:`self.project_id` and
                                                   :py:attr:`self.prediction_id`.
        :param float, None sandia_convective_coef: Coefficient `b` for the Sandia module surface temperature model. If
                                                   left as default (`None`), is automatically set as the
                                                   :py:attr:`sandia_convective_coef` of the module model specified by
                                                   :py:data:`module_id`. Must be between :py:data:`-1` and :py:data:`0`.
                                                   This value is only used if :py:attr:`model_temp_model` is set to
                                                   :py:attr:`~plantpredict.enumerations.ModuleTemperatureModelEnum.SANDIA`
                                                   for the :py:class:`~plantpredict.prediction.Prediction` associated
                                                   with the power plant by :py:attr:`self.project_id` and
                                                   :py:attr:`self.prediction_id`.
        :param float, None cell_to_module_temp_diff: Difference between surface and cell temperature of modules. If left
                                                     as default (`None`), is automatically set as the
                                                     :py:attr:`cell_to_module_temp_diff` of the module model specified
                                                     by :py:data:`module_id`. Must be between :py:data:`0` and
                                                     :py:data:`15` - units `[degrees-C]`.
        :param float tracker_load_loss: Accounts for losses from power use of horizontal tracker system. Defaults to
                                        `0.0`. Must be between :py:data:`0` and :py:data:`100` - units `[%]`.
        :raises ValueError: Raised if `block_name` is not a valid block name in the existing power plant, or if the
                            :py:data:`block_name` is valid but :py:data:`array_name` is not a valid array name in the
                            block, or if :py:data:`array_name` is valid but :py:data:`inverter_name` is not a valid
                            inverter in the array. Also raised if :py:data:`tracking_type` is
                            :py:attr:`~plantpredict.enumerations.TrackingTypeEnum.FIXED_TILT` and :py:data:`module_tilt`
                            is `None`, or if :py:data:`tracking_type` is
                            `~plantpredict.enumerations.TrackingTypeEnum.HORIZONTAL_TRACKER` and
                            :py:data:`tracking_backtracking_type` is `None`. Also raised if both
                            :py:data:`field_dc_power` and :py:data`number_of_series_strings_wired_in_parallel` are
                            `None` or are both not `None`.
        :return: The name of the newly added DC field.
        :rtype: int
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
        collector_bandwidth = self._calculate_collector_bandwidth(
            module_width=m.width,
            module_length=m.length,
            module_orientation=module_orientation,
            vertical_intermodule_gap=vertical_intermodule_gap,
            modules_high=modules_high
        )
        table_length = self._calculate_table_length(
            modules_wide=modules_wide,
            module_width=m.width,
            module_length=m.length,
            module_orientation=module_orientation,
            lateral_intermodule_gap=lateral_intermodule_gap
        )
        tables_per_row = self._calculate_tables_per_row(
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
            "tracking_backtracking_type": tracking_backtracking_type,
            "minimum_tracking_limit_angle_d": minimum_tracking_limit_angle_d,
            "maximum_tracking_limit_angle_d": maximum_tracking_limit_angle_d,
            "module_orientation": module_orientation,
            "modules_high": modules_high,
            "module_azimuth": (module_azimuth if module_azimuth is not None
                               else self._get_default_module_azimuth_from_latitude()),
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

    def __init__(self, api, project_id=None, prediction_id=None, use_cooling_temp=True, **kwargs):
        """
        Constructor method.
        """
        self.project_id = project_id
        self.prediction_id = prediction_id
        self.use_cooling_temp = use_cooling_temp

        self.power_factor = None
        self.blocks = []
        self.transformers = []
        self.transmission_lines = []

        # set any provided keyword arguments as attributes
        self.__dict__.update(kwargs)

        super(PowerPlant, self).__init__(api)
