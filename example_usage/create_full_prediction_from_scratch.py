"""This file contains the code for "Create full prediction from scratch" in the "Example Usage" section of the
documentation located at https://plantpredict-python.readthedocs.io."""

import plantpredict
from plantpredict.enumerations import prediction_status_enum, transposition_model_enum, spectral_shift_model_enum, \
    diffuse_direct_decomposition_model_enum, module_temperature_model_enum, incidence_angle_model_type_enum, \
    air_mass_model_type_enum, direct_beam_shading_model_enum, soiling_model_type_enum, degradation_model_enum, \
    tracking_type_enum, backtracking_type_enum

# authenticate with client credentials and assign TOKEN variable in plantpredict/settings.py
plantpredict.OAuth2.token(client_id=plantpredict.settings.CLIENT_ID, client_secret=plantpredict.settings.CLIENT_SECRET)

# Create the initial prediction, assigning it a Project using "prediction.project_id"
# (assuming the Project already exists).
prediction = plantpredict.Prediction()
prediction.name = "Test Prediction"
prediction.project_id = 11623
prediction.status = prediction_status_enum.DRAFT_PRIVATE
prediction.year_repeater = 3

# instantiate weather using the weather ID, and retrieve all of its attributes, assuming the file is already created
weather_id = 499
weather = plantpredict.Weather(id=weather_id)
weather.get()

# ensure that the prediction start/end attributes match those of the weather file
prediction.start_date = weather.start_date
prediction.end_date = weather.end_date
prediction.start = weather.start_date
prediction.end = weather.end_date

# change the weather ID of the prediction, and update the prediction
prediction.weather_id = weather_id

# Set all of the model options on the prediction and update.
prediction.diffuse_direct_decomp_model = diffuse_direct_decomposition_model_enum.NONE
prediction.transposition_model = transposition_model_enum.PEREZ
prediction.mod_temp_model = module_temperature_model_enum.HEAT_BALANCE
prediction.inc_angle_model = incidence_angle_model_type_enum.TABULAR_IAM
prediction.spectral_shift_model = spectral_shift_model_enum.TWO_PARAM_PWAT_AND_AM
prediction.air_mass_model = air_mass_model_type_enum.BIRD_HULSTROM
prediction.direct_beam_shading_model = direct_beam_shading_model_enum.TWO_DIMENSION_TRIGONOMETRIC
prediction.soiling_model = soiling_model_type_enum.CONSTANT_MONTHLY
prediction.monthly_factors = [
    {"month": 1, "month_name": "Jan", "albedo": 0.2, "soiling_loss": 2.0},
    {"month": 2, "month_name": "Feb", "albedo": 0.2, "soiling_loss": 2.0},
    {"month": 3, "month_name": "Mar", "albedo": 0.2, "soiling_loss": 2.0},
    {"month": 4, "month_name": "Apr", "albedo": 0.2, "soiling_loss": 2.0},
    {"month": 5, "month_name": "May", "albedo": 0.2, "soiling_loss": 2.0},
    {"month": 6, "month_name": "Jun", "albedo": 0.2, "soiling_loss": 2.0},
    {"month": 7, "month_name": "Jul", "albedo": 0.2, "soiling_loss": 2.0},
    {"month": 8, "month_name": "Aug", "albedo": 0.2, "soiling_loss": 2.0},
    {"month": 9, "month_name": "Sep", "albedo": 0.2, "soiling_loss": 2.0},
    {"month": 10, "month_name": "Oct", "albedo": 0.2, "soiling_loss": 2.0},
    {"month": 11, "month_name": "Nov", "albedo": 0.2, "soiling_loss": 2.0},
    {"month": 12, "month_name": "Dec", "albedo": 0.2, "soiling_loss": 2.0},
]
prediction.diffuse_direct_decomp_model_executed = True
prediction.use_meteo_dni = False
prediction.use_meteo_poai = False
prediction.degradation_model = degradation_model_enum.LINEAR_DC
prediction.linear_degradation_rate = 0.5
prediction.first_year_degradation = False

prediction.create()

# get module file and inverter file that will be used in power plant for reference
module = plantpredict.Module(id=298)
module.get()
inverter = plantpredict.Inverter(id=619)
inverter.get()

# calculate field dc power and dc field dimensions based on desired DCAC Ratio
dc_ac_ratio = 1.23
inverter_setpoint = inverter.power_rated
field_dc_power = dc_ac_ratio*inverter_setpoint/2    # divide by 2 since two dc fields
planned_module_rating = module.stc_max_power
modules_wired_in_series = 10
number_of_series_strings_wired_in_parallel = 1000*field_dc_power/(planned_module_rating*modules_wired_in_series)    # convert field dc power from kW to W

