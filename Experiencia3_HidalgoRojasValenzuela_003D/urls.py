
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GreenPanda.urls')),
    path('Productos/', include('GreenPanda.urls')),
    path('QuienesSomos/', include('GreenPanda.urls')),
    path('Registro/', include('GreenPanda.urls')),
    path('Despacho/', include('GreenPanda.urls')),
    path('Comentarios/', include('GreenPanda.urls')),
    path('CrearComentario/', include('GreenPanda.urls'))
]
