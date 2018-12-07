#-*- coding: utf-8 -*-

from django.http import Http404

from space.negocio.categoria_negocio import CategoriaNegocio
from space.negocio.espaco_negocio import EspacoNegocio
from space.negocio.gestor_negocio import GestorNegocio
from space.negocio.reserva_negocio import ReservaNegocio


class Processador():

    @staticmethod
    def __configure(**kwargs):
        methods = {
            'categoria': CategoriaNegocio(kwargs.get('oid')),
            'espaco': EspacoNegocio(kwargs.get('oid')),
            'item-espaco': None,
            'reserva': ReservaNegocio(kwargs.get('oid')),
            'item-reserva': None,
            'gestor': GestorNegocio(kwargs.get('oid')),
            'solicitante': None
        }
        return methods


    def run(self, request, **kwargs):
        method = Processador.__configure(**kwargs)

        tipo = kwargs.get('tipo', None)
        action = kwargs.get('action', None)

        if action:
            if action == 'create':
               return method[tipo].create(request)
            if action == 'update':
               return method[tipo].update(request)
            if action == 'delete':
                return method[tipo].delete(request)
            if action == 'list':
                return method[tipo].list(request)

        raise Http404('Solictação não pode ser atendida')
