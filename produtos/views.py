from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from .forms import AdicionarProduto
from .models import Produto, Fornecedor

from users.models import User


@login_required
def add_produto(request):
    if not request.user.has_perm('global_permissions.incluir_produto'):
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
            return render(request, 'produtos/add_produto.html', context=context)

        else:
            form = AdicionarProduto()
            context = {
                'form': form
            }
            return render(request, 'produtos/add_produto.html', context=context)

