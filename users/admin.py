from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .forms import UserCreationForm, UserChangeForm
from .models import User

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    list_display_links = ('username',)
    list_display = ('id', 'username', 'email', 'telefone', )
    fieldsets = auth_admin.UserAdmin.fieldsets + (('Informações Adicionais',
                  {'fields': ('telefone', 'cep', 'endereco', 'foto_user')
                }),)
