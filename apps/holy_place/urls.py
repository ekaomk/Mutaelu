from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('category/<category_name>/', views.category, name='category'),
]