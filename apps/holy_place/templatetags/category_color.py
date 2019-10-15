from django import template

register = template.Library()

@register.filter
def category_color(value):
    switch = { "ความรัก": "danger",
               "โชคลาภ": "warning",
               "คุ้มครอง": "success",
               "การงาน": "info",
               "อื่นๆ": "primary"
              } 
    return switch[value]