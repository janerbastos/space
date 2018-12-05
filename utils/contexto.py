#-*- coding: utf-8 -*-

def configure(form, titulo, descricao, object, objects, modulo, action):
    """
    Define os parametro que serão encaminhados para o contexto de resposta.
    :param form: objeto do tipo form
    :param titulo: titulo do object
    :param descricao: descrição sobre o object
    :param object: objeto a ser gerenciado
    :param objects: lista de objeto
    :param modulo: nome do modulo em processamento
    :param action: o tipo de ação que será ou foi executada
    :return: dicionário de contexto dos dados acima
    """
    data = {
        'form': form,
        'titulo': titulo,
        'descricao': descricao,
        'object': object,
        'objects': objects,
        'modulo': modulo,
        'action': action
    }
    return data