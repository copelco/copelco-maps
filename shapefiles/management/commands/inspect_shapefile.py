import pprint

from django.core.management.base import BaseCommand
from django.contrib.gis.gdal import DataSource


class Command(BaseCommand):
    help = 'Inspect shapefiles'

    def handle(self, shapefile, **options):
        layer = DataSource(shapefile)[0]
        layer_info = {
            'Name': layer.name,
            'Total Features': layer.num_feat,
            'Fields': layer.fields,
            'SRS': layer.srs.name,
        }
        print '-------------------- Layer --------------------'
        pprint.pprint(layer_info)
        feature = layer[0]
        feature_info = {}
        for field in feature:
            feature_info[field.name] = field.value
        print '-------------------- Feature --------------------'
        pprint.pprint(feature_info)
