from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Client(models.Model):
    first_name = models.CharField(max_length=100)  # Vardas
    last_name = models.CharField(max_length=100)  # Pavardė
    company = models.CharField(max_length=255, blank=True)  # Įmonė
    email = models.EmailField(unique=True)  # El. paštas
    phone = models.CharField(max_length=20, blank=True)  # Telefonas
    address = models.TextField(blank=True)  # Adresas

    def __str__(self):
        return f"{self.company}"

class Employee(models.Model):
    first_name = models.CharField(max_length=100)  # Vardas
    last_name = models.CharField(max_length=100)  # Pavardė
    position = models.CharField(max_length=255)  # Pareigos
    photo = models.ImageField(upload_to="employee_photos/", blank=True, null=True)  # Nuotrauka

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size, Image.Resampling.LANCZOS)
                img.save(self.photo.path)

class Project(models.Model):
    name = models.CharField(max_length=255)  # Pavadinimas
    start_date = models.DateField()  # Pradžios data
    end_date = models.DateField(blank=True, null=True)  # Pabaigos data
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="projects")  # Klientas
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="managed_projects")  # Atsakingasis/vadovas
    employees = models.ManyToManyField(Employee, related_name="projects")  # Darbuotojai
    tasks = models.ManyToManyField('Task', related_name='project_tasks')  # Darbai
    invoices = models.ManyToManyField('Invoice', related_name='project_invoices')  # Sąskaitos
    photo = models.ImageField(upload_to='project_photos/', blank=True, null=True)  # Pridėtas nuotraukos laukas
    description = HTMLField(blank=True, null=True)  # HTML aprašymo laukas

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size, Image.Resampling.LANCZOS)
                img.save(self.photo.path)



class Task(models.Model):
    name = models.CharField(max_length=255)  # Pavadinimas
    description = models.TextField(blank=True)  # Pastabos

    def __str__(self):
        return self.name


class Invoice(models.Model):
    date_issued = models.DateField()  # Išrašymo data
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Suma

    def __str__(self):
        return f"Invoice {self.id}"


"""
Projektas
    -Pavadinimas
    -Pradžios data
    -Pabaigos data
    -Klientas (ryšys su Klientas)
    -Atsakingasis/vadovas (ryšys su User)
    -Darbuotojai (ryšys su Darbuotojas)
    -Darbai (ryšys su Darbas)
    -Sąskaitos (ryšys su Sąskaita)
Klientas
    -Vardas
    -Pavardė
    -Įmonė
    -Kontaktai (galima išskirstyti į atskirus laukus)
Darbuotojas
    -Vardas
    -Pavardė
    -Pareigos
    -Nuotrauka
Darbas
    -Pavadinimas
    -Pastabos
Sąskaita
    -Išrašymo data
    -Suma
"""