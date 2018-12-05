#-*- coding: utf-8 -*-

from space_manage.processador import Processador


class RequisicaoResposta():

    @staticmethod
    def processador(self, **kwargs):
        proc = Processador()
        return proc.run(**kwargs)

