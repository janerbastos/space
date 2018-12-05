#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from space_manage.negocio.negocio import Negocio
from space_manage.forms.categoria_forms import CategoriaEspacoForm
from space_manage.models import CategoriaEspaco

from space_manage.utils.contexto import  configure


class CategoriaNegocio(Negocio):


    def __init__(self, oid=None):
        try:
            self.categoria = CategoriaEspaco.objects.get(id=oid)
        except CategoriaEspaco.DoesNotExist:
            self.categoria = None


    def create(self, request):
        form = CategoriaEspacoForm(request.POST or None, instance=self.categoria)
        is_save = False
        model = None
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            is_save = True
            return redirect('space:categorias')
        data = configure(form, 'Categoria', 'Criando uma categoria.', self.categoria, None, 'categorias', 'create')

        return render(request, 'space_layout/index.html', context=data)


    def update(self, request):
        form = CategoriaEspacoForm(request.POST or None, instance=self.categoria)
        is_save = False
        model = None
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            is_save = True
            return redirect('space:categorias')
        data = configure(form, 'Categoria', 'Atualizando uma categoria.', self.categoria, None, 'categorias', 'update')

        return render(request, 'space_layout/index.html', context=data)


    def list(self, request):
        categorias = CategoriaEspaco.objects.all()
        data = configure(None, 'Categorias', 'Relação de conteúdos encontreado.', None, categorias, 'categorias', 'list')
        return render(request, 'space_layout/index.html', context=data)


    def delete(self, request):
        super().delete(self.categoria)
        return redirect('space:categorias')


