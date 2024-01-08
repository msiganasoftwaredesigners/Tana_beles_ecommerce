from django import template

register = template.Library()

@register.filter
def discounted_price(price):
    return price - (price * 0.15)