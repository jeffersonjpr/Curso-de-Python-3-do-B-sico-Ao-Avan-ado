from django.shortcuts import render
from .models import Contato
from django.http import Http404


def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {'contatos': contatos})


def contact(request, contato_id):
    try:
        contato = Contato.objects.get(id=contato_id)
        return render(request, 'contatos/contact.html', {
            'contato': contato
        })
    except Contato.DoesNotExist as e:
        raise Http404('Contato não encontrado')
