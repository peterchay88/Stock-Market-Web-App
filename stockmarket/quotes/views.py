from django.shortcuts import render
from . polygon.tickers import Tickers
import dotenv
import os

# TODO: Refactor how we load the secrets file, currently only works on my local machine
dotenv.load_dotenv("/Users/peter/Repositories/StockMarketWebApp/secrets.env")


def home(request):
    """
    Render the home page of the stock market application.
    Args:
        request: The HTTP request object.
    Returns:
        HttpResponse: Rendered home page template.
    """
    if request.method == 'POST':
        search_ticker = request.POST['ticker']
        ticker = Tickers(api_key=os.getenv("POLYGON_API_KEY"))
        api_response = ticker.get_specific_ticker(ticker=search_ticker.upper())
        return render(
            request=request,
            template_name='home.html',
            context={'api_response': api_response['results']}
        )
    else:
        return render(
            request=request,
            template_name='home.html',
            context={'No_ticker': "Enter a ticker symbol to get information"}
        )


def about(request):
    """
    Render the about page of the stock market application.
    Args:
        request: The HTTP request object.
    Returns:
        HttpResponse: Rendered about page template.
    """
    return render(
        request,
        template_name='about.html',
        context={}
    )
