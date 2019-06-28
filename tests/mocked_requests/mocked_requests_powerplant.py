from tests.mocked_requests.mock_response import MockResponse


def mocked_requests_post(*args, **kwargs):
    if kwargs['url'] == "https://api.plantpredict.com/Project/710/Prediction/556/PowerPlant":
        return MockResponse(
            json_data={},
            status_code=204
        )

    return MockResponse(None, 404)


def mocked_requests_get(*args, **kwargs):
    if kwargs['url'] == "https://api.plantpredict.com/Project/710/Prediction/555/PowerPlant":
        return MockResponse(
            json_data={
                "id": 1000,
                "project_id": 710,
                "prediction_id": 555,
                "blocks": [{
                    "id": 1,
                    "arrays": [{
                        "id": 2,
                        "inverters": [{
                            "id": 3,
                            "dc_fields": [{"id": 4}]
                        }]
                    }]
                }]
            },
            status_code=200
        )

    return MockResponse(None, 404)
