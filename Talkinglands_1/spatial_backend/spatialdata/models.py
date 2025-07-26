
from django.db import models

class PointData(models.Model):
    name = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.name

class PolygonData(models.Model):
    name = models.CharField(max_length=100)
    coordinates = models.JSONField()  # e.g. [[lng, lat], [lng, lat], ...]

    def __str__(self):
        return self.name

