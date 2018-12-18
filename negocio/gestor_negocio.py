#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Q

from space.negocio.negocio import Negocio
from space.forms.user_forms import UserCreateForm, UserUpdateForm
from space.models import Gestor

from space.utils.contexto import  configure, excluir_ultimo_item


class GestorNegocio(Negocio):

    def __init__(self, oid=None):
        self.paginas = self.pages % 'gestores'
        try:
            self.user = Gestor.objects.get(id=oid)
        except Gestor.DoesNotExist:
            self.user = None


    def create(self, request):
        form = UserCreateForm(request.POST or None, instance=self.user)
        is_save = False
        model = None
        if form.is_valid():

            model = form.save(commit=False)
            model.set_password(model.password)
            model.save()
            
            is_save = True
            return redirect('space:gestores')
        data = configure(form, 'Usuarios', 'Criando uma gestor de espaços.', self.user, None, 'gestores', 'create')

        return render(request, self.template, context=data)


    def update(self, request):
        form = UserUpdateForm(request.POST or None, instance=self.user.usuario)
        is_save = False
        model = None
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            is_save = True
            return redirect('space:gestores')
        data = configure(form, 'Usuários', 'Atualizando uma gestor espaços.', self.user, None, 'gestores', 'update')

        return render(request, self.template, context=data)


    def list(self, request):
        gestores = Gestor.objects.all()
        data = configure(None, 'Gestores', 'Relação de conteúdos encontreado.', None, gestores, 'gestores', 'list')
        if request.is_ajax():   
            html_string = render_to_string(self.paginas, data)
            return JsonResponse({'result': html_string}, status=200)
        return render(request, self.template, context=data)


    def delete(self, request):
        super().delete(self.user)
        return redirect('space:gestores')


    def delete_item(self, request):
        pass


    def add_item(self, request):
        search = request.GET.get('search', None)
        users = None
        
        if search:
            users = User.objects.filter(Q(username__startswith=search) | Q(first_name__startswith=search) | Q(last_name__startswith=search))
        data = {
            'result': 'Usuário já vinculado ou não econtrado.',
        }
        if request.method == 'POST':
            url = excluir_ultimo_item(request.path)
            print(url)
            try:
                oid  = request.POST.get('oi', None)
                user = User.objects.get(id=oid)
                gestor = Gestor(papel='Gestor', usuario=user)
                gestor.save()
                return JsonResponse({'action': 'fechar', 'url': url}, status=201)
            except:
                pass
            
        if request.is_ajax():
            html_string = render_to_string('space/componentes/aux_modal_form.html', {'objects': users, 'opcao': 'lista-usuarios'})
            data['result'] = html_string
            data['action'] = 'pesquisar'
            return JsonResponse(data, status=200)

        data = configure(None, 'Usuários', 'Relação de conteúdos encontreado.', None, users, 'usuarios', 'list')
        return render(request, self.template, context=data)