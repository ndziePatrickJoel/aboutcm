from django import template

register = template.Library()


def qanda_split(str_to_split, separator):
    
    return str(str_to_split).split(separator)

register.filter('qanda_split', qanda_split)