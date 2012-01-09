from django.contrib.gis import admin
from shapefiles.models import Location


class LocationAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'type', 'area')
    list_filter = ('type',)
    search_fields = ('name',)


admin.site.register(Location, LocationAdmin)
