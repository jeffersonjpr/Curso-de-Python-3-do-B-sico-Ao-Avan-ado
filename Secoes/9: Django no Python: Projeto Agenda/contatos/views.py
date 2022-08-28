from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat


def index(request):
    contatos = Contato.objects.order_by('id').filter(
        mostrar=True)  # Filtra os contatos que estão ativos
    paginator = Paginator(contatos, 5)  # 5 contatos por página

    page = request.GET.get('page')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {'contatos': contatos})


def contact(request, contato_id):
    #contato = Contato.objects.get(id=contato_id)
    # Retorna 404 se não encontrar o contato
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        # Lança uma exceção 404 se o usuário não estive ativo
        raise Http404('Contato não encontrado')

    return render(request, 'contatos/contact.html', {
        'contato': contato
    })


def busca(request):
    termo = request.GET.get('termo')
    print("Termo:", termo)

    if termo is None or not termo:
        raise Http404()

    ## Seleção
    # Concatena nome e sobrenome
    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo),
        mostrar=True
    )
    print(contatos.query)  # Imprime a consulta SQL feita para a busca acima
    # End seleção

    paginator = Paginator(contatos, 5)  # 5 contatos por página

    page = request.GET.get('page')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {'contatos': contatos})
