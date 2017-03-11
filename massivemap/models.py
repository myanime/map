
from django.db import models
from django.contrib.gis.db import models as gismodels


class WeatherStation(gismodels.Model):
    name = models.CharField(max_length=256)
    geom = gismodels.PointField()

    objects = gismodels.GeoManager()

    def __unicode__(self):
        return self.name

