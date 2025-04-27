from django import forms
from .models import Persona, Restaurante, Reserva

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'