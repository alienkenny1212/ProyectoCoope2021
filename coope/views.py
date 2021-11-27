from django.shortcuts import render
from django.utils import timezone
from .models import Socio
# Create your views here.
def post_list_Socios(request):
    socios = Socio.objects.filter(Afiliacion_date__lte=timezone.now()).order_by('Afiliacion_date')
    return render(request, 'Socios/post_list_Socios.html', {'socios': socios})