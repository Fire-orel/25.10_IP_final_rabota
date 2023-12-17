from django import template

register = template.Library()

@register.filter (name='cart_quantity')
def cart_quantity(count,id):
    print(count)
    value=count[str(id)]
    print(value)
    return value
