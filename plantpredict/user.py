import requests
from plantpredict import settings
from plantpredict.error_handlers import handle_refused_connection, handle_error_response


class User(object):
    """
    """
    @staticmethod
    @handle_error_response
    @handle_refused_connection
    def get_queue():
        """GET /User/Queue

        :return:
        """
        return requests.get(
            url=settings.BASE_URL + "/User/Queue",
            headers={"Authorization": "Bearer " + settings.TOKEN}
        )

