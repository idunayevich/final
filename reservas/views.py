from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Persona, Restaurante, Reserva
from .forms import PersonaForm, RestauranteForm, ReservaForm

# Persona Views
class PersonaListView(LoginRequiredMixin, ListView):
    model = Persona
    template_name = 'reservas/persona_list.html'
    context_object_name = 'personas'

class PersonaCreateView(LoginRequiredMixin, CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'reservas/persona_form.html'
    success_url = reverse_lazy('reservas:persona_list')

class PersonaUpdateView(LoginRequiredMixin, UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'reservas/persona_form.html'
    success_url = reverse_lazy('reservas:persona_list')

class PersonaDeleteView(LoginRequiredMixin, DeleteView):
    model = Persona
    template_name = 'reservas/persona_confirm_delete.html'
    success_url = reverse_lazy('reservas:persona_list')

# Restaurante Views
class RestauranteListView(LoginRequiredMixin, ListView):
    model = Restaurante
    template_name = 'reservas/restaurante_list.html'
    context_object_name = 'restaurantes'

class RestauranteCreateView(LoginRequiredMixin, CreateView):
    model = Restaurante
    form_class = RestauranteForm
    template_name = 'reservas/restaurante_form.html'
    success_url = reverse_lazy('reservas:restaurante_list')

class RestauranteUpdateView(LoginRequiredMixin, UpdateView):
    model = Restaurante
    form_class = RestauranteForm
    template_name = 'reservas/restaurante_form.html'
    success_url = reverse_lazy('reservas:restaurante_list')

class RestauranteDeleteView(LoginRequiredMixin, DeleteView):
    model = Restaurante
    template_name = 'reservas/restaurante_confirm_delete.html'
    success_url = reverse_lazy('reservas:restaurante_list')

# Reserva Views
class ReservaListView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'reservas/reserva_list.html'
    context_object_name = 'reservas'

class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservas/reserva_form.html'
    success_url = reverse_lazy('reservas:reserva_list')

class ReservaUpdateView(LoginRequiredMixin, UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservas/reserva_form.html'
    success_url = reverse_lazy('reservas:reserva_list')

class ReservaDeleteView(LoginRequiredMixin, DeleteView):
    model = Reserva
    template_name = 'reservas/reserva_confirm_delete.html'
    success_url = reverse_lazy('reservas:reserva_list')