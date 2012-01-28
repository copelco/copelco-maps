from django.conf.urls import patterns, include, url

from directions import views


urlpatterns = patterns('',
    url(r'^$', views.directions, name='view-directions'),
)
