from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from posts.models import TimeStampedModel


# AbstractUser은 장고에 기본적으로 있는 유저 모델입니다.
# 이 모델은 유용한 필드들을 미리 지정해놓았기 때문에 이 모델을 상속받고, 필요한 필드들을 추가했습니다.
class User(AbstractUser):
    """ User Model """
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    profile_image = models.ImageField(
        upload_to=f'profile_images/', # 프로필 이미지가 업로드 되면 media/profile_images 파일에 모임, 각 앱마다 다른 파일에 게시되도록 upload_to 필드를 설정해준 것
        blank=True, # 유저가 회원가입할 때, 프로필 이미지를 넣지 않아도 회원가입이 되도록 설정해주기 위함
        null=True, # null값을 갖을 수 있음
        )
    name = models.CharField(max_length=255, null=True) #null 값은 갖을 수 있으나, blank=False(기본값)이기 때문에 유저는 꼭 이름을 적어야 함
    bio = models.TextField(blank=True, null=True) # 짧은 자기소개
    phone = models.CharField(max_length=140, blank=True, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True) # choices를 설정함으로써, 유저가 한정적인 답을 줄 수 있도록 함

    # 유저가 다른 유저들로부터 받은 하트 개수
    @property
    def userlike_count(self):
        return self.userlike_to.count()
    
    # 유저가 다른 유저들로부터 받은 쪽지 개수
    @property
    def letter_count(self):
        return self.letter_to.count()

    def __str__(self):
        return self.username


class UserLike(TimeStampedModel):
    """  UserLike Model"""
    userlike_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, # config/settings.py에 설정한 '신뢰할 수 있는 유저 모델'을 가져와 사용/현재는 위에 있는 User모델이 설정되어 있는 것을 확인할 수 있음
        on_delete=models.PROTECT, # 유저가 회원탈퇴(해당 유저데이터 삭제)를 해도 좋아요는 삭제 하지 않게함
        null=True, 
        related_name='userlike_to' # User 모델에서 UserLike를 불러올 때 해당 이름으로 부를 수 있음
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
        on_delete=models.SET_DEFAULT, # 쪽지를 받은 유저가 회원탈퇴를 할 경우 쪽지를 삭제하지 않고, 회원이름이 '알수없음'으로 설정됨
        null=True, 
        default='알수없음', 
        related_name='letter_to'
        )
    letter_from = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_DEFAULT, 
        null=True, 
        default='알수없음'
        )
    text = models.TextField(null=True)
    check = models.BooleanField(default=False) # letter_to 유저가 해당 쪽지를 확인했는지 체그하는 필드
    