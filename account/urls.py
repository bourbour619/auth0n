from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('', view=ProfileAccountView.as_view(), name='profile'),
    path('register/', view=RegisterAccountView.as_view(), name='register'),
    path('login/', view=LoginAccountView.as_view(), name='login'),
    path('edit/', view=EditAccountView.as_view(), name='edit'),
    path('groups/', view=GroupsAccountView.as_view(), name='groups'),
    path('permissions/', view=PermissionsAccountView.as_view(), name='permissions'),
    path('sessions/', view=SessionsAccountView.as_view(), name='sessions'),
    path('logout/', view=logout_view, name='logout')
]
