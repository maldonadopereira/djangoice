from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from .forms import AdicionarProduto
from .models import Produto



@login_required
def adicionar_produto(request):
    if not request.user.has_perm('global_permissions.manipular_produto'):
        raise PermissionDenied
    else:
        if request.method == 'POST':
            form = AdicionarProduto(request.POST)
            if form.is_valid():
                produto = form.save()
                form = AdicionarProduto()
            context = {
                'form': form
            }
            return render(request, 'produtos/adicionar_produto.html', context=context)

        else:
            form = AdicionarProduto()
            context = {
                'form': form
            }
            return render(request, 'produtos/adicionar_produto.html', context=context)

def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    produto_a_editar = {
        'produto': produto
    }
    return render(request, 'produtos/editar_produto.html', produto_a_editar)

def listar_produto(request):
    if request.user.is_authenticated:
        produtos = Produto.objects.order_by('id')
        dados = {
            'produtos': produtos
        }
        return render(request, 'produtos/listar_produto.html', dados)

def detalhar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    produto_a_exibir = {
        'produto': produto
    }
    return render(request, 'produtos/detalhar_produto.html', produto_a_exibir)
