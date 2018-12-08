#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from space.negocio.negocio import Negocio
from space.forms.espaco_forms import EspacoCreateForm
from space.models import Espaco

from ..utils.contexto import  configure

class EspacoNegocio(Negocio):


    def __init__(self, oid=None):
        try:
            self.espaco = Espaco.objects.get(id=oid)
        except Espaco.DoesNotExist:
            self.espaco = None


    def create(self, request):
        form = EspacoCreateForm(request.POST or None, instance=self.espaco)
        is_save = False
        model = None
        user = request.user
        if form.is_valid():
            model = form.save(commit=False)
            model.gestor = user.papel
            model.save()
            is_save = True
            return redirect('space:espacos')
        data = configure(form, 'Espaço físico', 'Criando uma espaço físico.', self.espaco, None, 'espacos', 'create')

        return render(request, self.template, context=data)


    def update(self, request):
        form = EspacoCreateForm(request.POST or None, instance=self.espaco)
        is_save = False
        model = None
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            is_save = True
            return redirect('space:espacos')
        data = configure(form, 'Espaço físico', 'Atualizando uma espaço físico.', self.espaco, None, 'espacos', 'update')

        return render(request, self.template, context=data)


    def list(self, request):
        espacos = Espaco.objects.all()
        data = configure(None, 'Espaços Físicos', 'Relação de conteúdos encontreado.', None, espacos, 'espacos', 'list')
        return render(request, self.template, context=data)


    def delete(self, request):
        super().delete(self.espaco)
        return redirect('space:espacos')


