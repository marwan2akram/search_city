from django.db import models

# Create your models here.


# Create the cities model
class Cities(models.Model):
    city = models.CharField(max_length=120)
    city_ascii = models.CharField(max_length=120)
    province_id = models.CharField(max_length=2)
    province_name = models.CharField(max_length=50)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)
    population = models.FloatField()
    density = models.FloatField()
    timezone = models.CharField(max_length=120)
    ranking = models.IntegerField()
    postal = models.TextField()
    city_id = models.CharField(max_length=10)

    def __str__(self):
        return self.city

