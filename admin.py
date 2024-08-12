# blog_app/admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    list_filter = ('published_date',)
    search_fields = ('title', 'content')
