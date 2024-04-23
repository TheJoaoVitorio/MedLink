from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def landing_page(request):
    return render (request,'landing_page.html')


def cadastro(request):

    if request.method == 'GET':
        return render(request,'cadastro.html')
    elif request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('senha')
        confirmPassword = request.POST.get('confirmar-senha')

        if password != confirmPassword:
            #o messages tem 3parametros , o request , tipo de msg e o texto da mensagem
            messages.add_message(request,constants.ERROR ,"Senha e o confirmar senha devem ser iguais")
            return redirect('/usuarios/cadastro')
        if len(password) < 6:
            messages.add_message(request,constants.ERROR ,"A Senha deve ter mais de 6 digitos")
            return redirect('/usuarios/cadastro')

                            #o primeiro parametro e do BD e o outro é do valor da request username
                        #filtro para pegar os valores(do BD) que sejam iguais a da request
        users = User.objects.filter(username = username)
            #vai retornar um valor boolean
        if users.exists():
            messages.add_message(request,constants.ERROR ,"Já exite um usuário com esse username")
            return redirect ('/usuarios/cadastro')

        user = User.objects.create_user(
            username = username,
            email = email,
            password = password
        )
        return redirect ('/usuarios/login')

def login(request):

    if request.method == "GET":
        return render (request , 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('senha')

        user = auth.authenticate(request, username=username , password=password)
        #se for True 
        if user:
            auth.login(request,user)
            return redirect ('pacientes/home')

        messages.add_message(request,constants.ERROR ,"Usuário ou senha inválidos")
        return redirect('/usuarios/login')

def logout(request):
    auth.logout(request)
    return redirect('/usuarios/login')