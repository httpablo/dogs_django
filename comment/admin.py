from django.contrib import admin
from . import models


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'img', 'comment',)
    search_fields = ('user', 'comment',)


admin.site.register(models.Comment, CommentAdmin)
