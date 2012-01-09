Local Development Setup
-----------------------

::

    $ mkvirtualenv --distribute -p python2.6 elections
    $ pip install --no-index --find-links=file:$PWD/requirements/sdists/ -r requirements/apps.txt

    $ createdb --template=template_postgis elections_devel

Useful sites
------------

# http://iknuth.com/2010/04/displaying-a-google-maps-api-v3-map-in-a-django-application-with-geodjango-and-postgis/
# http://www.geocodezip.com/
