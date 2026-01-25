from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True)

    ROLE_CHOICE = (
        ('admin','admin'),
        ('patient','patient'),
        ('doctor','doctor')
    )
    role = models.CharField(max_length=50,choices=ROLE_CHOICE,default='patient')
    
