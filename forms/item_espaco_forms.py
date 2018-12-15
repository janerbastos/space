#-*- coding: utf-8 -*-

from django import forms
from space.models import ItemEspaco

class ItemEspacoForm(forms.ModelForm):

    class Meta:
        model = ItemEspaco
        fields = ['nome', 'descricao', 'quantidade', 'status', 'observacao']
        labels = {
            'nome': 'Nome',
            'descricao': 'Informações',
            'quantidade': 'Quantidade',
            'status': 'Status',
            'observacao': 'Observações'
        }
        help_texts = {
            'nome': 'Nome para o objeto',
            'descricao': 'Informações mais detahada do objeto',
            'observacao': 'Outras observações, como: cuidados etc',
            'status': 'Informar se esse item esta disponivel'
        }