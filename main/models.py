from django.db import models

# Create your models here.
class Todo(models.Model):

    Todo_list = models.TextField()  # todolist
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    email = models.EmailField() # 사용자 정보
    class Meta:
        db_table = "Todotext"