from django import template

from store.models import Cateogary

register = template.Library()

@register.inclusion_tag('menu.html')
def menu():
    cateogaries = Cateogary.objects.all()
    return {'cateogaries':cateogaries}