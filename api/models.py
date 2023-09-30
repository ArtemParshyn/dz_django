from django.db import models
from django.contrib.auth.models import AbstractUser

class ApiUser(AbstractUser):
    ...

class Storage(models.Model):
    name = models.CharField(max_length=120)


class Good(models.Model):
    quantity = models.PositiveIntegerField()
    hotel = models.ForeignKey(Storage, related_name='storage', on_delete=models.CASCADE)
