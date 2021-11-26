from django import forms

from .models import Socio

class PostForm_Socio(forms.ModelForm):

    class Meta:
        model = Socio
        fields = ('Nombres', 'Apellidos','Afiliacion_date', 'Genre','Codigo_Socio', 'Cantidad_propiedad',)