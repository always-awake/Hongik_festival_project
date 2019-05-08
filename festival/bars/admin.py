from django.contrib import admin
from . import models


@admin.register(models.Bar)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'text',
    )
