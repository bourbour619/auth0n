from django.contrib import admin
from .models import User, UserStore

# Register your models here.

admin.site.register(User)
admin.site.register(UserStore)