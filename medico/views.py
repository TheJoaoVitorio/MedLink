from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from .models import Especialidade
from .models import DadosMedico
from .models import is_medico

# Create your views here.
@login_required
def cadastro_medico(request):
    
    DMedicos = DadosMedico.objects.filter(user = request.user)

    if DMedicos.exists():
        messages.add_message(request,constants.WARNING,"Médico já registrado! ")
        return redirect('/medicos/abrir-horario') #erro,pois precisa fazer o path,template e a view

    if request.method == 'GET':
        especialidades = Especialidade.objects.all() 
        return render(request , 'cadastro_medico.html', {'especialidade': especialidades})
    elif request.method == 'POST':
        crm = request.POST.get('crm')
        cim = request.FILES.get('cim')
        nome_completo = request.POST.get('nome')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        numero = request.POST.get('numero')
        rg = request.FILES.get('rg')
        foto_perfil = request.FILES.get('foto-perfil')
        especialidade = request.POST.get('especialidade')
        descricao = request.POST.get('descricao')
        valor_consulta = request.POST.get('valor_consulta')

        dados_medico = DadosMedico(
            crm = crm,
            nome = nome_completo,
            cep = cep ,
            rua = rua ,
            bairro = bairro,
            numero = numero,
            rg = rg,
            cedula_identidade_medica = cim,
            foto = foto_perfil,
            especialidade_id = especialidade,
            descricao = descricao,
            valor_consulta = valor_consulta,

            user = request.user
        )
        dados_medico.save()
        messages.add_message(request,constants.SUCCESS ,"Cadastro Médico realizado com sucesso!")
        return redirect('/medicos/abrir-horario') #ERRO 


def HomeMedico(request):
    return render (request,'home-medico.html',)