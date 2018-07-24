import time
import requests
import json
from plantpredict.utilities import convert_json, camel_to_snake
from plantpredict.oauth2 import OAuth2


def handle_refused_connection(function):
    def function_wrapper(*args, **kwargs):
        connection_error = True
        while connection_error:
            try:
                connection_error = False
                return function(*args, **kwargs)
            except requests.exceptions.ConnectionError:
                print('Connection refused, trying again...')
                time.sleep(7)
    return function_wrapper


def handle_error_response(function):
    def function_wrapper(*args, **kwargs):
        response = function(*args, **kwargs)
        try:
            if response.status_code == 401:
                OAuth2.refresh()
            elif not 200 <= response.status_code < 300:
                raise APIError(response.status_code, response.content)
            else:
                if response.content:
                    if "Queue" in response.url:
                        return json.loads(response.content)
                    else:
                        return convert_json(json.loads(response.content), camel_to_snake)
                else:
                    return {'is_successful': True}
        except AttributeError:
            return response

    return function_wrapper


class APIError(Exception):

    def __init__(self, status, errors):
        self.status = status
        self.errors = errors

    def __str__(self):
        return "HTTP Status Code {}: {}".format(
            self.status,
            self.errors
        )
