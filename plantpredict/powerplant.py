from plantpredict.plant_predict_entity import PlantPredictEntity
from plantpredict.utilities import decorate_all_methods
from plantpredict.error_handlers import handle_refused_connection, handle_error_response


@decorate_all_methods(handle_refused_connection)
@decorate_all_methods(handle_error_response)
class PowerPlant(PlantPredictEntity):
    """
    """
    def create(self):
        """POST /Project/{ProjectId}/Prediction/{PredictionId}/PowerPlant"""
        self.create_url_suffix = "/Project/{}/Prediction/{}/PowerPlant".format(self.project_id, self.prediction_id)

        return super(PowerPlant, self).create()

    def delete(self):
        """DELETE /Project/{ProjectId}/Prediction/{PredictionId}/PowerPlant"""
        self.delete_url_suffix = "/Project/{}/Prediction/{}/PowerPlant".format(self.project_id, self.prediction_id)
        super(PowerPlant, self).delete()

    def get(self):
        """"GET /Project/{ProjectId}/Prediction/{PredictionId}/PowerPlant"""
        self.get_url_suffix = "/Project/{}/Prediction/{}/PowerPlant".format(self.project_id, self.prediction_id)

        return super(PowerPlant, self).get()

    def update(self):
        """PUT /Project/{ProjectId}/Prediction/{PredictionId}/PowerPlant"""
        self.update_url_suffix = "/Project/{}/Prediction/{}/PowerPlant".format(self.project_id, self.prediction_id)

        return super(PowerPlant, self).update()
