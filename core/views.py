from django.shortcuts import render, redirect
from .models import Colaborador
from .forms import ColaboradorForm

# Create your views here.
def menuprincipal(request):
    return render(request, 'menuprincipal.html')

def galeria(request):
    return render(request, 'galeria.html')

def form_noticias(request):
    if request.method=='GET':
        formulario=ColaboradorForm()
        contexto={
            'formulario':formulario
        }
    else:
        formulario=ColaboradorForm(request.POST)
        contexto={
            'formulario':formulario
        }
    if formulario.is_valid():
        formulario.save()
        return redirect('gestion_noticias')

    return render(request, 'core/form_noticias.html', {'formulario':formulario})

def gestion_noticias(request):
    colaborador=Colaborador.objects.all()
    return render(request, 'core/gestion_noticias.html' , context={'colab':colaborador})

def form_del_colab(request,id):
    colaborador = Colaborador.objects.get(rut=id)
    colaborador.delete()
    return redirect('gestion_noticias')

def form_mod(request,id):
    colaborador = Colaborador.objects.get(rut=id)

    datos ={
        'form': ColaboradorForm(instance=colaborador)
    }
    if request.method == 'POST': 
        formulario = ColaboradorForm(data=request.POST, instance = colaborador)
        if formulario.is_valid: 
            formulario.save()           #permite actualizar la info del objeto encontrado
            return redirect('gestion_noticias')
    return render(request, 'core/form_mod.html', datos)
