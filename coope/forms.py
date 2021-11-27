from django import forms
from .models import Persona
from .models import Socio
from .models import Empleado

class PostForm_Socio(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ('Nombres', 'Apellidos','Afiliacion_date', 'Genre','Codigo_Socio', 'Cantidad_propiedad',)

class PostForm_Persona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('Nombres', 'Apellidos','CUI', 'born_date','Genre',)

class PostForm_Empleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('Nombres', 'Apellidos','CUI', 'FechaNac','Genre', 'Estado', 'User', 'Password', 'Puesto',)