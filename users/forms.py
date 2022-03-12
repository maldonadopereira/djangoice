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



