import logging

from tastypie.resources import ModelResource
from tastypie import fields

from django.contrib.gis.geos import MultiPolygon, Polygon
from django.db.models import Sum

from census.models import Population

from shapefiles.models import Location
from shapefiles.api import LocationResource


logger = logging.getLogger('census.api')


class PopulationResource(ModelResource):
    location = fields.ForeignKey(LocationResource, 'location')
    geometry = fields.ListField()
    percent = fields.DecimalField()

    class Meta:
        queryset = Population.objects.all()
        resource_name = 'population'
        allowed_methods = ['get']
        limit = 200

    def dehydrate_geometry(self, bundle):
        logger.debug(bundle.obj.name)
        geom = bundle.obj.location.geometry.simplify(0.0005,
                                                     preserve_topology=True)
        if geom.geom_type != 'MultiPolygon':
            logger.debug('Converting back to MultiPolygon')
            geom = MultiPolygon(geom)
        return geom.coords

    def dehydrate_percent(self, bundle):
        max_val = Population.objects.order_by('-total')[0].total * 1.0
        # total = Population.objects.aggregate(sum=Sum('total'))['sum'] * 1.0
        percent = bundle.obj.total / max_val
        print bundle.obj.total, max_val, percent
        return percent
