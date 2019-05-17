from django.contrib import admin
from . import models


@admin.register(models.Bar)
class BarAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'keyword',
        'address',
        'created_at',
    )


@admin.register(models.BarLike)
class BarLikeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'bar',
        'creator',
    )