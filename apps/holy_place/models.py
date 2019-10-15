from django.db import models
from django.conf import settings

import os
from uuid import uuid4

# rename file with uuid
def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper

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
    thumbnail_image = models.ImageField(upload_to = path_and_rename(f"{settings.MEDIA_PATH}/place_thumbnail_image/"))

