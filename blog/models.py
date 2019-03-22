import os
from django.db import models
import random
from django.db.models.signals import  pre_save, post_save

from .utils import unique_slug_generator


def get_filename_ext(filepath):
    """Split file path into name & extension"""
    base_name   = os.path.basename(filepath)
    name, ext   = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    """Create New File Name"""
    new_filename    = random.randint(1, 3910209312)
    name, ext       = get_filename_ext(filename)
    final_filename  = f"{new_filename}{ext}"
    return f'blog/{new_filename}/{final_filename}'


# Create your models here.
class Blog(models.Model):
    title       = models.CharField(max_length=50)
    slug        = models.SlugField(blank=True, unique=True)
    content     = models.TextField()
    author      = models.CharField(max_length=50)
    date_added  = models.DateTimeField(auto_now_add=True)
    image       = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    status      = models.BooleanField(default=True)

    def get_absolute_url(self):
        return f'/blog/{self.slug}'

    def __str__(self):
        return self.title

def blog_pre_save_reciever(sender, instance, *args, **kwargs):
    """Create slug value for every empty slug field"""
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(blog_pre_save_reciever, sender=Blog)
