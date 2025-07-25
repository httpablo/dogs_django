from django.contrib import admin
from . import models


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'photo', 'comment',)
    search_fields = ('user', 'comment',)


admin.site.register(models.Comment, CommentAdmin)
