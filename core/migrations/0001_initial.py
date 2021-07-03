# Generated by Django 3.2.3 on 2021-07-02 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='Rut del colaborador')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre completo')),
                ('telefono', models.CharField(max_length=9, verbose_name='Numero de contacto')),
                ('direccion', models.CharField(max_length=50, verbose_name='Dirección')),
                ('email', models.CharField(max_length=100, verbose_name='Correo electronico')),
                ('pais', models.CharField(max_length=20, verbose_name='País')),
                ('contraseña', models.CharField(max_length=20, verbose_name='Contraseña')),
            ],
        ),
    ]