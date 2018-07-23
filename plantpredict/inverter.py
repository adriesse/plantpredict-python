from plantpredict.plant_predict_entity import PlantPredictEntity
from plantpredict.utilities import decorate_all_methods
from plantpredict.error_handlers import handle_refused_connection, handle_error_response


@decorate_all_methods(handle_refused_connection)
@decorate_all_methods(handle_error_response)
class Inverter(PlantPredictEntity):
    """
    """
    def create(self):
        """POST /Inverter"""
        self.create_url_suffix = "/Inverter"
        super(Inverter, self).create()

    def delete(self):
        """DELETE /Inverter/{Id}"""
        self.delete_url_suffix = "/Inverter/{}".format(self.id)
        super(Inverter, self).delete()

    def get(self):
        """GET /Inverter/{Id}"""
        self.get_url_suffix = "/Inverter/{}".format(self.id)
        super(Inverter, self).get()

    def update(self):
        """PUT /Inverter"""
        self.update_url_suffix = "/Inverter/{}".format(self.id)
        super(Inverter, self).update()
