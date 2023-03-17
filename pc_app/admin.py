from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import User, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('header', 'text', 'authors_link', 'display_comments', 'created_at')
    list_filter = ('created_at',)
    actions = ['delete_all_comments']

    @admin.action(description='Удалить комментарии к посту')
    def delete_all_comments(self, request, queryset):
        for comment in queryset:
            comment.comments.clear()
        self.message_user(request, f'Комменты удалены')

    def authors_link(self, obj):
        user = obj.author
        url = reverse("admin:pc_app_user_changelist") + str(user.pk)
        return format_html(f'<a href="{url}"> {user} </a>')

    authors_link.short_description = 'Авторы'


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'age', 'is_active')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author')
    list_filter = ('author',)
    search_fields = ('text',)


admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
