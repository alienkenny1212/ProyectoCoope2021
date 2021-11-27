from django.shortcuts import render
from django.utils import timezone
from .models import Socio
from .models import Persona
from .forms import PostForm_Socio
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list_Socios(request):
    socios = Socio.objects.filter(Afiliacion_date__lte=timezone.now()).order_by('Afiliacion_date')
    return render(request, 'Socios/post_list_Socios.html', {'socios': socios})

def post_new_Socios(request):
    form = PostForm_Socio()
    return render(request, 'Socios/post_new_Socios.html', {'form': form})

def post_detail_Socios(request, pk):
    socios = get_object_or_404(Socio, pk=pk)
    return render(request, 'Socios/post_detail_Socios.html', {'socios': socios})

def post_list_personas(request):
    personas = Persona.objects.order_by('born_date')
    return render(request, 'Personas/post_list_personas.html', {'personas': personas})

def post_new_persona(request):
    form = PostForm_Socio()
    return render(request, 'Personas/post_new_persona.html', {'form': form})
    
def post_detail_persona(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    return render(request, 'Personas/post_detail_persona.html', {'persona': persona})