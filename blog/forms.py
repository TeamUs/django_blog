# forms.py
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': _('Имя пользователя'),
            'password1': _('Пароль'),
            'password2': _('Подтверждение пароля'),
        }

class AuthUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']
