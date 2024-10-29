from django import template

register=template.Library()

@register.simple_tag(name='getstatus')

def getstatus(status):
    status=status-1
    array=['Order Confirmed','Order Processed','Order Delivered','Order Rejected']
    return array[status]

