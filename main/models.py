from django.db import models
import threading
import time

""" money = models.IntegerField()  # 시급
    year = models.IntegerField() #년
    month = models.IntegerField() # 월
    date = models.IntegerField # 일
    gender = models.BooleanField() # 성병 true == 남자 false == 여자
    region = models.TextField() # 지역"""

# Create your models here.
class Todo(models.Model):

    Todo_list = models.TextField()  # todolist
    month_year = models.TextField() # 달 월
    day = models.IntegerField() # 날
    email = models.EmailField() # 사용자 정보
    class Meta:
        db_table = "Todotext"

class Upload(models.Model):

    title_box = models.TextField() # 제목
    content_box = models.TextField() # 본문
    email = models.EmailField() # 사용자 정보
    start = models.TextField() #근무 시작일
    end = models.TextField() #근무 마감일
    area = models.TextField() # 지역
    gender = models.CharField(max_length=3) # 성별
    money = models.IntegerField() #시급
    class Meta:
        db_table = "Upload"

class Hots(models.Model):
    title_box = models.TextField()  # 제목
    content_box = models.TextField()  # 본문
    email = models.EmailField()  # 사용자 정보
    start = models.TextField()  # 근무 시작일
    end = models.TextField()  # 근무 마감일
    area = models.TextField()  # 지역
    gender = models.CharField(max_length=5)  # 성별
    start_money = models.IntegerField()  # 시작 시급
    end_money = models.IntegerField() # 종료 시급
    image = models.TextField(default="#") # 더미 이미지 //구현 실패

    class Meta:
        db_table = "Hottimes"





