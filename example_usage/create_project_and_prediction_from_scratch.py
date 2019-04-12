"""This file contains the code for "Create project from scratch" in the "Example Usage" section of the
documentation located at https://plantpredict-python.readthedocs.io."""

import plantpredict
from plantpredict.enumerations import prediction_status_enum, transposition_model_enum, spectral_shift_model_enum, \
    diffuse_direct_decomposition_model_enum, module_temperature_model_enum, incidence_angle_model_type_enum, \
    air_mass_model_type_enum, direct_beam_shading_model_enum, soiling_model_type_enum, degradation_model_enum, \
    tracking_type_enum, backtracking_type_enum, diffuse_shading_model_enum

# authenticate using API credentials
api = plantpredict.Api(
    username="insert username here",
    password="insert password here",
    client_id="insert client_id here",
    client_secret="insert client_secret here"
)

# instantiate a local instance of Project, assigning name, latitude, and longitude
project = api.project(name="Area 51 Alien Power Plant", latitude=37.23, longitude=-115.80)

# assign location attributes with helper method, and create in the PlantPredict database
project.assign_location_attributes()
project.create()

# instantiate a local instance of Prediction, assigning project_id (from the newly created project) and name
prediction = api.prediction(project_id=project.id, name="Area 51 - Contracted")

# assign the weather_id corresponding to the weather file you want to use (assuming it already exists in the
# PlantPredict database).
prediction.weather_id = 13628

# instantiate and retrieve the weather file and ensure that the two pairs of prediction start/end attributes match those
# of the weather file.
weather = api.weather(id=prediction.weather_id)
weather.get()
prediction.start_date = weather.start_date
prediction.end_date = weather.end_date
prediction.start = weather.start_date
prediction.end = weather.end_date

# Set ALL of the model options on the prediction using the enumerations library in plantpredict.enumerations similar to
# code below, but to your preferences.
prediction.diffuse_direct_decomp_model = diffuse_direct_decomposition_model_enum.NONE
prediction.transposition_model = transposition_model_enum.PEREZ
prediction.mod_temp_model = module_temperature_model_enum.HEAT_BALANCE
prediction.inc_angle_model = incidence_angle_model_type_enum.TABULAR_IAM
prediction.spectral_shift_model = spectral_shift_model_enum.TWO_PARAM_PWAT_AND_AM
prediction.air_mass_model = air_mass_model_type_enum.BIRD_HULSTROM
prediction.direct_beam_shading_model = direct_beam_shading_model_enum.LINEAR
prediction.diffuse_shading_model = diffuse_shading_model_enum.SCHAAR_PANCHULA
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
prediction.year_repeater = 3

# create the Prediction in PlantPredict database
prediction.create()

# change the prediction's status to DRAFT-SHARED to make it accessible to other members of your team (or to another
# relevant status)
prediction.change_prediction_status(new_status=prediction_status_enum.DRAFT_SHARED, note="Changed for tutorial.")

# instantiate a local instance of PowerPlant, assigning project_id and prediction_id
powerplant = api.powerplant(project_id=project.id, prediction_id=prediction.id)

# add fixed tilt array
fixed_tilt_block_name = powerplant.add_block()
fixed_tilt_array_name = powerplant.add_array(
    block_name=fixed_tilt_block_name,
    transformer_enabled=False,
)
fixed_tilt_inverter_name = powerplant.add_inverter(
    block_name=fixed_tilt_block_name,
    array_name=fixed_tilt_array_name,
    inverter_id=619,
    setpoint_kw=720.0
)
fixed_tilt_dc_field_name = powerplant.add_dc_field(
    block_name=fixed_tilt_block_name,
    array_name=fixed_tilt_array_name,
    inverter_name=fixed_tilt_inverter_name,
    module_id=298,
    ground_coverage_ratio=0.40,
    dc_ac_ratio=1.23,
    tracking_type=tracking_type_enum.FIXED_TILT,
    module_tilt=25.0,
    modules_high=4,
    modules_wired_in_series=10,
    number_of_rows=100
)

# add tracker array
tracker_block_name = powerplant.add_block()
tracker_array_name = powerplant.add_array(
    block_name=tracker_block_name,
    transformer_enabled=False,
)
tracker_inverter_name = powerplant.add_inverter(
    block_name=tracker_block_name,
    array_name=tracker_array_name,
    inverter_id=619,
    setpoint_kw=720.0
)
tracker_dc_field_name = powerplant.add_dc_field(
    block_name=tracker_block_name,
    array_name=tracker_array_name,
    inverter_name=tracker_inverter_name,
    module_id=298,
    ground_coverage_ratio=0.40,
    dc_ac_ratio=1.23,
    tracking_type=tracking_type_enum.HORIZONTAL_TRACKER,
    dc_field_backtracking_type=backtracking_type_enum.TRUE_TRACKING,
    modules_high=4,
    modules_wired_in_series=10,
    number_of_rows=100
)

# create the local instance of PowerPlant as a new entity in the PlantPredict database. since the id's of the project
# and prediction created previously were assigned to the PowerPlant, it will automatically attach to the prediction in
# PlantPredict
powerplant.create()

# the prediction can now be run
prediction.run()
