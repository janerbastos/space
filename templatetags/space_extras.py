# -*- coding: utf-8 -*-

from django import template
from django.utils.html import format_html

register = template.Library()


@register.filter(name='modulopage')
def page_modulo(modulo_name):
    source_file = "space/pages/%s.html" % modulo_name
    return source_file
