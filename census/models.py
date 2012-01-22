from django.db import models

from shapefiles.models import Location


class Population(models.Model):
    location = models.ForeignKey(Location)
    name = models.CharField(max_length=255)
    date = models.DateField()
    total = models.PositiveIntegerField()
