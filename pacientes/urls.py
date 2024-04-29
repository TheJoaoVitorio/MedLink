from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomePaciente , name = 'home'),
    path('escolher_horario/<int:id_dados_medicos>',views.EscolherHorario, name='escolher_horario'),
]
