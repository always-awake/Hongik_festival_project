from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class User(models.Model):
    """ User Model """
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified'),
    )
    profile_image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255, null=True)
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=140, blank=True, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)

    def __str__(self):
        return self.username
    