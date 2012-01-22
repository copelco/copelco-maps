import logging

from django.contrib.gis.geos import MultiPolygon, Polygon

from tastypie.cache import SimpleCache
from tastypie.resources import ModelResource

from shapefiles.models import Location


logger = logging.getLogger('shapefiles.api')


class LocationResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'
        allowed_methods = ['get']
        filtering = {
            'type': ['exact'],
        }
        # cache = SimpleCache()
        limit = 200

    def _log_geom(self, geom):
        msg = '{0} with {1} geometries and {2} coords'
        logger.debug(msg.format(geom.geom_type, geom.num_geom,
                                geom.num_coords))

    def dehydrate_geometry(self, bundle):
        logger.debug(bundle.obj.name)
        geom = bundle.obj.geometry
        self._log_geom(geom)
        logger.debug('Simplifying geometry...')
        geom = bundle.obj.geometry.simplify(0.0005, preserve_topology=True)
        self._log_geom(geom)
        if geom.geom_type != 'MultiPolygon':
            logger.debug('Converting back to MultiPolygon')
            geom = MultiPolygon(geom)
            self._log_geom(geom)
        return geom.coords
