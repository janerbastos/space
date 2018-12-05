#-*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from space_manage.models import CHOICE_PAPEL_USUARIO


class UserCreateForm(forms.ModelForm):

    password = forms.CharField(label='Senha', required=False, widget=forms.PasswordInput)
    conf_password = forms.CharField(label='Confirmar senha', required=False, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        labels = {
            'first_name': 'Primeiro nome',
            'last_name': 'Último nome',
            'email': 'Email',
            'username': 'Nome de usuário',

        }

        help_texts = {
            'username': 'Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.'
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Primeiro nome',
            'last_name': 'Último nome',
            'email': 'Email',
        }
