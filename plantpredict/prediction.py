import requests
from plantpredict import settings
from plantpredict.plant_predict_entity import PlantPredictEntity
from plantpredict.powerplant import PowerPlant
from plantpredict.utilities import convert_json, snake_to_camel
from plantpredict.error_handlers import handle_refused_connection, handle_error_response
from plantpredict.enumerations.library_status_enum import *


class Prediction(PlantPredictEntity):
    """
    T
    """
    def create(self, name=None, project_id=None, status=DRAFT_PRIVATE, year_repeater=1):
        """POST /Project/{ProjectId}/Prediction

        :param name:
        :type name: str
        :param project_id:
        :type
        :param status:
        :param year_repeater:
        :return:
        """
        self.name = name if name is not None else self.name
        self.project_id = project_id if project_id is not None else self.project_id
        self.status = status if self.status is None else self.status
        self.year_repeater = year_repeater if self.year_repeater is None else self.year_repeater

        self.create_url_suffix = "/Project/{}/Prediction".format(self.project_id)

        return super(Prediction, self).create()

    def delete(self):
        """DELETE /Project/{ProjectId}/Prediction/{Id}"""
        self.delete_url_suffix = "/Project/{}/Prediction/{}".format(self.project_id, self.id)

        return super(Prediction, self).delete()

    def get(self):
        """GET /Project/{ProjectId}/Prediction/{Id}"""
        self.get_url_suffix = "/Project/{}/Prediction/{}".format(self.project_id, self.id)

        return super(Prediction, self).get()

    def update(self):
        """PUT /Project/{ProjectId}/Prediction"""
        self.update_url_suffix = "/Project/{}/Prediction".format(self.project_id)

        return super(Prediction, self).update()

    @handle_refused_connection
    @handle_error_response
    def run(self, export_options=None):
        """POST /Project/{ProjectId}/Prediction/{PredictionId}/Run"""

        return requests.post(
            url=settings.BASE_URL + "/Project/{}/Prediction/{}/Run".format(self.project_id, self.id),
            headers={"Authorization": "Bearer " + settings.TOKEN},
            json=convert_json(export_options, snake_to_camel)
        )

    @handle_refused_connection
    @handle_error_response
    def get_results_summary(self):
        """GET /Project/{ProjectId}/Prediction/{Id}/ResultSummary"""

        return requests.get(
            url=settings.BASE_URL + "/Project/{}/Prediction/{}/ResultSummary".format(self.project_id, self.id),
            headers={"Authorization": "Bearer " + settings.TOKEN}
        )

    @handle_refused_connection
    @handle_error_response
    def get_results_details(self):
        """GET /Project/{ProjectId}/Prediction/{Id}/ResultDetails"""

        return requests.get(
            url=settings.BASE_URL + "/Project/{}/Prediction/{}/ResultDetails".format(self.project_id, self.id),
            headers={"Authorization": "Bearer " + settings.TOKEN}
        )

    @handle_refused_connection
    @handle_error_response
    def get_nodal_data(self, params):
        """GET /Project/{ProjectId}/Prediction/{Id}/NodalJson"""

        return requests.get(
            url=settings.BASE_URL + "/Project/{}/Prediction/{}/NodalJson".format(self.project_id, self.id),
            headers={"Authorization": "Bearer " + settings.TOKEN},
            params=convert_json(params, snake_to_camel)
        )

    @handle_refused_connection
    @handle_error_response
    def clone(self, new_prediction_name):
        """

        Parameters
        ----------
        new_prediction_name

        Returns
        -------

        """
        # clone prediction
        new_prediction = Prediction()
        self.get()
        original_prediction_id = self.id

        new_prediction.__dict__ = self.__dict__
        # initialize necessary fields
        new_prediction.__dict__.pop('prediction_id', None)
        new_prediction.__dict__.pop('created_date', None)
        new_prediction.__dict__.pop('last_modified', None)
        new_prediction.__dict__.pop('last_modified_by', None)
        new_prediction.__dict__.pop('last_modified_by_id', None)
        new_prediction.__dict__.pop('project', None)
        new_prediction.__dict__.pop('power_plant_id', None)
        new_prediction.__dict__.pop('powerplant', None)

        new_prediction.name = new_prediction_name
        new_prediction.create()
        new_prediction_id = new_prediction.id

        # clone powerplant and attach to new prediction
        new_powerplant = PowerPlant()
        powerplant = PowerPlant(project_id=self.project_id, prediction_id=original_prediction_id)
        powerplant.get()
        new_powerplant.__dict__ = powerplant.__dict__
        new_powerplant.prediction_id = new_prediction_id
        new_powerplant.__dict__.pop('id', None)

        # initialize necessary fields
        for block in new_powerplant.blocks:
            block.pop('id', None)
            for array in block['arrays']:
                array.pop('id', None)
                for inverter in array['inverters']:
                    inverter.pop('id', None)
                    for dc_field in inverter['dc_fields']:
                        dc_field.pop('id', None)

        new_powerplant.create()

        self.id = original_prediction_id
        self.get()

        return new_prediction_id

    def __init__(self):
        self.name = None
        self.project_id = None
        self.status = None
        self.year_repeater = None

        super(Prediction, self).__init__()
