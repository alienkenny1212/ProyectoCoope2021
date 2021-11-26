from django.db import models
from django.utils import timezone

# Crear modelo
class Persona(models.Model):
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    CUI = models.CharField(max_length=13)
    born_date = models.DateField()
    Genre = models.CharField(max_length=9)

    def __str__(self):
        return self.Nombres + ' ' +self.Apellidos
    
# Crear modelo Socio

class Socio(models.Model):
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Afiliacion_date = models.DateField()
    Genre = models.CharField(max_length=9)
    Codigo_Socio = models.CharField(max_length=100)
    Cantidad_propiedad = models.DecimalField

    def __str__(self):
        return self.Nombres + ' ' +self.Apellidos