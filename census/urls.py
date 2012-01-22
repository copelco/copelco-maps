from django.conf.urls import patterns, include, url

from census.api import PopulationResource

from django.views.generic import TemplateView


entry_resource = PopulationResource()

urlpatterns = patterns('',
    url(r'^api/', include(entry_resource.urls)),
    url(r'^population/$',
        TemplateView.as_view(template_name='census/population.html'),
        name='population'),
)
