from django.contrib import admin
from django.urls import path

from users import views

urlpatterns = [
    path('', views.index, name='index'),
    path('erro_404', views.erro_404, name='404'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('accounts/profile/', views.profile, name='profile'),
    path('cadastro', views.completa_cadastro, name='completa_cadastro')
]
