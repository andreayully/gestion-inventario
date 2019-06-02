# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Persona(User):
    identificacion=models.IntegerField(blank=False, null=False)
    fecha_registro=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.username
