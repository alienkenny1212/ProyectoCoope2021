from django.db import models
from django.utils import timezone

# Create your models here.
class Persona(models.Model):
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    CUI = models.CharField(max_length=13)
    born_date = models.DateField()
    Genre = models.CharField(max_length=9)

    def __str__(self):
        return self.Nombres + ' ' +self.Apellidos