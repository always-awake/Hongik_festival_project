from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from festival.posts.models import TimeStampedModel

class User(models.Model):
    """ User Model """
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    profile_image = models.ImageField(upload_to=f'profile_images/', blank=True, null=True)
    name = models.CharField(max_length=255, null=True)
    bio = models.TextField(blank=True, null=True) # 짧은 자기소개
    phone = models.CharField(max_length=140, blank=True, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)

    def __str__(self):
        return self.username


class UserLike(TimeStampedModel):
    """  UserLike Model"""
    userlike_to = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    userlike_from = models.ForeignObject(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.userlike_to.id}-{self.userlike_from.id}'


class Letter(TimeStampedModel):
    """ Letter Model """
    letter_to = models.ForeignKey(User, on_delete=models.SET_DEFAULT, null=True, default='알수없음')
    letter_from = models.ForeignObject(User, on_delete=models.SET_DEFAULT, null=True, default='알수없음')
    text = models.TextField(null=True)
    check = models.BooleanField(default=False)
    