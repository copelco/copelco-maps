from django.conf.urls import patterns, include, url

from shapefiles import views


urlpatterns = patterns('',
    url(r'^type/$',
        views.TypeList.as_view(), name='list-types'),
    url(r'^type/(?P<location_type>[\w-]+)/$',
        views.LocationList.as_view(), name='list-locations'),
    url(r'^type/(?P<location_type>[\w-]+)/(?P<pk>\d+)/$',
        views.LocationView.as_view(), name='view-location'),
    url(r'^preview/(?P<location_type>[\w-]+)/(?P<location_id>\d+)/$',
        views.preview,
        name='preview'),
)
