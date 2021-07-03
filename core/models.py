from django.db import models

# Create your models here.

class Colaborador(models.Model):
    rut=models.CharField(primary_key=True, max_length=9, verbose_name='Rut del colaborador')

    nombre=models.CharField(max_length=100, verbose_name='Nombre completo')
    telefono=models.CharField(max_length=9, verbose_name='Numero de contacto')
    direccion=models.CharField(max_length=50, verbose_name='Dirección')
    email=models.CharField(max_length=100, verbose_name='Correo electronico')
    pais=models.CharField(max_length=20, verbose_name='País')
    contraseña=models.CharField(max_length=20, verbose_name='Contraseña')

    def __str__(self):
        return(self.rut)