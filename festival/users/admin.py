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
class UserLikeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'userlike_to',
        'userlike_from',
    )


@admin.register(models.Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'letter_to',
        'letter_from',
        'check',
    )