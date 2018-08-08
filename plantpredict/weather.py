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

        Minimum required attributes for successful Weather creation:

        .. csv-table::
            :header: Field, Type, Description

            latitude, float, adfaldkfa
            longitude, float, adlfajdfla
            weather detail, dict, adf;lkajdsf

        :return:
        """
        self.create_url_suffix = "/Weather"
        super(Weather, self).create()

    def delete(self):
        """DELETE /Weather/{Id}"""
        self.delete_url_suffix = "/Weather/{}".format(self.id)
        super(Weather, self).delete()

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
