from django.contrib import admin
from django.apps import AppConfig
# Register your models here.

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title"]
    class Meta:
        model = Post
    name = 'posts'
admin.site.register(Post, PostModelAdmin)
