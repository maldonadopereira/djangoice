from django.shortcuts import render, redirect

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