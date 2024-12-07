from django import template

register = template.Library()

@register.filter(name='boolean_to_text')
def boolean_to_text(value):
    return "Sí" if value else "No"
