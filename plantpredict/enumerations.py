class PlantPredictEnum(dict):
    pass


# Air Mass Model
air_mass_model_type_enum = PlantPredictEnum()
air_mass_model_type_enum.BIRD_HULSTROM = 0
air_mass_model_type_enum.KASTEN_SANDIA = 1

# Backtracking Type
backtracking_type_enum = PlantPredictEnum()
backtracking_type_enum.TRUE_TRACKING = 0   # no backtracking
backtracking_type_enum.BACKTRACKING = 1    # shade avoidance

# Cell Technology
cell_technology_type_enum = PlantPredictEnum()
cell_technology_type_enum.NTYPE_MONO_CSI = 1
cell_technology_type_enum.PTYPE_MONO_CSI_PERC = 2
cell_technology_type_enum.PTYPE_MONO_CSI_BSF = 3
cell_technology_type_enum.POLY_CSI_PERC = 4
cell_technology_type_enum.POLY_CSI_BSF = 5
cell_technology_type_enum.CDTE = 6
cell_technology_type_enum.CIGS = 7

# Cleaning Frequency
cleaning_frequency_enum = PlantPredictEnum()
cleaning_frequency_enum.NONE = 0
cleaning_frequency_enum.DAILY = 1
cleaning_frequency_enum.MONTHLY = 2
cleaning_frequency_enum.QUARTERLY = 3
cleaning_frequency_enum.YEARLY = 4

# Construction Type
construction_type_enum = PlantPredictEnum()
construction_type_enum.GLASS_GLASS = 1
construction_type_enum.GLASS_BACKSHEET = 2

# Data Source
data_source_enum = PlantPredictEnum()
data_source_enum.MANUFACTURER = 1
data_source_enum.PVSYST = 2
data_source_enum.UNIVERSITY_OF_GENEVA = 3
data_source_enum.PHOTON = 4
data_source_enum.SANDIA_DATABASE = 5
data_source_enum.CUSTOM = 6

# Degradation Model
degradation_model_enum = PlantPredictEnum()
degradation_model_enum.NONE = 0
degradation_model_enum.STEPPED_AC = 1
degradation_model_enum.LINEAR_AC = 2
degradation_model_enum.LINEAR_DC = 3
degradation_model_enum.NON_LINEAR_DC = 4

# Diffuse Direct Decomposition Model
diffuse_direct_decomposition_model_enum = PlantPredictEnum()
diffuse_direct_decomposition_model_enum.ERBS = 0
diffuse_direct_decomposition_model_enum.REINDL = 1
diffuse_direct_decomposition_model_enum.DIRINT = 2
diffuse_direct_decomposition_model_enum.NONE = 3

# Diffuse Shading Model
diffuse_shading_model_enum = PlantPredictEnum()
diffuse_shading_model_enum.NONE = 0
diffuse_shading_model_enum.SCHAAR_PANCHULA = 1

# Direct Beam Shading Model
direct_beam_shading_model_enum = PlantPredictEnum()
direct_beam_shading_model_enum.LINEAR = 0
direct_beam_shading_model_enum.NONE = 1
direct_beam_shading_model_enum.TWO_DIMENSION = 2   # Retired
direct_beam_shading_model_enum.FRACTIONAL_EFFECT = 3   # Fractional Electric Shading
direct_beam_shading_model_enum.CSI_3_DIODE = 4
direct_beam_shading_model_enum.MODULE_FILE_DEFINED = 5

# Entity Type
entity_type_enum = PlantPredictEnum()
entity_type_enum.PROJECT = 1
entity_type_enum.MODULE = 2
entity_type_enum.INVERTER = 3
entity_type_enum.WEATHER = 4
entity_type_enum.PREDICTION = 5

# Energy Storage System (ESS) Charge Algorithm
ess_charge_algorithm_enum = PlantPredictEnum()
ess_charge_algorithm_enum.LGIA_EXCESS = 0
ess_charge_algorithm_enum.ENERGY_AVAILABLE = 1
ess_charge_algorithm_enum.CUSTOM = 2

# Energy Storage System (ESS) Dispatch Custom Command
ess_dispatch_custom_command_enum = PlantPredictEnum()
ess_dispatch_custom_command_enum.NONE = 0
ess_dispatch_custom_command_enum.DISCHARGE = 1
ess_dispatch_custom_command_enum.CHARGE = 2

# Faciality
faciality_enum = PlantPredictEnum()
faciality_enum.MONOFACIAL = 0
faciality_enum.BIFACIAL = 1

# Incidence Angle Model Type
incidence_angle_model_type_enum = PlantPredictEnum()
incidence_angle_model_type_enum.SANDIA = 2
incidence_angle_model_type_enum.ASHRAE = 3
incidence_angle_model_type_enum.NONE = 4
incidence_angle_model_type_enum.TABULAR_IAM = 5

# TODO Library Status


# Module Degradation Model
module_degradation_model_enum = PlantPredictEnum()
module_degradation_model_enum.UNSPECIFIED = 0
module_degradation_model_enum.LINEAR = 1
module_degradation_model_enum.NONLINEAR = 2

# Module Orientation
module_orientation_enum = PlantPredictEnum()
module_orientation_enum.LANDSCAPE = 0
module_orientation_enum.PORTRAIT = 1

# TODO Module Shading Response

# TODO Module Temperature Model

# TODO Module Type

# Prediction Status
prediction_status_enum = PlantPredictEnum()
prediction_status_enum.DRAFT_PRIVATE = 1
prediction_status_enum.DRAFT_SHARED = 2
prediction_status_enum.ANALYSIS = 3
prediction_status_enum.BID = 4
prediction_status_enum.CONTRACT = 5
prediction_status_enum.DEVELOPMENT = 6
prediction_status_enum.AS_BUILT = 7
prediction_status_enum.WARRANTY = 8
prediction_status_enum.ARCHIVED = 9

# TODO Prediction Version

# TODO Processing Status

# TODO Project Status

# PV Model
pv_model_type_enum = PlantPredictEnum()
pv_model_type_enum.ONE_DIODE_RECOMBINATION = 0
pv_model_type_enum.ONE_DIODE = 1
pv_model_type_enum.ONE_DIODE_RECOMBINATION_NONLINEAR = 3

# TODO Soiling Model

# Spectral Shift Model
spectral_shift_model_enum = PlantPredictEnum()
spectral_shift_model_enum.NO_SPECTRAL_SHIFT = 0
spectral_shift_model_enum.ONE_PARAM_PWAT_OR_SANDIA = 1
spectral_shift_model_enum.TWO_PARAM_PWAT_AND_AM = 2
spectral_shift_model_enum.MONTHLY_OVERRIDE = 3

# TODO Spectral Weather Type

# Tracking Type
tracking_type_enum = PlantPredictEnum()
tracking_type_enum.FIXED_TILT = 0
tracking_type_enum.HORIZONTAL_TRACKER = 1
tracking_type_enum.SEASONAL_TILT = 2

# TODO Transposition Model

# TODO Weather Data Provider

# TODO Weather Data Type

# TODO Weather File Column Type

# TODO Weather P-Level

# TODO Weather Time Resolution
