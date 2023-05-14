from django.contrib import admin
from .models import User, UserStore
from django.contrib.auth.models import Permission

# Register your models here.

admin.site.register(User)
admin.site.register(Permission)
admin.site.register(UserStore)