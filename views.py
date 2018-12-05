#-*- coding: utf-8 -*-

from django.shortcuts import render

from .controller.requisicao_resposta import Processador
from .utils.contexto import configure

# Interface de acesso web


def index(request):
    data = configure(None, 'SPACE', 'Gestor de espaços', None, None, None, 'view')
    return render(request, 'space_layout/index.html', context=data)


def categorias(request, oid=None, action='list'):
    return Processador().run(request, tipo='categoria', oid=oid, action=action)


def espacos(request, oid=None, action='list'):
    return Processador().run(request, tipo='espaco', oid=oid, action=action)


def gestores(request, oid=None, action='list'):
    return Processador().run(request, tipo='gestor', oid=oid, action=action)


def reservas(request, oid=None, action='list'):
    return Processador().run(request, tipo='reserva', oid=oid, action=action)

