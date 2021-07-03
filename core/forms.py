from django import forms
from django.forms import ModelForm,widgets
from .models import Colaborador

class ColaboradorForm(ModelForm):
    class Meta:
        model = Colaborador
        fields = ['rut','nombre','telefono','direccion','email','pais','contraseña']
        labels={
            'rut':'RUT',
            'nombre':'Nombre de usuario',
            'telefono':'Teléfono',
            'direccion':'Dirección',
            'email':'Correo Electronico',
            'pais':'País',
            'contraseña':'Contraseña'
        }

        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'name': 'rut',
                    'id': 'rut',
                    'placeholder': 'RUT'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'name': 'nombre',
                    'id': 'nombre',
                    'placeholder': 'Nombre de usuario'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'telefono',
                    'name': 'telefono',
                    'placeholder': 'Número de contacto',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'name': 'direccion',
                    'id': 'direccion',
                    'placeholder': 'Ingrese su dirección'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'email',
                    'name': 'email',
                    'placeholder': 'Nombre@dominio.cl'
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'pais',
                    'name': 'pais',
                    'placeholder': 'Ingrese su País',
                }
            ),
            'contraseña': forms.TextInput(
                attrs={
                    'class': 'controls',
                    'id': 'contraseña',
                    'name': 'contraseña',
                    'placeholder': 'Ingrese su contraseña'
                }
            ),
         
        }