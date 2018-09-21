import json
import requests
from plantpredict.settings import BASE_URL, TOKEN, REFRESH_TOKEN


class OAuth2(object):
    @staticmethod
    def token(client_id, client_secret):
        """

        :param client_id:
        :param client_secret:
        :return:
        """
        response = requests.post(
            url=BASE_URL + "/oauth2/token",
            headers={"content-type": "application/x-www-form-urlencoded"},
            data={
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": "client_credentials"
            }
        )

        # set authentication token as global variable
        try:
            TOKEN = json.loads(response.content)['access_token']
            REFRESH_TOKEN = json.loads(response.content)['refresh_token']
        except KeyError:
            pass

        return response

    @staticmethod
    def refresh():
        response = requests.post(
            url=BASE_URL + "/oauth2/token",
            headers={"content-type": "application/x-www-form-urlencoded"},
            data={
                "refresh_token": REFRESH_TOKEN,
                "grant_type": "refresh_token"
            }
        )

        # set authentication token as global variable
        try:
            TOKEN = json.loads(response.content)['access_token']
            REFRESH_TOKEN = json.loads(response.content)['refresh_token']
        except KeyError:
            pass

        return response

    def __init__(self):
        pass

