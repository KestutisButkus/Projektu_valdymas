# from django import forms
# from .models import Project
#
# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['name', 'start_date', 'end_date', 'client', 'employees']

from django import forms  # Importuoja forms modulį iš Django
from .models import Project  # Importuoja Project modelį iš dabartinio programos katalogo

# Sukuria naują klasę ProjectForm, kuri paveldi iš forms.ModelForm
class ProjectForm(forms.ModelForm):
    # Meta klasė pateikia modelio formų metainformaciją
    class Meta:
        model = Project  # Nurodo, kad ši forma susieta su Project modeliu
        fields = ['name', 'start_date', 'end_date', 'client', 'employees', 'description', 'photo']  # Nurodo, kurie laukai iš Project modelio turi būti įtraukti į formą
