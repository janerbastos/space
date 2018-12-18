#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.db.models import Q

from space.negocio.negocio import Negocio
from space.forms.espaco_forms import EspacoCreateForm
from space.models import Espaco
from space.negocio.localizacao_negocio import LocalizacaoNegocio

from ..utils.contexto import  configure

class EspacoNegocio(Negocio):

    def __init__(self, oid_l, oid=None):
        self.oid = oid
        self.oid_l = oid_l


    def get_object(self):
        try:
            return Espaco.objects.get(id=self.oid)
        except Espaco.DoesNotExist:
            return None


    def create(self, request):
        localizador = LocalizacaoNegocio(self.oid_l).get_object()
        espaco = self.get_object()
        form = EspacoCreateForm(request.POST or None, instance=espaco)
        is_save = False
        model = None
        user = request.user
        if form.is_valid():
            model = form.save(commit=False)
            model.gestor = user.papel
            model.localizacao = localizador
            model.save()
            is_save = True
            return redirect('space:espacos')
        data = configure(form, 'Espaço físico', 'Criando uma espaço físico.', espaco, None, 'espacos', 'create')

        return render(request, self.template, context=data)


    def update(self, request):
        espaco = self.get_object()
        print(espaco)
        form = EspacoCreateForm(request.POST or None, instance=espaco)
        is_save = False
        model = None
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            is_save = True
            return redirect('space:espacos')
        data = configure(form, 'Espaço físico', 'Atualizando uma espaço físico.', espaco, None, 'espacos', 'update')

        return render(request, self.template, context=data)


    def list(self, request):
        espacos = Espaco.objects.all()
        search = request.POST.get('search', None)
        if request.method == 'POST' and search:
            espacos = espacos.filter(Q(nome__startswith=search) | Q(localizacao__nome__startswith=search))
        data = configure(None, 'Espaços Físicos', 'Relação de conteúdos encontreado.', None, espacos, 'espacos', 'list')
        return render(request, self.template, context=data)


    def delete(self, request):
        espaco = self.get_object()
        super().delete(espaco)
        return redirect('space:espacos')


