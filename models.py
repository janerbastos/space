#-*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models



# Modulo de Negócio.

CHOICE_INFO_RESERVA = (
    ('aguradando', 'Aguardando analise'),
    ('nao-autorizado', 'Não autorizado'),
    ('cancelado', 'Cancelado'),
    ('autorizado', 'Autorizado'),
)

CHOICE_PAPEL_USUARIO = (
    ('gestor', 'Gestor'),
    ('solicitante', 'Solicitante')
)


class Gestor(models.Model):
    """
    Classe de modelo que abstrai usuário(s) responsável pela gestão de seus
    espaços fisicos
    """
    papel = models.CharField(max_length=30, default='solicitante', choices=CHOICE_PAPEL_USUARIO)
    usuario = models.OneToOneField(User, related_name='papel', on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.get_full_name()


class CategoriaEspaco(models.Model):
    """
    Classe que abstai categorizador de tipo de espaço fisico para reserva
    """

    nome = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Espaco(models.Model):
    """
    Class que abstrai os espaços físicos disponíveis para locação
    """

    nome = models.CharField(max_length=50)
    descricao = models.TextField(null=True, blank=True)
    gestor = models.ForeignKey(Gestor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaEspaco, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome
    

class ItemEspaco(models.Model):
    """
    Class que abstrai os itens que compoem os espaços fisicos
    """

    espaco = models.ForeignKey(Espaco, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    descricao = models.TextField(null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)
    quantidade = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)


class Reserva(models.Model):
    """
    Class que abstrai os pedidos de reserva de espaços
    """

    descricao = models.TextField()
    data_pedido_at = models.DateTimeField(auto_created=True)
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='minhas_reservas')

    def __str__(self):
        from django.utils.html import format_html
        return format_html('Código da resevar <b>%s</b>, resgitrada em %s' % (self.id, self.data_pedido_at))


class ItemReserva(models.Model):
    """
    Tabela de itens da reserva
    """

    reserva = models.ForeignKey(Reserva, on_delete=True, related_name='dados_reserva')
    espaco = models.ForeignKey(Espaco, on_delete=True)
    inicio_at = models.DateTimeField()
    termino_at = models.DateTimeField()
    info_reserva = models.CharField(max_length=15, default='aguradando', choices=CHOICE_INFO_RESERVA)
    observacao = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)

