import requests
from requests import Response
import logging

logger = logging.getLogger(__name__)


class PolygonRequests:
    """
    A class to handle requests to the Polygon API.
    """
    def __init__(self, api_key: str):
        self.__api_key = api_key
        self.__base_url = "https://api.polygon.io/"

    @property
    def base_url(self) -> str:
        """
        Returns the base URL for the Polygon API.
        """
        return self.__base_url

    @base_url.setter
    def base_url(self, value: str):
        """
        Sets the base URL for the Polygon API.
        :param value:
        :return:
        """
        self.__base_url = value

    @staticmethod
    def assert_status_code(expected_status_code: int, response: Response) -> bool:
        """
        Asserts that the returned status code matches the expected status code.
        :param expected_status_code: Expected HTTP status code.
        :param response: Response object
        :return:True or False
        """
        if expected_status_code != response.status_code:
            logger.error(f"Expected status code {expected_status_code}, but got {response.status_code}." )
            logger.error(f"Response Body: {response.json()}")
            return False
        else:
            return True

    def get(self, endpoint: str) -> Response:
        """
        GET Wrapper for Polygon API requests.
        :param endpoint: Endpoint to hit.
        :return: Response object
        """
        response = requests.get(url=f"{self.base_url}{endpoint}?apiKey={self.__api_key}")
        # TODO: Add logic for checking if API KEY exists then redact it
        logger.info(f"{self.base_url}{endpoint}&apiKey=*****")
        return response
