from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_cubtotal(price, quantity):
    return price * quantity
