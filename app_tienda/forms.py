from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre', 'edad', 'peso', 'cuidados', 'enfermedades', 'especie', 'alimentacion', 'foto_animal', 'id_proveedor']