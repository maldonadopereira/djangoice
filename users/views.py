from django.shortcuts import render, redirect, get_object_or_404

from users.models import User


def index(request):
    return render(request, 'index.html')

def erro_404(request):
    return render(request, '404.html')

def erro_403(request):
    return render(request, '403.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')

    else:
        return redirect('index')

def profile(request, user_id):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=user_id)

        context = {
            'user': user
        }
        return render(request, 'profile.html', context)

    else:
        return redirect('index'),



def completa_cadastro(request):
    if request.user.is_authenticated:
        return render(request, 'completa_cadastro.html')
    else:
        return redirect('index')

def atualiza_cadastro(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            user_id = request.POST['user_id']
            u = User.objects.get(pk=user_id)
            u.first_name = request.POST['first_name']
            u.last_name = request.POST['last_name']
            u.email = request.POST['email']
            u.telefone = request.POST['telefone']
            u.cep = request.POST['cep']
            u.endereco = request.POST['endereco']
            if 'foto_user' in request.POST:
                u.foto_user = request.POST['foto_user']
            u.save()
            return redirect('profile')
        else:
            return render(request, 'completa_cadastro.html')
    else:
        return redirect('index')