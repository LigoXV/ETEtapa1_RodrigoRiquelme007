from django.shortcuts import render

# Create your views here.
def menuprincipal(request):
    return render(request, 'menuprincipal.html')

def galeria(request):
    return render(request, 'galeria.html')

def form_noticias(request):
    return render(request, 'core/form_noticias.html')

def gestion_noticias(request):
    return render(request, 'core/gestion_noticias.html')