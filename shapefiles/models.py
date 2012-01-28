from django.contrib.gis.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    area = models.FloatField()
    geometry = models.MultiPolygonField()

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=255)
    point = models.PointField()
    address = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
