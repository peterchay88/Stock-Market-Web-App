from django.shortcuts import render
from . polygon.tickers import Tickers
import dotenv
import os

# TODO: Refactor how we load the secrets file
dotenv.load_dotenv("/Users/peter/Repositories/StockMarketWebApp/secrets.env")


def home(request):
    """
    Render the home page of the stock market application.
    Args:
        request: The HTTP request object.
    Returns:
        HttpResponse: Rendered home page template.
    """
    ticker = Tickers(api_key=os.getenv("POLYGON_API_KEY"))
    api_response = ticker.get_specific_ticker(ticker="AAPL")
    return render(request, 'home.html', {'api_response': api_response})


def about(request):
    """
    Render the about page of the stock market application.
    Args:
        request: The HTTP request object.
    Returns:
        HttpResponse: Rendered about page template.
    """
    return render(request, 'about.html', {})
