from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_comida = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    dia = models.DateField()
    hora = models.TimeField()
    cant_personas = models.PositiveIntegerField()

    def __str__(self):
        return f"Reserva {self.dia} {self.hora} - {self.cant_personas} personas"