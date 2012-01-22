from django.contrib import admin

from census.models import Population


class PopulationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'total', 'date')


admin.site.register(Population, PopulationAdmin)
