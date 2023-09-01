from django import template



register = template.Library()

@register.simple_tag

def get_specific_link(table,name,fieldname): 
    querySetSpecific = table.objects.where(f'{fieldname} = {name}')
    return querySetSpecific
    