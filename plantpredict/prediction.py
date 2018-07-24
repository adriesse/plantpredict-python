import requests
from plantpredict import settings
from plantpredict.plant_predict_entity import PlantPredictEntity
from plantpredict.powerplant import PowerPlant
from plantpredict.utilities import decorate_all_methods, convert_json, camel_to_snake, snake_to_camel
from plantpredict.error_handlers import handle_refused_connection, handle_error_response


@decorate_all_methods(handle_refused_connection)
@decorate_all_methods(handle_error_response)
class Prediction(PlantPredictEntity):
    """
    """
    def create(self):
        """POST /Project/{ProjectId}/Prediction"""
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

    def run(self, export_options=None):
        """POST /Project/{ProjectId}/Prediction/{PredictionId}/Run"""

        return requests.post(
            url=settings.BASE_URL + "/Project/{}/Prediction/{}/Run".format(self.project_id, self.id),
            headers={"Authorization": "Bearer " + settings.TOKEN},
            json=convert_json(export_options, snake_to_camel)
        )

    def get_results_summary(self):
        """GET /Project/{ProjectId}/Prediction/{Id}/ResultSummary"""

        return requests.get(
            url=settings.BASE_URL + "/Project/{}/Prediction/{}/ResultSummary".format(self.project_id, self.id),
            headers={"Authorization": "Bearer " + settings.TOKEN}
        )

    def get_results_details(self):
        """GET /Project/{ProjectId}/Prediction/{Id}/ResultDetails"""

        return requests.get(
            url=settings.BASE_URL + "/Project/{}/Prediction/{}/ResultDetails".format(self.project_id, self.id),
            headers={"Authorization": "Bearer " + settings.TOKEN}
        )

    def get_nodal_data(self, params):
        """GET /Project/{ProjectId}/Prediction/{Id}/NodalJson"""

        return requests.get(
            url=settings.BASE_URL + "/Project/{}/Prediction/{}/NodalJson".format(self.project_id, self.id),
            headers={"Authorization": "Bearer " + settings.TOKEN},
            params=convert_json(params, snake_to_camel)
        )

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

    def init(self):
        """This class initializes with the attributes (with set to null) required to successfully create a new
        prediction via Prediction.create()."""

        super(Prediction, self).__init__()
        self.__dict__.update({
            'project_id': 0,
            'linear_degradation_rate': 0,
            'error_model_acc': 0,
            'error_sens_acc': 0,
            'error_int_ann_var': 0,
            'error_mon_acc': 0,
            'error_spa_var': 0
        })
