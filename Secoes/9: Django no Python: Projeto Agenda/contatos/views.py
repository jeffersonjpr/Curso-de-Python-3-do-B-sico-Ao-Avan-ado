from django.shortcuts import render
from .models import Contato

def index(request):
    return render(request, 'contatos/index.html', {'nome': 'Jefferson Michael'})