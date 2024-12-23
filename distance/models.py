from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)  # Miesto pavadinimas
    latitude = models.FloatField()  # Platuma
    longitude = models.FloatField()  # Ilguma

    def __str__(self):
        return self.name
