from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'cover', 'content', 'published_date']

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'post']
