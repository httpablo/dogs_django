from django.contrib import admin
from . import models


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'img',)
    search_fields = ('user', 'name',)


admin.site.register(models.Photo, PhotoAdmin)
