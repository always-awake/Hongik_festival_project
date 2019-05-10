from django.db import models

# Create your models here.
class board(models.Model):
    subject = models.CharField( max_length=50 , blank=True) # 제목
    name = models.CharField( max_length=50,blank=True) #이름
    created_date = models.DateField( null = True , blank = True) # 작성일
    mail = models.CharField( max_length=50,blank=True) # 메일
    memo = models.CharField( max_length=200,blank=True) #내용
    hits = models.IntegerField(null=True,blank=True) # 조회수

