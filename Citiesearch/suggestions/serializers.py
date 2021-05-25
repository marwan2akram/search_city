from rest_framework import serializers
from .models import Cities


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ("id","city", "city_ascii", "province_id", "province_name", "lat", "lng")