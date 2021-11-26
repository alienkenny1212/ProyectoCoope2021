from django.shortcuts import render

# Create your views here.
def post_list_Socios(request):
    return render(request, 'Socios/post_list_Socios.html', {})