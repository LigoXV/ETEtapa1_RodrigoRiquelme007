from django.urls import path
from .views import menuprincipal, galeria, form_noticias, gestion_noticias

urlpatterns = [
    path('', menuprincipal, name="menuprincipal"),
    path('galeria', galeria, name="galeria"),
    path('form_noticias', form_noticias, name="form_noticias"),
    path('gestion_noticias', gestion_noticias, name="gestion_noticias"),
]