# calculate post to post spacing from desired GCR, use width in collector bandwidth since module orientation landscape
GCR = 0.40
modules_high = 4
vertical_intermodule_gap = 0.02
collector_bandwidth = modules_high*module.width/1000 + 3*vertical_intermodule_gap
post_to_post_spacing = collector_bandwidth/GCR

# create a power plant with a single block, single array, single inverter, and two dc fields (fixed tilt array and
# tracker array)
powerplant = plantpredict.PowerPlant(project_id=prediction.project_id, prediction_id=prediction.id)
powerplant.power_factor = 1.0
powerplant.blocks = [{
    "name": 1,
    "arrays": [{
        "name": 1,
        "ac_collection_loss": 1.0,
        "das_load": 800.0,
        "cooling_load": 0.0,
        "transformer_enabled": False,
        "transformer_kva_rating": inverter_setpoint,
        "transformer_high_side_voltage": 34.5,
        "transformer_no_load_loss": 0.2,
        "transformer_full_load_loss": 0.7,
        "inverters": [{
            "name": "A",
            "inverter_id": 619,
            "setpoint_kw": inverter_setpoint,
            "power_factor": 1.0,
            "kva_rating": inverter_setpoint,
            "dc_fields": [
                # fixed tilt dc field
                {
                    "name": 1,
                    "module_id": 298,
                    "tracking_type": tracking_type_enum.FIXED_TILT,
                    "modules_high": modules_high,
                    "modules_wide": modules_wired_in_series, # each string is a row, for simplicity
                    "lateral_intermodule_gap": 0.02,
                    "vertical_intermodule_gap": vertical_intermodule_gap,
                    "module_orientation": module.default_orientation,
                    "collector_bandwidth": collector_bandwidth,
                    "post_to_post_spacing": post_to_post_spacing,
                    "number_of_rows": number_of_series_strings_wired_in_parallel,   # each string is a row, for simplicity
                    "module_azimuth": 180.0,
                    "module_tilt": 25.0,
                    "planned_module_rating": module.stc_max_power,
                    "field_dc_power": field_dc_power,
                    "modules_wired_in_series": modules_wired_in_series,
                    "number_of_series_strings_wired_in_parallel": number_of_series_strings_wired_in_parallel,
                    "sandia_conductive_coef": module.sandia_conductive_coef,
                    "sandia_convective_coef": module.sandia_convective_coef,
                    "cell_to_module_temp_diff": module.cell_to_module_temp_diff,
                    "heat_balance_conductive_coef": module.heat_balance_conductive_coef,
                    "heat_balance_convective_coef": module.heat_balance_convective_coef,
                    "module_mismatch_coefficient": module.module_mismatch_coefficient,
                    "module_quality": module.module_quality,
                    "light_induced_degradation": module.light_induced_degradation,
                    "tracker_load_loss": 0.0,
                    "dc_wiring_loss_at_stc": 1.5,
                    "dc_health": 0.0
                },
                # tracker dc field
                {
                    "name": 2,
                    "module_id": 298,
                    "tracking_type": tracking_type_enum.HORIZONTAL_TRACKER,
                    "modules_high": modules_high,
                    "modules_wide": modules_wired_in_series, # each string is a row, for simplicity
                    "lateral_intermodule_gap": 0.02,
                    "vertical_intermodule_gap": vertical_intermodule_gap,
                    "module_orientation": module.default_orientation,
                    "collector_bandwidth": collector_bandwidth,
                    "post_to_post_spacing": post_to_post_spacing,
                    "number_of_rows": number_of_series_strings_wired_in_parallel,   # each string is a row, for simplicity
                    "dc_field_backtracking_type": backtracking_type_enum.TRUE_TRACKING,
                    "minimum_tracking_limit_angle_d": -60,
                    "maximum_tracking_limit_angle_d": 60,
                    "planned_module_rating": module.stc_max_power,
                    "field_dc_power": field_dc_power,
                    "modules_wired_in_series": modules_wired_in_series,
                    "number_of_series_strings_wired_in_parallel": number_of_series_strings_wired_in_parallel,
                    "sandia_conductive_coef": module.sandia_conductive_coef,
                    "sandia_convective_coef": module.sandia_convective_coef,
                    "cell_to_module_temp_diff": module.cell_to_module_temp_diff,
                    "heat_balance_conductive_coef": module.heat_balance_conductive_coef,
                    "heat_balance_convective_coef": module.heat_balance_convective_coef,
                    "module_mismatch_coefficient": module.module_mismatch_coefficient,
                    "module_quality": module.module_quality,
                    "light_induced_degradation": module.light_induced_degradation,
                    "tracker_load_loss": 0.0,
                    "dc_wiring_loss_at_stc": 1.5,
                    "dc_health": 0.0
                }
            ]
        }]
    }]
}]

powerplant.create()


# run the prediction
prediction.run()

