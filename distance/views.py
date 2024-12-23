from django.shortcuts import render
from math import radians, sin, cos, sqrt, atan2
from .models import City
from .forms import CityDistanceForm

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Žemės spindulys kilometrais
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def city_distance_view(request):
    form = CityDistanceForm()
    closest_city = None
    distances = []

    if request.method == 'POST':
        form = CityDistanceForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']

            for city in City.objects.all():
                distance = calculate_distance(latitude, longitude, city.latitude, city.longitude)
                # Suapvaliname iki vieno skaitmens po kablelio
                distances.append((city.name, round(distance, 1)))

            distances.sort(key=lambda x: x[1])
            closest_city = distances[0]

    return render(request, 'main.html', {
        'form': form,
        'distances': distances,
        'closest_city': closest_city,
    })
