from django.contrib.auth import forms as auth_forms
from .models import User
from allauth.account.forms import SignupForm
from django import forms


class UserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = User


class CustomSignupForm(SignupForm):
    '''username = forms.CharField(max_length=30, label='Nome de Usuário', widget=forms.TextInput(attrs={"placeholder": 'Nome de Usuário', "autocomplete": "username"}))
    email = forms.EmailField(max_length=30, label='E-mail', widget=forms.TextInput(attrs={"placeholder": 'E-mail', "autocomplete": "email"}))
    first_name = forms.CharField(max_length=30, label='Nome', widget=forms.TextInput(attrs={"placeholder": 'Nome', "autocomplete": "first_name"}))
    last_name = forms.CharField(max_length=30, label='Sobrenome', widget=forms.TextInput(attrs={"placeholder": 'Sobrenome', "autocomplete": "last_name"}))
    phone = forms.CharField(max_length=14, label='Telefone', widget=forms.TextInput(attrs={"placeholder": 'Telefone', "autocomplete": "phone"}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user'''
