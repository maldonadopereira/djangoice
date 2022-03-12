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
    first_name = forms.CharField(max_length=30, label='Sobrenome')
    last_name = forms.CharField(max_length=30, label='Nome')
    phone = forms.CharField(max_length=14, label='Telefone')
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
