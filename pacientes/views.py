from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from medico.models import Especialidade , DadosMedico , is_medico
# Create your views here.

@login_required
def HomePaciente(request):

    if request.method == 'GET':
        filtrar_medico = request.GET.get('medico')
        filtrar_especialidade = request.GET.getlist('especialidades')

        medicos = DadosMedico.objects.all()

        if filtrar_medico:
            medicos = medicos.filter(nome__icontains=filtrar_medico)

        if filtrar_especialidade:
            medicos = medicos.filter(especialidade_id__in=filtrar_especialidade)

        especialidades = Especialidade.objects.all()
        return render (request,'home_paciente.html',{'especialidade':especialidades , 'medicos':medicos , 'is_medico':is_medico(request.user)})