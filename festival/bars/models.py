from django.conf import settings
from django.db import models
from posts.models import TimeStampedModel


class Bar(TimeStampedModel):
    """ Bar Model """
    name = models.CharField(max_length=80)
    represent_image = models.ImageField(upload_to='bars')
    first_image = models.ImageField(upload_to='bars')
    second_image = models.ImageField(upload_to='bars')
    third_image = models.ImageField(upload_to='bars')
    summary = models.CharField(max_length=300, null=True)
    text = models.TextField(max_length=200) # 술집에 대한 간단한 소개
    location_url = models.TextField(max_length=200) # 술집 위치 -> 이후 필요에 따라 변경될 가능성이 높은 필드
    keyword = models.CharField(max_length=80, null=True) # 술집을 한단어로 표현하는 키워드
    address = models.CharField(max_length=300, null=True) # 홍대 정문에서 몇 분 이런식으로
    first_menu = models.CharField(max_length=150, null=True, blank=True) # 추천 메뉴1
    second_menu = models.CharField(max_length=150, null=True, blank=True) # 추천 메뉴2
    third_menu = models.CharField(max_length=150, null=True, blank=True) # 추천 메뉴3
    fourth_menu = models.CharField(max_length=150, null=True, blank=True) # 추천 메뉴4

    @property
    def barlike_count(self):
        return self.likes.count()
    
    def __str__(self):
        return f'{self.name}'
    

class BarLike(TimeStampedModel):
    """ BarLike Model """
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE, related_name='likes')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.bar.name}-{self.creator.name}'
    
