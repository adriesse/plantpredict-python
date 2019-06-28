from tests.mocked_requests.mock_response import MockResponse


def mocked_requests_post(*args, **kwargs):
    if kwargs['url'] == "https://api.plantpredict.com/Project/710/Prediction/555/Run":
        return MockResponse(json_data={}, status_code=204)

    elif kwargs['url'] == "https://api.plantpredict.com/Project/710/Prediction/555/ResultSummary":
        return MockResponse(
            json_data={},
            status_code=200
        )

    elif kwargs['url'] == "https://api.plantpredict.com/Project/710/Prediction":
        return MockResponse(
            json_data={"id": 556, "project_id": 710, "name": "Prediction Name 2"},
            status_code=200
        )

    return MockResponse(None, 404)


def mocked_requests_get(*args, **kwargs):
    if kwargs['url'] == "https://api.plantpredict.com/Project/710/Prediction/555/ResultSummary":
        return MockResponse(
            json_data={"prediction_name": "Test Prediction", "block_result_summaries": [{"name": 1}]},
            status_code=200
        )

    elif kwargs['url'] == "https://api.plantpredict.com/Project/710/Prediction/555/ResultDetails":
        return MockResponse(
            json_data={"prediction_name": "Test Prediction Details"},
            status_code=200
        )

    elif kwargs['url'] == "https://api.plantpredict.com/Project/710/Prediction/555/NodalJson":
        return {"nodal_data_dc_field": {}}

    elif kwargs['url'] == "https://api.plantpredict.com/Project/710/Prediction/555":
        return MockResponse(
            json_data={"id": 555, "project_id": 710, "name": "Prediction Name"},
            status_code=200
        )

    return MockResponse(None, 404)
