#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from space.negocio.negocio import Negocio
from space.forms.user_forms import UserCreateForm, UserUpdateForm
from space.models import Gestor

from space.utils.contexto import  configure


class GestorNegocio(Negocio):


    def __init__(self, oid=None):
        try:
            self.gestor = User.objects.get(id=oid)
        except User.DoesNotExist:
            self.gestor = None


    def create(self, request):
        form = UserCreateForm(request.POST or None, instance=self.gestor)
        is_save = False
        model = None
        if form.is_valid():

            model = form.save(commit=False)
            model.set_password(model.password)
            model.save()
            
            gestor = Gestor()
            gestor.usuario=model
            gestor.papel = 'gestor'
            gestor.save()
            
            is_save = True
            return redirect('space:gestores')
        data = configure(form, 'Usuarios', 'Criando uma gestor de espaços.', self.gestor, None, 'gestores', 'create')

        return render(request, 'space_layout/index.html', context=data)


    def update(self, request):
        form = UserUpdateForm(request.POST or None, instance=self.gestor)
        is_save = False
        model = None
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            is_save = True
            return redirect('space:gestores')
        data = configure(form, 'Usuários', 'Atualizando uma gestor espaços.', self.gestor, None, 'gestores', 'update')

        return render(request, 'space_layout/index.html', context=data)


    def list(self, request):
        gestores = Gestor.objects.all()
        data = configure(None, 'Usuários', 'Relação de conteúdos encontreado.', None, gestores, 'gestores', 'list')
        return render(request, 'space_layout/index.html', context=data)


    def delete(self, request):
        super().delete(self.gestor)
        return redirect('space:gestores')


