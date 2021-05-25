import json
from .models import Cities
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from .serializers import *
import pdb


class CityCreateAPIViewTestCase(APITestCase):
    list_cities = reverse("suggestions:list_cities")

    def setUp(self):
        # Create two cities, Both city names begin with "Lon"
        self.city1 = Cities.objects.create(
            id=1,
            city="London",
            city_ascii="London",
            province_id="ON",
            province_name="Ontario",
            lat="42.9836",
            lng="-81.2497",
            population=383822,
            density=913.1,
            timezone="America/Toronto",
            ranking=2,
            postal="N5Z N5X N5Y N5V N5W N6A",
            city_id=1124469960,
        )
        self.city2 = Cities.objects.create(
            id=2,
            city="Longueuil",
            city_ascii="Longueuil",
            province_id="QC",
            province_name="Quebec",
            lat="45.5333",
            lng="-73.5167",
            population=239700,
            density=2002,
            timezone="America/Montreal",
            ranking=2,
            postal="N5Z N5X N5Y N5V N5W N6A",
            city_id=1124122753,
        )

    # Test searching by only q = Longueuil
    def test_search_city_by_q(self):
        response = self.client.get(self.list_cities + '?q=Longueuil')
        response_body = json.loads(response.content)[0]
        # pdb.set_trace()
        self.assertEqual(200, response.status_code)
        self.assertEqual('Longueuil', response_body['city'])

    # Test searching by q = Longueuil, latitude, and, longitude
    def test_search_city_q_lan_lng(self):
        response = self.client.get(self.list_cities + '?q=Lon&latitude=42.9836&longitude=-81.2497')
        response_body = json.loads(response.content)[0]
        self.assertEqual(200, response.status_code)
        self.assertEqual('London', response_body['city'])

    # Test searching without any parameters
    def test_invalid_search_city(self):
        response = self.client.get(self.list_cities)
        self.assertEqual(422, response.status_code)
        self.assertEqual(b'{"detail":"You didn\'t enter the city name"}', response.content)