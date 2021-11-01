
from django.contrib.auth.models import AbstractUser
from django.db import models

class Permissions(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=200)
    permissions = models.ManyToManyField(Permissions)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.username

