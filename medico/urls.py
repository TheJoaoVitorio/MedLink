from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_medico',views.cadastro_medico , name='cadastro_medico' ),
    path('home/', views.HomeMedico, name='home-medico'),
    path('abrir_horario/',views.AbrirHorario , name='abrir_horario'),
]
