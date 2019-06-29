from django.contrib.gis.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    # For the location, you are using the PointField, a GeoDjango-specific geometric field for storing a GEOS Point object that represents a pair of longitude and latitude coordinates.
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)