# -*- coding: utf-8 -*-
from django.db import models
from users.models import Persona
# Create your models here.


class Categoria(models.Model):
    nombre=models.CharField(max_length=30, verbose_name='nombre')

    def __str__(self):
        return self.nombre


class Recurso(models.Model):
    nombre=models.CharField(max_length=30, verbose_name='nombre')
    codigo=models.CharField(max_length=5, verbose_name='codigo')
    marca=models.CharField(max_length=15, verbose_name='marca')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    persona_asignada=models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True)
    fecha_asignacion=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.nombre
