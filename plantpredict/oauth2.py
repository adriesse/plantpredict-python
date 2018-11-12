import json
import requests
import plantpredict


class OAuth2(object):
    @staticmethod
    def token():
        """
        :return:
        """
        response = requests.post(
            url="https://afse.okta.com/oauth2/aus3jzhulkrINTdnc356/v1/token",
            headers={"content-type": "application/x-www-form-urlencoded"},
            params={
                "grant_type": "password",
                "scope": "openid offline_access",
                "username": plantpredict.settings.USERNAME,
                "password": plantpredict.settings.PASSWORD,
                "client_id": plantpredict.settings.CLIENT_ID,
                "client_secret": plantpredict.settings.CLIENT_SECRET
            }
        )

        # set authentication token as global variable
        try:
            plantpredict.settings.TOKEN = json.loads(response.content)['access_token']
            plantpredict.settings.REFRESH_TOKEN = json.loads(response.content)['refresh_token']
        except KeyError:
            pass

        return response

    @staticmethod
    def refresh():
        response = requests.post(
            url="https://afse.okta.com/oauth2/aus3jzhulkrINTdnc356/v1/token",
            headers={"content-type": "application/x-www-form-urlencoded"},
            data={
                "refresh_token": plantpredict.settings.REFRESH_TOKEN,
                "grant_type": "refresh_token",
                "scope": "offline_access",
                "client_id": plantpredict.settings.CLIENT_ID,
                "client_secret": plantpredict.settings.CLIENT_SECRET
            }
        )

        # set authentication token as global variable
        try:
            plantpredict.settings.TOKEN = json.loads(response.content)['access_token']
            plantpredict.settings.REFRESH_TOKEN = json.loads(response.content)['refresh_token']
        except KeyError:
            pass

        return response

    def __init__(self):
        pass
