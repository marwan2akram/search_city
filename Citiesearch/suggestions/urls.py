from django.urls import path, include
# from .views import CitiesSearch
from . import views

app_name = "suggestions"

urlpatterns = [
    path('', views.get_cities, name='list_cities'),
]