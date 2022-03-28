from django.urls import path
from users import views

urlpatterns = [
    path('', views.index, name='index'),
    path('erro_404', views.erro_404, name='404'),
    path('erro_403', views.erro_403, name='403'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('accounts/profile/<int:user_id>', views.profile, name='profile'),
    path('cadastro', views.completa_cadastro, name='completa_cadastro'),
    path('atualiza_cadastro', views.atualiza_cadastro, name='atualiza_cadastro'),
]
