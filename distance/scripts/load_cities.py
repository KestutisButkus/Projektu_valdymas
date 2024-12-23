import csv
import os
from distance.models import City

def load_cities_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['City']
            coordinates = row['Coordinates']
            latitude, longitude = map(float, coordinates.strip('()').split(', '))
            city, created = City.objects.get_or_create(
                name=name,
                latitude=latitude,
                longitude=longitude
            )
            if created:
                print(f'City {city.name} added to the database.')

def run():
    # Paimame cities.csv failą iš ProMgt katalogo, kuriame yra manage.py
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    csv_file_path = os.path.join(base_dir, 'cities.csv')
    load_cities_from_csv(csv_file_path)
