from django import template
from django.contrib.gis.maps.google.overlays import GPolygon
from django.contrib.gis.maps.google.zoom import GoogleZoom
from django.core.cache import cache


register = template.Library()


class Polygon(GPolygon):
    """Extention of GPolygon to support Google Maps v3"""

    def latlng_from_coords(self, coords):
        return '[%s]' % ','.join(['new google.maps.LatLng(%s,%s)' % (y, x) for x, y in coords])


@register.filter(is_safe=True)
def gpolygone(geom):
    key = str(geom.area)
    points = cache.get(key)
    if points is None:
        p = Polygon(geom)
        points = p.points
        cache.set(key, points)
    return points


@register.filter(is_safe=True)
def gzoom(geom):
    gz = GoogleZoom()
    return gz.get_zoom(geom[0])


@register.filter(is_safe=True)
def simplify(geom):
    return geom.simplify(0.005, preserve_topology=True)
