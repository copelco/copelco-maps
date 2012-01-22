import csv
import datetime

from django.core.management.base import BaseCommand

from shapefiles.models import Location

from census.models import Population


class Command(BaseCommand):
    help = 'Import population CSV'

    def handle(self, csv_file, **options):
        year = datetime.date(2009, 1, 1)
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                county_name = row[0].strip('. ')
                total = row[1].replace(',', '')
                try:
                    location = Location.objects.get(name=county_name)
                except Location.DoesNotExist:
                    print 'Failed to find {0}'.format(county_name)
                    continue
                Population.objects.create(name=county_name, location=location,
                                          date=year, total=total)
