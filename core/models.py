from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(AbstractUser, BaseModel):
    class UserType(models.IntegerChoices):
        STAFF = 1
        SUBSCRIBER = 2
        OTHER = 3

    type = models.IntegerField(choices=UserType.choices)
    userstore = models.ForeignKey(to='UserStore', on_delete=models.SET_NULL, null=True)

class UserStore(models.Model):
    class UserStoreType(models.IntegerChoices):
        SYSTEM = 1
        APP = 2
    name = models.CharField(max_length=20)
    type = models.IntegerField(choices=UserStoreType.choices)
    active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    attrs = models.JSONField(default={})

  