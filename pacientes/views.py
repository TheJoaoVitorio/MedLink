from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse
from django.contrib.messages import constants
from django.contrib import messages

from medico.models import Especialidade , DadosMedico , is_medico , DatasAbertas
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

@login_required
def EscolherHorario(request,id_dados_medicos):

    if request.method == 'GET':
        
        medico = DadosMedico.objects.get(id=id_dados_medicos)
        datas_abertas = DatasAbertas.objects.filter(user=medico.user).filter(data__gte=datetime.now()).filter(agendado=False)

        if not datas_abertas:
            messages.add_message(request,constants.WARNING,"Esse médico não pussui horário aberto no momento.")
            return redirect('/pacientes/home')

        return render (request,'escolher_horario.html',{'medico':medico , 'datas_abertas':datas_abertas , 'is_medico':is_medico(request.user)})
