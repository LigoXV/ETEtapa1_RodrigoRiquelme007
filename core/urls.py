from django.urls import path
from .views import menuprincipal, galeria, form_noticias, gestion_noticias, form_mod, form_del_colab

urlpatterns = [
    path('', menuprincipal, name="menuprincipal"),
    path('galeria', galeria, name="galeria"),
    path('form_noticias', form_noticias, name="form_noticias"),
    path('gestion_noticias', gestion_noticias, name="gestion_noticias"),
    path('form_mod/<id>', form_mod, name="form_mod"),
    path('form_del_colab/<id>', form_del_colab, name="form_del_colab"),
]