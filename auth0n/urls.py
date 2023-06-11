"""
URL configuration for auth0n project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from account.views import ProfileAccountRedirectView
from core.views import AuthorizationView, TokenView, RevokeTokenView

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', ProfileAccountRedirectView.as_view(), name='index'),
    path('account/', include('account.urls', namespace='account')),
    path('dashboard/', include('dashboard.urls', namespace='dashbaord')),
    path('authorize/', AuthorizationView.as_view(), name='authorize'),
    prefix_default_language=False
)

urlpatterns += [
    path("i18n/", include("django.conf.urls.i18n")),
    path('token/', TokenView.as_view(), name='token'),
    path('revoke-token/', RevokeTokenView.as_view(), name='revoke_token')
]