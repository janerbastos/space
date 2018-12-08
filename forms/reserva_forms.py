#-*- coding: utf-8 -*-
from django import forms
from space.models import Reserva

class ReservaCreateForm(forms.ModelForm):

    #def __ini__(self, inicio_at=None, *args, **kwargs):
    #    super(AgendaCreateForm, self).__init__(*args, **kwargs)
    #    self.inicio_at[''] = inicio_at

    inicio_at = forms.DateTimeField(label='Início do evento.',)
    termino_at = forms.DateTimeField(label='Termino do evento.',)
    class Meta:
        model = Reserva
        fields = ['descricao']
        labels = {
            'descricao': 'Objetivo da reserva',
        }
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3,})
        }