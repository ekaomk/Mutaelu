from django.db import models
from django.conf import settings

from .helper import file_helper

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Place(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    rate_count = models.IntegerField()
    thumbnail_image = models.ImageField(upload_to = file_helper.path_and_rename(f"{settings.MEDIA_PATH}/place_thumbnail_image/"))

