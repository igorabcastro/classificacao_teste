from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nomeCompleto = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['nomeCompleto', 'email', 'username']


