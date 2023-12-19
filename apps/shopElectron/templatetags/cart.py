from django import template

register = template.Library()

@register.filter (name='cart_quantity')
def cart_quantity(count,id):
    # print(count)
    value=count[str(id)]
    # print(value)
    return value


@register.simple_tag
def cart_summa(prise,count):
    return prise*count

@register.simple_tag
def cart_summa_finish(product,count):
    suma=0

    for p in product:

        suma+=p.price*count[str(p.id)]
    # print(suma)


    return suma

@register.simple_tag
def countss(count):
    return len(count)
