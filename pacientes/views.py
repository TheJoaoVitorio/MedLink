from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def HomePaciente(request):
    return render (request,'home_paciente.html')