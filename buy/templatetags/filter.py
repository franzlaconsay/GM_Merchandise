from django import template

register = template.Library()

@register.filter(name='splitfirst')
def splitfirst(value, key):
  x = value.split(key)
  return x[0]

@register.filter(name='splitsecond')
def splitfirst(value, key):
  x = value.split(key)
  return x[1]

@register.filter(name='addbefore')
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg2) + str(arg1)

@register.filter(name='mul')
def mul(arg1, arg2):
    """concatenate arg1 & arg2"""
    return arg1 * arg2
