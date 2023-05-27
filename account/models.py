from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser, BaseModel):

    class UserType(models.TextChoices):
        STAFF = 'Staff', _('Staff')
        SUBSCRIBER = 'Subscriber', _('Subscriber')
        OTHER = 'Other', _('Other')

    class GenderType(models.TextChoices):
        MALE = 'Male', _('Male')
        FEMALE = 'Female', _('Female')

    type = models.CharField(choices=UserType.choices, verbose_name=_('Type'))
    gender = models.CharField(choices=GenderType.choices, verbose_name=_('Gender'))
    userstore = models.ForeignKey(to='core.UserStore', on_delete=models.SET_NULL, null=True, verbose_name=_('User Store'))