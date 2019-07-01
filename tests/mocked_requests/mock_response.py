import json


class MockResponse:
    def __init__(self, json_data, status_code):
        self.content = json.dumps(json_data)
        self.status_code = status_code

    def json(self):
        return self.content
