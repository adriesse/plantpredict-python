import requests
from plantpredict import settings
from plantpredict.plant_predict_entity import PlantPredictEntity
from plantpredict.utilities import decorate_all_methods
from plantpredict.error_handlers import handle_refused_connection, handle_error_response


@decorate_all_methods(handle_refused_connection)
@decorate_all_methods(handle_error_response)
class Project(PlantPredictEntity):
    """
    """
    def create(self):
        """POST /Project"""
        self.create_url_suffix = "/Project"

        return super(Project, self).create()

    def delete(self):
        """DELETE /Project/{ProjectId}"""
        self.delete_url_suffix = "/Project/{}".format(self.id)

        return super(Project, self).delete()

    def get(self):
        """GET /Project/{Id}"""
        self.get_url_suffix = "/Project/{}".format(self.id)

        return super(Project, self).get()

    def update(self):
        """PUT /Project"""
        self.update_url_suffix = "/Project"

        return super(Project, self).update()

    def get_all_predictions(self):
        """GET /Project/{ProjectId}/Prediction"""

        return requests.get(
            url=settings.BASE_URL + "/Project/{}/Prediction".format(self.id),
            headers={"Authorization": "Bearer " + settings.TOKEN}
        )

    # TODO figure this out
    @staticmethod
    def search(latitude, longitude, search_radius=1):
        """
        """
        return requests.get(
            url=settings.BASE_URL + "/Project/Search",
            headers={"Authorization": "Bearer " + settings.TOKEN},
            params={'latitude': latitude, 'longitude': longitude, 'searchRadius': search_radius}
        )
