from tests.mocked_requests.mock_response import MockResponse


def mocked_requests_get(*args, **kwargs):
    if kwargs['url'] == "https://api.plantpredict.com/Geo/39.67/-105.21/Location":
        return MockResponse(
            json_data={
                "country": "United States",
                "country_code": "US",
                "locality": "Morrison",
                "region": "North America",
                "state_province": "Colorado",
                "state_province_code": "CO"
            },
            status_code=200
        )

    elif kwargs['url'] == "https://api.plantpredict.com/Geo/39.67/-105.21/Elevation":
        return MockResponse(
            json_data={"elevation": 1965.96},
            status_code=200
        )

    elif kwargs['url'] == "https://api.plantpredict.com/Geo/39.67/-105.21/TimeZone":
        return MockResponse(
            json_data={"time_zone": -7.0},
            status_code=200
        )

    return MockResponse(None, 404)
