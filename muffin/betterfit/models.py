from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

class User(AbstractUser):
    clothes_img = models.ImageField(null=True)
    #pants_img=models.ImageField(null=True)
    #outer_img=models.ImageField(null=True)


