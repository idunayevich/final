from django.contrib import admin
from .models import Persona, Restaurante, Reserva

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'email')

@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_comida', 'direccion', 'horario')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('dia', 'hora', 'cant_personas')