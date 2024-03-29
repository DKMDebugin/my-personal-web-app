from django.contrib import admin

from .models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'status', 'date_created', 'date_updated']
