from django.shortcuts import render, redirect, get_object_or_404

from users.models import User


def index(request):
    return render(request, 'index.html')

def erro_404(request):
    return render(request, '404.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')

    else:
        return redirect('index')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')

    else:
        return redirect('account_login'),

def completa_cadastro(request):
    return render(request, 'completa_cadastro.html')


def atualiza_cadastro(request):
    if request.method =='POST':
        user_id = request.POST['user_id']
        u = User.objects.get(pk=user_id)
        u.first_name = request.POST['first_name']
        u.last_name = request.POST['last_name']
        u.email = request.POST['email']
        u.telefone = request.POST['telefone']
        u.cep = request.POST['cep']
        u.endereco = request.POST['endereco']

        u.save()
        return redirect('profile')