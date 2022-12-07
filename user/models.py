from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.
class User(AbstractBaseUser):
    """
    일반 유저 모델
    """

    nickname = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)
    year = models.IntegerField()
    area = models.TextField()
    master = models.BooleanField()

    USERNAME_FIELD = 'nickname'

    class Meta:
        db_table = "User"

"""class CEO(AbstractBaseUser):
    
   
    
    ceo_nickname = models.CharField(max_length=24, unique=True)
    ceo_name = models.CharField(max_length=24)
    ceo_email = models.EmailField(unique=True)

    USERNAME_FIELD = 'ceo_nickname'

    class Meta:
        db_table = "CEO_User"""

