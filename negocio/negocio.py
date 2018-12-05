#-*- coding: utf-8 -*-
from abc import ABC as abstract


class Negocio(abstract):
    """
    Classe de negocio abstrata
    """

    def create(self, request):
        """
        Metodo de criação de objeto de negocio
        :param request: parametro de requisição do usuário
        :return: retorna um response de confirmação de criação do objeto de negocio para o usuário
        """
        raise NotImplementedError


    def update(self, request):
        """
        Metodo de atualização de componentes de negocio
        :param request: parametro da requisição do usuário
        :return: retorna um response de confirmação da atualização do objeto de negocio para o usuário
        """
        raise NotImplementedError


    def list(self, request):
        raise NotADirectoryError


    def delete(self, object):
        """
        Metodo estatico de negocio, excluir objeto do sistema.
        :param object: objeto de negocio que será removido do sistema.
        :return: retorna um responser em formato de dicionário  cotento a conformação da exclusão do objeto de negocio do sistema ao usuário.
        """
        object.delete()
        return {'status': 'Sucesso', 'code': 201}



