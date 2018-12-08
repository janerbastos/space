#-*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils import timezone

from space.negocio.negocio import Negocio
from space.models import Reserva
from space.models import Espaco
from space.models import ItemReserva
from space.forms.reserva_forms import ReservaCreateForm
from space.utils.contexto import configure


class ReservaNegocio(Negocio):


    def __init__(self, oid):
        
        try:
            self.reserva = Reserva.objects.get(id=oid)
        except Reserva.DoesNotExist:
            self.reserva = None


    def add_espaco_reserva(self, request, reserva, inicio_at, termino_at):
        list_ = request.POST.getlist('espacos')
        for item in list_:
            espaco = Espaco.objects.get(id=item)
            item_reserva = ItemReserva(reserva=reserva, espaco=espaco, inicio_at=inicio_at, termino_at=termino_at)
            item_reserva.save()


    def create(self, request):

        #Pesquisar se existe espaços para reserva

        espacos = Espaco.objects.all()
        start = request.GET.get('start', '')
        end = request.GET.get('end', '')

        form = ReservaCreateForm(request.POST or None, instance=self.reserva, initial={'inicio_at': start})
        model = None
        is_save = False
        user = request.user

        if form.is_valid():
            model = form.save(commit=False)
            model.solicitante = user
            model.data_pedido_at = timezone.now()
            model.save()
            is_save = True
            self.add_espaco_reserva(request, model, form.cleaned_data['inicio_at'], form.cleaned_data['termino_at'])
            form = ReservaCreateForm()
        
        if request.is_ajax():
            html = render_to_string('space/componentes/aux_modal_form.html', {'form': form, 'opcao': 'reservar', 'objects': espacos})
            data = {
                'result': html,
                'action': 'create',
                'row': '',
            }
            if is_save:
                data['row'] = render_to_string('space/componentes/result_modal.html',
                context={'object': model, 'is_save': is_save, 'action': 'add-row'})
            
            return JsonResponse(data)

        if is_save:
            return redirect('space:reservas')

        data = configure(form, 'Reserva', 'Solicitação de espaço(s)...', self.reserva, espacos, 'reservas', 'create')
        return render(request, self.template, context=data)


    def update(self, request):

        #As atualizaçãos só serão permitidas se não existir nenhum item de reserva
        # for autorizada

        form = ReservaCreateForm(request.POST or None, instance=self.reserva)
        model = None
        is_save = False

        if form.is_valid():
            model = form.save(commit=False)
            model.save()
            return redirect('space:reservas')

        data = configure(form, 'Reserva', 'Atualização de reserva(s)...', self.reserva, None, 'reservas', 'update')
        return render(request, self.template, context=data)


    def list(self, request):

        #Implementar regra de negocico que desting gestor de solicitante

        user = request.user
        reservas = Reserva.objects.filter(solicitante=user).order_by('-data_pedido_at')
        data = configure(None, 'Reserva', 'Minhas reservas...', None, reservas, 'reservas', 'list')
        return render(request, self.template, context=data)


    def delete(self, request):

        #Só permitir a deleção pelo metodo post e somente se o status do espaço estiver False.
        
        super().delete(self.reserva)
        return redirect('space:reservas')
