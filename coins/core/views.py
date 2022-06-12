
from django.shortcuts import render


def login_user(request):
    return render(request, 'login.html')

def inicio(request):
    return render(request, 'inicio.html')

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def servicos(request):
    return render(request, 'servicos.html')

def contato(request):
    return render(request, 'contato.html')
