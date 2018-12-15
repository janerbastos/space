#-*- coding: utf-8 -*-
from django import forms

from space.models import Localizacao

class LocalizacaoForm(forms.ModelForm):

    class Meta:
        model = Localizacao
        fields = ['nome', 'endereco', 'latitude', 'longitude',]
        labels = {
            'nome': 'Identificador',
            'endereco': 'Endereço',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
        }