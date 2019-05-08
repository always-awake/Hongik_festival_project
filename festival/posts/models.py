from django.conf import settings
from django.db import models

# 데이터가 생성되고, 수정된 시간을 자동으로 기입하기 위해 베이스 모델을 만듦
# 생성시간, 수정시간 필드가 필요한 모델은 TimeStampedModel 을 상속받아 사용하면 됨
class TimeStampedModel(models.Model):
    """Base Model"""
    created_at = models.DateTimeField(auto_now_add=True) #게시 시간 추가
    updated_at = models.DateTimeField(auto_now=True) #수정 시간 새로고침

    # 이렇게 설정해줌으로써, TimeStampedModel은 데이터베이스에 기록되지 않음
    class Meta:
        abstract = True


class Post(TimeStampedModel):
    """ Post Model """
    title = models.CharField(max_length=140)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='posts'
        )
    image = models.ImageField(upload_to=f'posts/')
    text = models.TextField(max_length=200)
    how_many = models.IntegerField(default=1) # 몇대몇 미팅을 구하는지 인원수 
    activate = models.BooleanField(default=True) # 미팅대상을 구했으면 False, 구하고 있는 중이면 True

    def __str__(self):
        return f'{self.title}-{self.creator}'

    # 가장 최근 post가 상위에 노출되도록 DB정렬 순서 정렬
    class Meta:
        ordering = ['-created_at']