from django.db import models
from django.utils import timezone
from django.core import validators

# Create your models here.

# class Board(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Board(models.Model): # 기존의 모델에 validator만 추가해줍니다.
    id = models.AutoField(primary_key=True)
    title = models.CharField("제목", max_length=255,
                             validators=[
                                 validators.MinLengthValidator(2, "최소 세 글자 이상은 입력해주셔야 합니다.")
                             ])
    content = models.TextField("내용", validators=[ validators.MinLengthValidator(10, "최소 10글자 이상은 입력하셔야 합니다.")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Comment(models.Model):
    board = models.ForeignKey(Board, null=True ,on_delete=models.SET_NULL)
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=255,
                               validators=[
                                   validators.MinLengthValidator(5, "다섯글자 이상은 입력하십시오")
                               ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)