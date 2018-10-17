from plantpredict.plant_predict_entity import PlantPredictEntity


class PowerPlant(PlantPredictEntity):
    """
    """
    def create(self):
        """
        **POST** */Project/ :py:attr:`project_id` /Prediction/ :py:attr:`prediction_id` /PowerPlant*

        """
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
