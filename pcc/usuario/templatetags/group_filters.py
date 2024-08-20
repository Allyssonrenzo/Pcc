from django import template
register = template.Library()

@register.filter(name='is_empresa')
def is_empresa(user):
    return user.groups.filter(name="Empresa").exists()

@register.filter(name='is_usuario')
def is_usuario(user):
    return user.groups.filter(name="Usuario").exists()
