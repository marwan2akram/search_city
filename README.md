# search_city

[search_city](http://ec2-18-221-166-31.us-east-2.compute.amazonaws.com/suggestions/) 
is DRF app that provides REST API endpoint to auto-complete suggestions for large cities.


# Requirements

* Python (3.5, 3.6, 3.7, 3.8, 3.9)
* Django (2.2, 3.0, 3.1)

it's **highly recommend** and only officially support the latest patch release of
each Python and Django series.

# Installation DRF

Install using `pip`...

    pip install djangorestframework
    pip install django-filter  # Filtering support

Add `'rest_framework'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = [
        ...
        'rest_framework',
    ]

# Creating Migrations


	* python manage.py makemigrations
   
	* python manage.py migrate
   
# Run Server


	* python manage.py runserver

# create superuser


	* python manage.py createsuperuser

# Testing
To run the tests, run


	* python manage.py test

# Data 
You can find a CSV file **canadacities.csv** to use

To import the data from the **canadacities.csv** file to 
**suggestions_cities** table:

    * COPY suggestions_cities
    FROM '/home/user/projectpath/canadacities.csv'
    DELIMITER ',' CSV HEADER;


# Database

    DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'data base name',
         'USER': 'user name',
         'PASSWORD': 'user password',
         'HOST': 'localhost'
    ec2-18-221-166-31.us-east-2.compute.amazonaws.com
     }
 }

# AWS Public DNS

    ec2-18-221-166-31.us-east-2.compute.amazonaws.com

# Endpoints
```

GET /suggestions

```

# examples

    GET /suggestions/?q=Lon&latitude=43.70011&longitude=-79.4163

    Request parameter: q, latitude, longitude
-Returns:
```
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

[
    {
        "city": "London",
        "city_ascii": "London",
        "province_id": "ON",
        "province_name": "Ontario",
        "lat": "42.9836",
        "lng": "-81.2497",
        "score": 0.99
    },
    {
        "city": "Longueuil",
        "city_ascii": "Longueuil",
        "province_id": "QC",
        "province_name": "Quebec",
        "lat": "45.5333",
        "lng": "-73.5167",
        "score": 0.971
    },
    {
        "city": "Longue-Rive",
        "city_ascii": "Longue-Rive",
        "province_id": "QC",
        "province_name": "Quebec",
        "lat": "48.55",
        "lng": "-69.25",
        "score": 0.941
    },
    {
        "city": "Longlaketon No. 219",
        "city_ascii": "Longlaketon No. 219",
        "province_id": "SK",
        "province_name": "Saskatchewan",
        "lat": "50.9386",
        "lng": "-104.6913",
        "score": 0.899
    }
]



```

    GET /suggestions/?q=Del

    Request parameter: q


-Returns:
```

HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

[
    {
        "id": 54,
        "city": "Delta",
        "city_ascii": "Delta",
        "province_id": "BC",
        "province_name": "British Columbia",
        "lat": "49.0847",
        "lng": "-123.0586",
        "score": 0.75
    },
    {
        "id": 474,
        "city": "Delson",
        "city_ascii": "Delson",
        "province_id": "QC",
        "province_name": "Quebec",
        "lat": "45.37",
        "lng": "-73.55",
        "score": 0.67
    },
    {
        "id": 1707,
        "city": "Delisle",
        "city_ascii": "Delisle",
        "province_id": "SK",
        "province_name": "Saskatchewan",
        "lat": "51.9254",
        "lng": "-107.1333",
        "score": 0.6
    },
    {
        "id": 1107,
        "city": "Deloraine-Winchester",
        "city_ascii": "Deloraine-Winchester",
        "province_id": "MB",
        "province_name": "Manitoba",
        "lat": "49.1775",
        "lng": "-100.4322",
        "score": 0.26
    }
]
```


    GET /suggestions?q=SomeRandomCityInTheMiddleOfNowhere

-Returns:
```
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

[]
```

    GET /suggestions

-Returns:
```

HTTP 422 Unprocessable Entity
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

{
    "detail": "You didn't enter the city name"
}
```






























