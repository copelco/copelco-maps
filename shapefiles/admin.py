from django.contrib.gis import admin
from shapefiles.models import Location, Place


class LocationAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'type', 'area')
    list_filter = ('type',)
    search_fields = ('name',)


class PlaceAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'address', 'point')
    search_fields = ('name',)
    default_zoom = 20


admin.site.register(Location, LocationAdmin)
admin.site.register(Place, PlaceAdmin)
