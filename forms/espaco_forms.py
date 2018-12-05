#-*- coding: utf-8 -*-

from django import forms
from space_manage.models import Espaco

class EspacoCreateForm(forms.ModelForm):

    class Meta:
        model = Espaco
        fields = ['nome', 'descricao', 'categoria']
        labels = {
            'nome': 'Nome do espaço',
            'descricao': 'Descrição do espaço',
            'categoria': 'Categoria'
        }

        help_texts = {
            'categoria': 'Selecione uma categoria para o espaço físico.'
        }
