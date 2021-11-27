from django.shortcuts import render
from django.utils import timezone
from .models import Socio
from .forms import PostForm_Socio
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
#Vistas de socios
def post_list_Socios(request):
    socios = Socio.objects.filter(Afiliacion_date__lte=timezone.now()).order_by('Afiliacion_date')
    return render(request, 'Socios/post_list_Socios.html', {'socios': socios})
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

def post_detail_Socios(request, pk):
    socios = get_object_or_404(Socio, pk=pk)
    return render(request, 'Socios/post_detail_Socios.html', {'socios': socios})

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
   
    