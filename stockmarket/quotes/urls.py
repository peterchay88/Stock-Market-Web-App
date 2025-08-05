from django.urls import path
from . import views as view


urlpatterns = [
    path('', view.home, name='home'),
    path('about/', view.about, name='about'),
    path('add_stock/', view.add_stock, name='add_stock'),
]
