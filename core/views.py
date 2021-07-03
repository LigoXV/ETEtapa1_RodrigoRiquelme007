from django.shortcuts import render
from .models import Colaborador
# Create your views here.
def menuprincipal(request):
    return render(request, 'menuprincipal.html')

def galeria(request):
    return render(request, 'galeria.html')

def form_noticias(request):
    return render(request, 'core/form_noticias.html')

def gestion_noticias(request):
    colaborador=Colaborador.objects.all()
    return render(request, 'core/gestion_noticias.html' , context={'colab':colaborador})

def form_del_colab(request,id):
    colaborador = Colaborador.objects.get(rut=id)
    colaborador.delete()
    return redirect('gestion_noticias')
