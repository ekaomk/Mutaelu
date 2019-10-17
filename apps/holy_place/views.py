from django.shortcuts import render
from django.http import HttpResponse
from django import template
from .models import Category, Place

register = template.Library()

@register.filter
def intcomma(value):
    return value + 1

def index(request):
    context = {}
    #context["categorys"] = Category.objects.all()
    context["categorys"] = Category.objects.filter(show_in_home=True).all()
    context["places"] = Place.objects.all()
    return render(request, 'index.html', context)

def category(request, category_name):
    context = {}
    category = Category.objects.filter(name=category_name).first()
    context["categorys"] = Category.objects.filter(show_in_home=True).all()
    context["places"] = Place.objects.filter(category_id=category.id).select_related()
    context["title"] = category.name
    return render(request, 'index.html', context)