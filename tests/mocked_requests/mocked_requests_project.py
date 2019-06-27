from tests.mocked_requests.mock_response import MockResponse


def mocked_requests_get(*args, **kwargs):
    if kwargs['url'] == "https://api.plantpredict.com/Project/710/Prediction":
        return MockResponse(
            json_data=[
                {"project_id": 1, "name": "Project 1"},
                {"project_id": 2, "name": "Project 2"},
                {"project_id": 3, "name": "Project 3"}
            ],
            status_code=200
        )

    elif kwargs['url'] == "https://api.plantpredict.com/Project/Search":
        return MockResponse(
            json_data=[{"project_id": 1, "name": "Project 1"}],
            status_code=200
        )

    return MockResponse(None, 404)
