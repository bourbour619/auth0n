from django.urls import path
from .views import *


app_name = 'dashboard'

urlpatterns = [
    path('', DashboardRedirectView.as_view(), name='overview'),
    path('overview/', OverviewView.as_view(), name='overview'),
    path('applications/create/', ApplicationCreateView.as_view(), name='application_create'),
    path('applications/', ApplicationListView.as_view(), name='applications'),
    path('applications/edit/<str:pk>/', ApplicationUpdateView.as_view(), name='application_edit'),
    path('applications/delete/<int:pk>/', ApplicationDeleteView.as_view(), name='application_delete'),
    path('tokens/', TokenListView.as_view(), name='tokens'),
    path('tokens/delete/<int:pk>/', TokenDeleteView.as_view(), name='token_delete'),
]