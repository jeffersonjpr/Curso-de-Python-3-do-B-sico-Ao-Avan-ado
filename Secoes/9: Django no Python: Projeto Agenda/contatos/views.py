from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
from django.http import Http404

def index(request):
    contatos = Contato.objects.order_by('-nome') # Ordena os contatos pelo nome em ordem decrescente
    paginator = Paginator(contatos, 5) # 5 contatos por página

    page = request.GET.get('page')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {'contatos': contatos})


def contact(request, contato_id):
    #contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id) # Retorna 404 se não encontrar o contato

    if not contato.mostrar:
        raise Http404('Contato não encontrado') # Lança uma exceção 404 se o usuário não estive ativo

    return render(request, 'contatos/contact.html', {
        'contato': contato
    })
