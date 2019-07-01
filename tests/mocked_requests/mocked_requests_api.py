from tests.mocked_requests.mock_response import MockResponse


def mocked_requests_post(*args, **kwargs):
    if kwargs['url'] == "https://afse.okta.com/oauth2/aus3jzhulkrINTdnc356/v1/token":
        if kwargs["params"]["grant_type"] == "password":
            return MockResponse(
                json_data={"access_token": "dummy access token", "refresh_token": "dummy refresh token"},
                status_code=200
            )

        elif kwargs["params"]["grant_type"] == "refresh_token":
            return MockResponse(
                json_data={"access_token": "dummy access token 2", "refresh_token": "dummy refresh token 2"},
                status_code=200
            )

    return MockResponse(None, 404)
