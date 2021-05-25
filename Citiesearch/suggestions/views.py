from .models import Cities
from django.http import HttpResponse, JsonResponse
from .serializers import CitiesSerializer
from difflib import SequenceMatcher
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from math import sqrt


# Scoring function that return score based on lat, and lng.
def match_score(lat1, lng1, one_city):
    lat2 = float(one_city.lat)
    lng2 = float(one_city.lng)
    score_latitude = 0.0
    score_longitude = 0.0
    if lat1 <= lat2:
        score_lat = lat1 / sqrt(lat1 * lat2)
        score_latitude = score_lat
    elif lat1 > lat2:
        score_lat = lat2 / sqrt(lat1 * lat2)
        score_latitude = score_lat
    if lng1 >= lng2:
        score_lng = lng1 / sqrt(lng1 * lng2)
        score_longitude = score_lng
    elif lng1 < lng2:
        score_lng = lng2 / sqrt(lng1 * lng2)
        score_longitude = score_lng
    abs_score_lng = abs(score_longitude)
    total_score = ((score_latitude + abs_score_lng) / 2)
    return total_score


# Create an endpoint to handle GET requests
# That provides auto-complete suggestions for large cities.
@api_view(['GET'])
def get_cities(request):
    city = request.GET.get('q')
    lat = request.GET.get('latitude')
    lng = request.GET.get('longitude')
    cities_list = []

    if city:
        cities = Cities.objects.raw('SELECT * FROM suggestions_cities WHERE city LIKE %s', ["%" + city + "%"])

        if lat and lng:
            lat1 = float(lat)
            lng1 = float(lng)
            for one_city in cities:
                score_based_on_lng_lat = match_score(lat1, lng1, one_city)
                city_data = {
                    "city": one_city.city,
                    "city_ascii": one_city.city_ascii,
                    "province_id": one_city.province_id,
                    "province_name": one_city.province_name,
                    "lat": one_city.lat,
                    "lng": one_city.lng,
                    "score": round(score_based_on_lng_lat, 3)
                }
                cities_list.append(city_data)
            cities_list_ordered = sorted(cities_list, key=lambda i: i['score'], reverse=True)

            return Response(cities_list_ordered)

        for one_city in cities:
            seq = SequenceMatcher(a=city, b=one_city.city)
            answer = seq.ratio()
            score = round(answer, 2)
            city_data = {
                "id": one_city.id,
                "city": one_city.city,
                "city_ascii": one_city.city_ascii,
                "province_id": one_city.province_id,
                "province_name": one_city.province_name,
                "lat": one_city.lat,
                "lng": one_city.lng,
                "score": score
            }
            cities_list.append(city_data)
        cities_list_ordered = sorted(cities_list, key=lambda i: i['score'], reverse=True)
        return Response(cities_list_ordered)
    response = HttpResponse(" You didn't enter the city name")
    response.status_code = 422
    return Response({"detail": "You didn't enter the city name"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)