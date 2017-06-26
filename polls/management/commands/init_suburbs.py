import csv

from django.core.management.base import BaseCommand
from meat.models import Suburb


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('common_data/Australian_Post_Codes_Lat_Lon.csv', 'rt') as csvfile:
            headings = ['postcode', 'suburb', 'state', 'dc', 'type', 'lat', 'lon']
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
            next(csv_reader, None)  # skip the headers
            all_postcodes = []
            for row in csv_reader:

                suburb_name = row[headings.index('suburb')]
                suburb_postcode = row[headings.index('postcode')]
                postcode_count = all_postcodes.count(suburb_postcode)

                if postcode_count == 0:
                    all_postcodes.append(suburb_postcode)
                    suburb = Suburb()
                    suburb.name = suburb_name
                    print(suburb)
                    suburb.postcode = row[headings.index('postcode')]
                    suburb.state = row[headings.index('state')]
                    print(row[headings.index('lat')] + row[headings.index('lon')])
                    suburb.latitude = float(row[headings.index('lat')])
                    suburb.longitude = float(row[headings.index('lon')])
                    suburb.save()
