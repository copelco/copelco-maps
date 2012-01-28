copelco-maps
============

Simple project to play around with Shapefiles, GeoDjango, and Google Maps.

Local Development Setup
-----------------------

Setup your local environment like so::

    $ mkvirtualenv --distribute -p python2.6 elections
    $ pip install --no-index --find-links=file:$PWD/requirements/sdists/ -r requirements/apps.txt
    $ createdb --template=template_postgis elections_devel

Useful sites
------------

Some useful sites I found while Googling around:

* http://iknuth.com/2010/04/displaying-a-google-maps-api-v3-map-in-a-django-application-with-geodjango-and-postgis/
* http://www.geocodezip.com/
* http://ajpiano.com/widgetfactory/#slide20
