from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from posts.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author_link', 'created_at')
    list_filter = ('created_at',)

    def author_link(self, obj):
        url = reverse('admin:users_user_change', args=[obj.author.id])
        return format_html('<a href="{}">{}</a>', url, obj.author.login)

    author_link.short_description = 'Автор'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'text', 'created_at', 'updated_at')
    list_filter = ('id', 'author', 'post')
    search_fields = ('id', 'author', 'post', 'text', 'created_at')
