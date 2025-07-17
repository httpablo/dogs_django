from django.contrib import admin
from . import models
from comment.models import Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'img', 'accesses',)
    search_fields = ('user', 'name',)
    inlines = (CommentInline,)


admin.site.register(models.Photo, PhotoAdmin)
