#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse

from space.controller.requisicao_resposta import Processador
from space.utils.contexto import configure

import os
from os.path import join
import json

# Interface de acesso web


def index(request):
    data = configure(None, 'SPACE', 'Gestor de espaços', None, None, None, 'index')
    return render(request, 'space_layout/index.html', context=data)


def categorias(request, oid=None, action='list'):
    return Processador().run(request, tipo='categoria', oid=oid, action=action)


def espacos(request, oid=None, action='list'):
    return Processador().run(request, tipo='espaco', oid=oid, action=action)


def gestores(request, oid=None, action='list'):
    return Processador().run(request, tipo='gestor', oid=oid, action=action)


def reservas(request, oid=None, action='list'):
    return Processador().run(request, tipo='reserva', oid=oid, action=action)


def events(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path_json = os.path.join(BASE_DIR, 'space/data/evento.json')
    data = None
    with open(path_json) as json_data:
        data = json.load(json_data)
        json_data.close()
    
    return JsonResponse(data, safe=False)
