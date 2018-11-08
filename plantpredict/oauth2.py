import json
import requests
import plantpredict


class OAuth2(object):
    @staticmethod
    def token(client_id, client_secret):
        """

        :param client_id:
        :param client_secret:
        :return:
        """
        response = requests.post(
            url=plantpredict.settings.BASE_URL + "/oauth2/token",
            headers={"content-type": "application/x-www-form-urlencoded"},
            data={
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": "client_credentials"
            }
        )

        # set authentication token as global variable
        try:
            plantpredict.settings.TOKEN = json.loads(response.content)['access_token']
            plantpredict.settings.REFRESH_TOKEN = json.loads(response.content)['refresh_token']
        except KeyError:
            pass

        return response

    # TODO switch this to official token code
    @staticmethod
    def token_okta():
        """
        :return:
        """
        response = requests.post(
            #url="https://afse.okta.com/oauth2/aus3jzhulkrINTdnc356/v1/token",  # TODO switch back
            url="https://fse.oktapreview.com/oauth2/ausfopidl3Y2kHwOn0h7/v1/token", # this is the preview URL
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
            url=plantpredict.settings.BASE_URL + "/oauth2/token",
            headers={"content-type": "application/x-www-form-urlencoded"},
            data={
                "refresh_token": plantpredict.settings.REFRESH_TOKEN,
                "grant_type": "refresh_token"
            }
        )

        # set authentication token as global variable
        try:
            plantpredict.settings.TOKEN = json.loads(response.content)['access_token']
            plantpredict.settings.REFRESH_TOKEN = json.loads(response.content)['refresh_token']
        except KeyError:
            pass

        return response

    # TODO switch this to official refresh
    @staticmethod
    def refresh_okta():
        response = requests.post(
            #url="https://afse.okta.com/oauth2/aus3jzhulkrINTdnc356/v1/token",  # TODO switch back
            url="https://fse.oktapreview.com/oauth2/ausfopidl3Y2kHwOn0h7/v1/token", # this is the preview URL
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

