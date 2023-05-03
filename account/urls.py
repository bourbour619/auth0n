from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('register/', view=RegisterView.as_view(), name='register'),
    path('login/', view=LoginView.as_view(), name='login'),
    path('profile/', view=ProfileView.as_view(), name='profile'),
    path('logout/', view=logout_view, name='logout')
]
