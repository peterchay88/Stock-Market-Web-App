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
    def __assert_status_code(expected_status_code: int, returned_status_code: int):
        """
        Asserts that the returned status code matches the expected status code.
        :param expected_status_code: Expected HTTP status code.
        :param returned_status_code: Actual returned HTTP status code.
        :return:
        """
        assert expected_status_code == returned_status_code, \
            f"Expected status code {expected_status_code}, but got {returned_status_code}."

    def get(self, endpoint: str) -> Response:
        """
        GET Wrapper for Polygon API requests.
        :param endpoint: Endpoint to hit.
        :return: Response object
        """
        response = requests.get(url=f"{self.base_url}{endpoint}&apiKey={self.__api_key}")
        # TODO: Add logic for checking if API KEY exists then redact it
        logger.info(f"{self.base_url}{endpoint}&apiKey=*****")
        self.__assert_status_code(expected_status_code=200, returned_status_code=response.status_code)
        return response
