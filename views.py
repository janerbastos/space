#-*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import JsonResponse

from space.controller.requisicao_resposta import Processador
from space.utils.contexto import configure, redirect_if_param

import os
from os.path import join
import json

# Interface de acesso web


def index(request):
    data = configure(None, 'SPACE', 'Gestor de espaços', None, None, None, 'index')
    return render(request, 'space/index.html', context=data)


def categorias(request, oid=None, action='list'):
    return Processador().run(request, tipo='categoria', oid=oid, action=action)


def localizacoes(request, oid=None):
    localizador = request.GET.get('localizador', None)
    action = request.GET.get('action', 'list')
    if localizador:
        response = redirect('space:espacos')
        return redirect_if_param(response, 'action=create&localizador=%s' % oid )
    else:   
        return Processador().run(request, tipo='localizacao', oid=oid, action=action)


def espacos(request, oid=None):
    localizador = request.GET.get('localizador', None)
    action = request.GET.get('action', 'list')
    if not localizador and (action in ['create', 'update']):
        return redirect('space:manage-localizador')
    return Processador().run(request, tipo='espaco', oid=oid, oid_l=localizador, action=action)


def gestores(request, oid=None, action='list'):
    return Processador().run(request, tipo='gestor', oid=oid, action=action)


def reservas(request, oid=None, action='list'):
    return Processador().run(request, tipo='reserva', oid=oid, action=action)


def events(request):
    from space.models import ItemReserva

    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #path_json = os.path.join(BASE_DIR, 'space/data/evento.json')
    
    start = request.GET.get('start', None).split('-')
    end = request.GET.get('end', None).split('-')

    objects = ItemReserva.objects.all()
    
    json_data = '['
    comprimento = objects.count()
    i = 1
    #with open(path_json) as json_data:
    #    data = json.load(json_data)
    #    json_data.close()

    for item in objects:
        json_data += '{"id": "%s", ' % item.id
        json_data += '"title": "%s", ' % item.espaco.nome
        json_data += '"description": "%s<br>Solicitante: <strong>%s</strong>", ' % (item.reserva.descricao, item.reserva.solicitante.get_full_name())
        json_data += '"start": "%s", ' % item.inicio_at.strftime("%Y-%m-%dT%H:%M:%S")
        json_data += '"end": "%s"}' % item.termino_at.strftime("%Y-%m-%dT%H:%M:%S")
        if i < comprimento:
            json_data += ', '
        i += 1
    json_data += ']'
    data = json.loads(json_data.encode('utf-8'))
    print(data)
    return JsonResponse(data, safe=False)
