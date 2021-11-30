from django.contrib import admin
from .models import Persona
from .models import Socio
from .models import Empleado
from .models import Tecnico
from .models import Inspector

admin.site.register(Persona)
admin.site.register(Socio)
admin.site.register(Empleado)
admin.site.register(Tecnico)
admin.site.register(Inspector)