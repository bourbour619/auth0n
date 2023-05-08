from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('', view=ProfileAccountRedirectView.as_view(), name='account-profile'),
    path('register/', view=RegisterAccountView.as_view(), name='account-register'),
    path('login/', view=LoginAccountView.as_view(), name='account-login'),
    path('edit/', view=EditAccountView.as_view(), name='account-edit'),
    path('groups/', view=GroupsAccountView.as_view(), name='account-groups'),
    path('permissions/', view=PermissionsAccountView.as_view(), name='account-permissions'),
    path('sessions/', view=SessionsAccountView.as_view(), name='sessions'),
    path('logout/', view=logout_view, name='account-logout')
]
