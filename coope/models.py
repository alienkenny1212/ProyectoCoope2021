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
    Cantidad_propiedad = models.CharField(max_length=9)
    def publish(self):
    
        self.save()
    def __str__(self):
        return self.Nombres + ' ' +self.Apellidos

#Crear Modelo Empleado
class Empleado(models.Model):
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    CUI = models.CharField(max_length=17)
    FechaNac = models.DateField()
    Genre = models.CharField(max_length=10)
    User = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Puesto = models.CharField(max_length=60)
    Estado = models.CharField(max_length=60)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.Nombres + ' ' +self.Apellidos


#Crear Modelo Tecnico
class Tecnico(models.Model):
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    CUI = models.CharField(max_length=17)
    FechaNac = models.DateField()
    Genre = models.CharField(max_length=10)
    Codigo_tecnico = models.CharField(max_length=20)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.Nombres + ' ' +self.Apellidos

#Crear Modelo Inspector
class Inspector(models.Model):
    Nombre= models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    CUI = models.CharField(max_length=17)
    FechaN = models.DateField()
    Genero = models.CharField(max_length=10)
    CodigoInsp = models.CharField(max_length=20)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.Nombre + ' ' +self.Apellido