from django.contrib import admin
from .models import Category, Place

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'color', 'show_in_home']
    list_display = ['name', 'color', 'show_in_home']

class PlaceAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'rating', 'rate_count', 'thumbnail_image']
    list_display = ['name', 'category', 'rating', 'rate_count']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Place, PlaceAdmin)