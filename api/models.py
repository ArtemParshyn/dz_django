from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class ApiUser(AbstractUser):
    ...


class Storage(models.Model):
    name = models.CharField(max_length=120)


class Good(models.Model):
    name = models.CharField(max_length=120)
    #quantity = models.PositiveIntegerField()
