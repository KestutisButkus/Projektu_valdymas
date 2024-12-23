# forms.py
from django import forms

class CityDistanceForm(forms.Form):
    name = forms.CharField(label='City name', max_length=100)
    latitude = forms.FloatField(label='Latitude')
    longitude = forms.FloatField(label='Longitude')
