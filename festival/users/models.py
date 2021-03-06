from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from posts.models import TimeStampedModel


class User(AbstractUser):
    """ User Model """
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    profile_image = models.ImageField(
        upload_to='profile_images',
        blank=True,
        null=True
        )
    name = models.CharField(max_length=140, blank=False, null=True)
    phone = models.CharField(max_length=225, blank=False, null=True) 
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    profile_open = models.BooleanField(default=True, null=True)

    @property
    def userlike_count(self):
        return self.userlike_to.count()
    
    @property
    def post_count(self):
        return self.posts.count()

    def __str__(self):
        return self.username


class UserLike(TimeStampedModel):
    """  UserLike Model"""
    userlike_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True, 
        related_name='userlike_to'
        ) # 유저 좋아요 받는 대상 유저
    userlike_from = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        null=True,
        ) # 유저 좋아요 보내는 유저

    def __str__(self):
        return f'{self.userlike_to.id}-{self.userlike_from.id}'


class Letter(TimeStampedModel):
    """ Letter Model """
    letter_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT,
        null=True, 
        related_name='letter_to'
        )
    letter_from = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT, 
        null=True, 
        related_name='letter_from'
        )
    text = models.TextField(null=True)
    check_to = models.BooleanField(default=False, null=True)
    check_from = models.BooleanField(default=False, null=True)
    delete_to = models.BooleanField(default=False, null=True) # 받은쪽이 삭제
    delete_from = models.BooleanField(default=False, null=True) # 보낸 쪽이 삭제
    # 쪽지함에서 삭제(실제로 디비에서 삭제되는 것이 아닌 목록에 띄우지 않는 것임)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.letter_to.name}-{self.letter_from.name}'
