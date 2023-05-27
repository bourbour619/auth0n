from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserStore(models.Model):
    class UserStoreType(models.TextChoices):
        SYSTEM = 'SYSTEM'
        APP = 'APP'
    name = models.CharField(max_length=20, verbose_name=_('Name'))
    type = models.CharField(choices=UserStoreType.choices, verbose_name=_('Type'))
    active = models.BooleanField(default=True, verbose_name=_('Active'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    attrs = models.JSONField(default=dict, null=True, blank=True, verbose_name=_('Attributes'))

    class Meta:
        verbose_name = _('User Store')
        verbose_name_plural = _('User Store\'s')

    def __str__(self):
        return self.name

  