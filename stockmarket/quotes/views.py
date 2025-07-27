from django.shortcuts import render


def home(request):
    """
    Render the home page of the stock market application.
    Args:
        request: The HTTP request object.
    Returns:
        HttpResponse: Rendered home page template.
    """
    return render(request, 'home.html', {})


def about(request):
    """
    Render the about page of the stock market application.
    Args:
        request: The HTTP request object.
    Returns:
        HttpResponse: Rendered about page template.
    """
    return render(request, 'about.html', {})
