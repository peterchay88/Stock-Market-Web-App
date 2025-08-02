# TODO: Resolve absolute import statements
# from stockmarket.quotes.polygon.polygon_api import PolygonRequests

from . polygon_api import PolygonRequests
from enum import Enum
from .. logging_config.logging_config import logging

logger = logging.getLogger(__name__)


class TickerEndpoint(Enum):
    """
    Enum class for Ticker API endpoints.
    """
    TICKERS = "v3/reference/tickers/"


class Tickers(PolygonRequests):
    """
    A class to handle requests to the Ticker endpoint in the Polygon API.
    """

    def __int__(self, api_key: str):
        """
        Initializes the Tickers class with the API key.
        :param api_key: The API key for Polygon.
        """
        super().__init__(api_key=api_key)

    def get_specific_ticker(self, ticker: str):
        """
        Issues a GET request to the ticker endpoint with a specific ticker as a param
        :param ticker: Ticker to get information for.
        :return:
        """
        response = self.get(endpoint=f"{TickerEndpoint.TICKERS.value}{ticker}")
        return response.json()


if __name__ == "__main__":
    # Example usage
    import os
    import dotenv

    dotenv.load_dotenv("/Users/peter/Repositories/StockMarketWebApp/secrets.env")

    tickers = Tickers(api_key=os.getenv("POLYGON_API_KEY"))
    specific_ticker_info = tickers.get_specific_ticker(ticker="AAPL")
    print(specific_ticker_info)
