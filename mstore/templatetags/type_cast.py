
from django import template


register = template.Library()


@register.filter("value_to_dict")
def value_to_dict(value, v2):
    print(v2)
    return dict(value)



