from django.urls import path
from .views import (
    PersonaListView, PersonaCreateView, PersonaUpdateView, PersonaDeleteView,
    RestauranteListView, RestauranteCreateView, RestauranteUpdateView, RestauranteDeleteView,
    ReservaListView, ReservaCreateView, ReservaUpdateView, ReservaDeleteView,
)

app_name = 'reservas'
urlpatterns = [
    # Persona
    path('personas/', PersonaListView.as_view(), name='persona_list'),
    path('personas/create/', PersonaCreateView.as_view(), name='persona_create'),
    path('personas/<int:pk>/update/', PersonaUpdateView.as_view(), name='persona_update'),
    path('personas/<int:pk>/delete/', PersonaDeleteView.as_view(), name='persona_delete'),
    # Restaurante
    path('restaurantes/', RestauranteListView.as_view(), name='restaurante_list'),
    path('restaurantes/create/', RestauranteCreateView.as_view(), name='restaurante_create'),
    path('restaurantes/<int:pk>/update/', RestauranteUpdateView.as_view(), name='restaurante_update'),
    path('restaurantes/<int:pk>/delete/', RestauranteDeleteView.as_view(), name='restaurante_delete'),
    # Reserva
    path('reservas/', ReservaListView.as_view(), name='reserva_list'),
    path('reservas/create/', ReservaCreateView.as_view(), name='reserva_create'),
    path('reservas/<int:pk>/update/', ReservaUpdateView.as_view(), name='reserva_update'),
    path('reservas/<int:pk>/delete/', ReservaDeleteView.as_view(), name='reserva_delete'),
]