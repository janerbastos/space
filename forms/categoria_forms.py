#-*- coding: utf-8 -*-

from django import forms

from space.models import CategoriaEspaco


class CategoriaEspacoForm(forms.ModelForm):

    class Meta:

        model = CategoriaEspaco
        
        fields = ['nome', 'status',]
        
        labels = {
            'nome': 'Nome da categoria',
            'status': 'Habilitado'
        }

        help_texts = {
            'nome': 'Descreva um nome para um grupo de categória. ex.: "Salas", "Auditórios", "Laboratório".',
        }

