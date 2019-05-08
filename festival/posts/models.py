from django.db import models


class TimeStampedModel(models.Model):
    """Base Model"""
    created_at = models.DateTimeField(auto_now_add=True) #게시 시간 추가
    updated_at = models.DateTimeField(auto_now=True) #수정 시간 새로고침

    class Meta:
        abstract = True