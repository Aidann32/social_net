from django.contrib import admin
from .models import Post, Comment, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('title', 'author', 'content', 'image', 'liked', 'get_likes_number', 'get_comment_number', )


admin.site.register(Comment)
admin.site.register(Like)
