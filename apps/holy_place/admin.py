from django.contrib import admin
from .models import Category, Place

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'color']
    list_display = ['name', 'color']

class PlaceAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'rating', 'rate_count', 'thumbnail_image']
    list_display = ['name', 'category', 'rating', 'rate_count']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Place, PlaceAdmin)