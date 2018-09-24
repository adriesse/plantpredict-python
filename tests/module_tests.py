import plantpredict
from plantpredict.enumerations import pv_model_type_enum, cell_technology_type_enum


plantpredict.OAuth2.token(client_id=plantpredict.settings.CLIENT_ID, client_secret=plantpredict.settings.CLIENT_SECRET)

m = plantpredict.Module()

m.name = "Test Module"
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

# for recomb
#m.built_in_voltage = 0.9
#m.recombination_parameter = 0.9

m.create()

m.delete()

