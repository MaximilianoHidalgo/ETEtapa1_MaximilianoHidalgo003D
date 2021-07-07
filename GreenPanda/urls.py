from django.urls import path
from .views import Paginaprincipal, Productos, QuienesSomos, Registro, Despacho, Registros, form_registro
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',Paginaprincipal, name='Paginaprincipal'),
    path('Productos/',Productos, name='Productos'),
    path('QuienesSomos/',QuienesSomos, name='QuienesSomos'),
    path('Registro/',Registro, name='Registro'),
    path('Despacho/',Despacho, name='Despacho'),
    path('Registros/',Registros, name='Registros'),
    path('CrearRegistro/',form_registro, name='CrearRegistro'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)