from optparse import make_option, OptionParser

from django.core.management.base import BaseCommand
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource, OGRGeomType, OGRGeometry

from shapefiles.models import Location


class Command(BaseCommand):
    help = 'Import shapefiles'
    option_list = BaseCommand.option_list + (
        make_option("-n", "--name", action="store", type="string", dest="name"),
    )

    def handle(self, shapefile, **options):
        if options['name']:
            name_field = options['name']
        else:
            name_field = 'NAME'
        layer = DataSource(shapefile)[0]
        Location.objects.filter(type=layer.name).delete()
        for feature in layer:
            print feature
            if feature.geom.geom_type.name != 'MultiPolygon':
                geom = OGRGeometry(OGRGeomType('MultiPolygon'))
                geom.add(feature.geom)
            else:
                geom = feature.geom
            Location.objects.create(name=feature[name_field],
                                    type=layer.name,
                                    area=geom.area,
                                    geometry=geom.wkt)
