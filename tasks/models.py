from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import UserManager
class Estudiante(models.Model):
    username = models.CharField(max_length=50,unique=True)
    codigo = models.CharField(unique=True)
    password = models.CharField()
    grupo = models.CharField(max_length=50)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
    PASSWORD_FIELD = 'password'
    is_authenticated = True
    is_anonymous = False
    object= UserManager()
    check_password = True






