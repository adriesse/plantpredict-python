import json
import requests
from plantpredict import settings
from plantpredict.plant_predict_entity import PlantPredictEntity
from plantpredict.error_handlers import handle_refused_connection, handle_error_response
from plantpredict.utilities import decorate_all_methods, convert_json, camel_to_snake, snake_to_camel


class Weather(PlantPredictEntity):
    """
    The full contents of the Weather database entity (in JSON) can be found under
    "GET /Weather/{Id}" in `the general PlantPredict API documentation
    <http://app.plantpredict.com/swagger/ui/index#!/Weather/Weather_Get_0>`_.
    """

    def create(self):
        """
        POST /Weather

        Creates a new Weather entity.

        .. csv-table:: Minimum required attributes for successful Weather creation
            :header: Field, Type, Description

            name, str, Name of weather file
            country_code, str, Country code of the Weather's location (ex. US for United States, AUS for Australia, etc.)
            country, str, Full name of the country of the Weather's location.
            latitude, float, North-South coordinate of the Project location, in decimal degrees.
            longitude, float, East-West coordinate of the Project location, in decimal degrees.
            data_provider, int, Represents a weather data source. See (and/or import) :py:mod:`plantpredict.enumerations.weather_data_provider_enum` for a list of options.
            weather_detail, list of dict, Each dictionary in the list contains one timestamp of weather data points summarized below.

        .. list-table:: Contents of each weather_detail timestamp
            :header-rows: 1

            * - Field
              - Type
              - Description
            * - Index
              - aldkfjafa
              - aldskfjakdlf

        :return: A dictionary containing the project id.
        :rtype: dict
        """
        self.create_url_suffix = "/Weather"
        super(Weather, self).create()

    def delete(self):
        """DELETE /Weather/{WeatherId}

        Deletes an existing Weather entity in PlantPredict. The local instance of the Weather entity must have
        attribute self.id identical to the weather id of the Weather to be deleted.

        :return: A dictionary {"is_successful": True}.
        :rtype: dict
        """
        self.delete_url_suffix = "/Weather/{}".format(self.id)

        return super(Weather, self).delete()

    def get(self):
        """GET /Weather/{Id}"""
        self.get_url_suffix = "/Weather/{}".format(self.id)
        super(Weather, self).get()

    def update(self):
        """PUT /Weather"""
        self.update_url_suffix = "/Weather/{}".format(self.id)
        super(Weather, self).update()

    @handle_refused_connection
    @handle_error_response
    def get_detail(self):
        """GET /Weather/{Id}/Detail"""
        return requests.get(
            url=settings.BASE_URL + "/Weather/{}/Detail".format(self.id),
            headers={"Authorization": "Bearer " + settings.TOKEN}
        )

    @staticmethod
    def search(latitude, longitude, search_radius=2):
        """GET /Weather/Search

        :param latitude:
        :param longitude:
        :param search_radius:
        :return:
        """
        response = requests.get(
            url=settings.BASE_URL + "/Weather/Search",
            headers={"Authorization": "Bearer " + settings.TOKEN},
            params=convert_json({
                'latitude': latitude,
                'longitude': longitude,
                'search_radius': search_radius
            }, snake_to_camel)
        )

        weather_list = json.loads(response.content)

        return [convert_json(w, camel_to_snake) for w in weather_list]

    @handle_refused_connection
    @handle_error_response
    def download(self, latitude, longitude, provider=0):
        """POST /Weather/Download/{Provider}

        Weather Providers -
        Unknown = 0,
        Meteonorm = 1,
        CPRSolarAnywhere = 2,
        NSRDB_PSM = 3,
        NSRDB_SUNY = 4,
        NSRDB_MTS2 = 5,
        SolarGIS = 6

        # ^^^ TODO include this under param provider with description.

        :param latitude:
        :param longitude:
        :param provider:
        :return:
        """
        response = requests.post(
            url=settings.BASE_URL + "/Weather/Download/{}".format(provider),
            headers={"Authorization": "Bearer " + settings.TOKEN},
            params={'latitude': latitude, 'longitude': longitude}
        )

        self.id = json.loads(response.content)['id'] if 200 <= response.status_code < 300 else None

        return response
