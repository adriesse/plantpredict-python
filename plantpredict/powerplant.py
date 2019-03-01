from plantpredict.plant_predict_entity import PlantPredictEntity
from plantpredict.error_handlers import handle_refused_connection, handle_error_response
import copy

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

    @handle_refused_connection
    @handle_error_response
    def clone_block(self, block_id_to_clone):
        """

        :return:
        """
        block_to_clone = [b for b in self.blocks if b['id'] == block_id_to_clone][0]
        block_copy = copy.deepcopy(block_to_clone)
        block_copy["name"] = len(self.blocks)
        self.blocks.append(block_copy)
        self.update()

        return self.blocks[-1]
