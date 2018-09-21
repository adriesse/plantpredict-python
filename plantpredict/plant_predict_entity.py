import json
import requests
from plantpredict.settings import BASE_URL, TOKEN
from plantpredict.utilities import convert_json, camel_to_snake, snake_to_camel, decorate_all_methods
from plantpredict.error_handlers import handle_refused_connection, handle_error_response


@decorate_all_methods(handle_refused_connection)
@decorate_all_methods(handle_error_response)
class PlantPredictEntity(object):
    def create(self, *args):
        """Generic POST request."""
        response = requests.post(
            url=BASE_URL + self.create_url_suffix,
            headers={"Authorization": "Bearer " + TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )

        # power plant is the exception that doesn't have its own id. has a project and prediction id ???
        try:
            self.id = json.loads(response.content)['id'] if 200 <= response.status_code < 300 else None
        except ValueError:
            pass

        return response

    def delete(self):
        """Generic DELETE request."""

        return requests.delete(
            url=BASE_URL + self.delete_url_suffix,
            headers={"Authorization": "Bearer " + TOKEN}
        )

    def get(self):
        """Generic GET request."""
        response = requests.get(
            url=BASE_URL + self.get_url_suffix,
            headers={"Authorization": "Bearer " + TOKEN}
        )
        attr = convert_json(json.loads(response.content), camel_to_snake)
        for key in attr:
            setattr(self, key, attr[key])

        return response

    def update(self):
        """Generic PUT request."""

        return requests.put(
            url=BASE_URL + self.update_url_suffix,
            headers={"Authorization": "Bearer " + TOKEN},
            json=convert_json(self.__dict__, snake_to_camel)
        )

    def __init__(self, **kwargs):
        self.create_url_suffix = None
        self.delete_url_suffix = None
        self.get_url_suffix = None
        self.update_url_suffix = None

        self.__dict__.update(kwargs)
