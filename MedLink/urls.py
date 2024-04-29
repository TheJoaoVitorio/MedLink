#
from django.contrib import admin
from django.urls import path,include  #include inclui outras urls dentro de uma url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')), #dentro desse path tem outras urls, como a de cadastro/
    path('medico/', include('medico.urls')),
    path('', include('usuarios.urls')),
    path('pacientes/', include('pacientes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)