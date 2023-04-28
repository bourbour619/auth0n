from django.urls import path
from .views import *

urlpatterns = [
    path('register/', view=RegisterView.as_view(), name='register'),
    path('login/', view=LoginView.as_view(), name='login')
]
