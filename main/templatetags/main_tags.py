from django import template
import markdown
from django.utils.safestring import mark_safe


register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(text)

@register.filter(name='skill_column')
def skill_column(arr):

    delitel = len(arr)/4

    if delitel.is_integer():
        coun_in_column = delitel
    else:
        coun_in_column = len(arr)//4 + 1
    str = '<td><ul>'
    for j, i in enumerate(arr):
        if j > 0 and (j / coun_in_column).is_integer():
            str += f'<li>{i.name}<li></ul></td><td><ul>'
        else:
            str += f'<li>{i.name}<li>'
    str += '</ul></td>'
    return str