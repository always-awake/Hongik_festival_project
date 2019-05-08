from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'gender',
        'phone',
    )


@admin.register(models.UserLike)
class UserLike(admin.Model):
    list_display = (
        'id',
        'userlike_to',
        'userlike_from',
    )