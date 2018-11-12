import json
import plantpredict
from plantpredict.enumerations import weather_data_provider_enum, library_status_enum, weather_data_type_enum, \
    weather_plevel_enum
import numpy as np


# authenticate with client credentials and assign TOKEN variable in plantpredict/settings.py
plantpredict.OAuth2.token()

# load JSON file containing weather time series
with open('example_usage_files/weather_details.json', 'rb') as json_file:
    weather_details = json.load(json_file)

# get location info from latitude and longitude
latitude = 35.0
longitude = -119.0
location_info = plantpredict.Geo.get_location_info(latitude=latitude, longitude=longitude)

# initial the weather file and populate REQUIRED weather fields
weather = plantpredict.Weather()
weather.name = "Python SDK Test Weather"
weather.latitude = 35.0
weather.longitude = -119.0
weather.country = location_info['country']
weather.country_code = location_info['country_code']
weather.data_provider = weather_data_provider_enum.METEONORM
weather.weather_details = weather_details

# populate additional weather metadata
weather.elevation = round(plantpredict.Geo.get_elevation(latitude=latitude, longitude=longitude)['elevation'], 2)
weather.locality = location_info['locality']
weather.region = location_info['region']
weather.state_province = location_info['state_province']
weather.state_province_code = location_info['state_province_code']
weather.time_zone = plantpredict.Geo.get_time_zone(latitude=latitude, longitude=longitude)['time_zone']
weather.status = library_status_enum.DRAFT_PRIVATE
weather.data_type = weather_data_type_enum.MEASURED
weather.p_level = weather_plevel_enum.P95
weather.time_interval = 60  # minutes
weather.global_horizontal_irradiance_sum = round(
    sum([w['global_horizontal_irradiance'] for w in weather_details])/1000, 2
)
weather.diffuse_horizontal_irradiance_sum = round(
    sum([w['diffuse_horizontal_irradiance'] for w in weather_details])/1000, 2
)
weather.direct_normal_irradiance_sum = round(
    sum([w['direct_normal_irradiance'] for w in weather_details])/1000, 2
)
weather.average_air_temperature = np.round(np.mean([w['temperature'] for w in weather_details]), 2)
weather.average_relative_humidity = np.round(np.mean([w['relative_humidity'] for w in weather_details]), 2)
weather.average_wind_speed = np.round(np.mean([w['windspeed'] for w in weather_details]), 2)
weather.max_air_temperature = np.round(max([w['temperature'] for w in weather_details]), 2)

# create weather file in PlantPredict
weather.create()

# delete weather for housekeeping
weather.delete()
