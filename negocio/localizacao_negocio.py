#-*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.template.loader import render_to_string

from space.models import Localizacao
from space.negocio.negocio import Negocio
from space.forms.localizacao_forms import LocalizacaoForm
from space.utils.contexto import configure


class LocalizacaoNegocio(Negocio):

    def __init__(self, oid):
        self.oid = oid

    def get_object(self):
        try:
            return Localizacao.objects.get(id=self.oid)
        except Localizacao.DoesNotExist:
            return None
    

    def create(self, request):
        form = LocalizacaoForm(request.POST or None, instance=None)
        model = None
        is_save = False
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            is_save = True
        
        if request.is_ajax():
            html = render_to_string('?template',{'form': form, 'object': None,})
        
        if is_save:
            return redirect('space:manage-localizacao')
        data = configure(form, 'Localização', 'Criando uma nova localização.', None, None, 'localizacao', 'create')
        return render(request, self.template, context=data)
    

    def update(self, request):
        localizacao = self.get_object()
        form = LocalizacaoForm(request.POST or None, instance=localizacao)
        model = None
        is_save = False
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            is_save = True
        
        if request.is_ajax():
            html = render_to_string('?template',{'form': form, 'object': localizacao,})
        
        if is_save:
            return redirect('space:manage-localizacao')
        data = configure(form, 'Localização', 'Criando uma nova localização.', localizacao, None, 'localizacao', 'create')
        return render(request, self.template, context=data)


    def list(self, request):
        localizacoes = Localizacao.objects.all()
        data = configure(None, 'Localização', 'Lista de objetos.', None, localizacoes, 'localizacao', 'list')
        return render(request, self.template, context=data)
    

    def delete(self, request):
        localizacao = self.get_object()
        super().delete(localizacao)
        return redirect('space:manage-localizacao')