from re import L
from django.shortcuts import render
from django.utils import timezone
from .models import Socio
from .models import Persona
from .models import Empleado
from .models import Tecnico
from .forms import PostForm_Persona, PostForm_Socio, PostForm_Empleado, PostForm_Tecnico
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

# Create your views here.

def menu_principal(request):
    return render(request, 'index.html')

#SOCIOS By Julio Ve
#
#
#
def post_list_Socios(request):
    socios = Socio.objects.filter(Afiliacion_date__lte=timezone.now()).order_by('Afiliacion_date')
    return render(request, 'Socios/post_list_Socios.html', {'socios': socios})

def post_detail_Socios(request, pk):
    socios = get_object_or_404(Socio, pk=pk)
    return render(request, 'Socios/post_detail_Socios.html', {'socios': socios})

def post_new_Socios(request):
    if request.method == "POST":
        form = PostForm_Socio(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail_socios', pk=post.pk)
    else:
        form = PostForm_Socio()
    return render(request, 'Socios/post_new_Socios.html', {'form': form})

def post_edit_socios(request, pk):
    post = get_object_or_404(Socio, pk=pk)
    if request.method == "POST":
        form = PostForm_Socio(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail_socios', pk=post.pk)
    else:
        form = PostForm_Socio(instance=post)
    return render(request, 'Socios/post_new_Socios.html', {'form': form})

def post_delete_socios(request, pk):
    socios = Socio.objects.get(pk=pk)
    if request.method =="POST":
            socios.delete()
            return redirect('/Socios')
    return render(request, 'Socios/post_delete_Socios.html', {'socios': socios})
#
#
#
#
#SOCIOS 

#PERSONAS
#
#
#
def post_list_personas(request):
    personas = Persona.objects.order_by('born_date')
    return render(request, 'Personas/post_list_personas.html', {'personas': personas})

def post_detail_persona(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    return render(request, 'Personas/post_detail_persona.html', {'persona': persona})

def post_new_persona(request):
    if request.method == "POST":
        form = PostForm_Persona(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail_persona', pk=post.pk)
    else:
        form = PostForm_Persona()
    return render(request, 'Personas/post_new_persona.html', {'form': form})

def post_edit_persona(request, pk):
    post = get_object_or_404(Persona, pk=pk)
    if request.method == "POST":
        form = PostForm_Persona(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail_persona', pk=post.pk)
    else:
        form = PostForm_Persona(instance=post)
    return render(request, 'Personas/post_new_persona.html', {'form': form})

def post_delete_persona(request, pk):
    personas = Persona.objects.get(pk=pk)
    if request.method =="POST":
            personas.delete()
            return redirect('/Personas')
    return render(request, 'Personas/post_delete_persona.html', {'personas': personas})
#
#
#
# PERSONAS

#EMPLEADOS
#
#
#
def post_list_empleado(request):
    empleados = Empleado.objects.order_by('FechaNac')
    return render(request, 'Empleados/post_list_Empleados.html', {'empleado': empleados})

def post_detail_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    return render(request, 'Empleados/post_detail_Empleados.html', {'empleado': empleado})


def post_new_empleado(request):
    if request.method == "POST":
        form = PostForm_Empleado(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail_empleado', pk=post.pk)
    else:
        form = PostForm_Empleado()
    return render(request, 'Empleados/post_new_Empleados.html', {'form': form})

def post_edit_empleado(request, pk):
    post = get_object_or_404(Empleado, pk=pk)
    if request.method == "POST":
        form = PostForm_Empleado(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail_empleado', pk=post.pk)
    else:
        form = PostForm_Empleado(instance=post)
    return render(request, 'Empleados/post_new_Empleados.html', {'form': form})

def post_delete_empleado(request, pk):
    empleados = Empleado.objects.get(pk=pk)
    if request.method =="POST":
            empleados.delete()
            return redirect('/Empleados')
    return render(request, 'Empleados/post_delete_Empleados.html', {'empleados': empleados})
#
#
#
# EMPLEADOS

#Tecnico
#
#
#
def post_list_tecnico(request):
    tecnicos = Tecnico.objects.order_by('FechaNac')
    return render(request, 'Tecnicos/post_list_Tecnicos.html', {'tecnicos': tecnicos})

def post_detail_tecnico(request, pk):
    tecnico = get_object_or_404(Tecnico, pk=pk)
    return render(request, 'Tecnicos/post_detail_Tecnicos.html', {'tecnico': tecnico})


def post_new_tecnico(request):
    if request.method == "POST":
        form = PostForm_Tecnico(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail_tecnico', pk=post.pk)
    else:
        form = PostForm_Tecnico()
    return render(request, 'Tecnicos/post_new_Tecnicos.html', {'form': form})

def post_edit_tecnico(request, pk):
    post = get_object_or_404(Tecnico, pk=pk)
    if request.method == "POST":
        form = PostForm_Tecnico(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail_tecnico', pk=post.pk)
    else:
        form = PostForm_Tecnico(instance=post)
    return render(request, 'Tecnicos/post_new_Tecnicos.html', {'form': form})

def post_delete_tecnico(request, pk):
    tecnicos = Tecnico.objects.get(pk=pk)
    if request.method =="POST":
            tecnicos.delete()
            return redirect('/Tecnicos')
    return render(request, 'Tecnicos/post_delete_Tecnicos.html', {'tecnicos': tecnicos})
#
#
#
# Tecnico