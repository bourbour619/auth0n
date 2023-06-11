from django.views.generic.base import View
from django.urls import resolve
from django.http import QueryDict
from oauth2_provider.views import AuthorizationView as BaseAuthorizationView, TokenView as BaseTokenView, RevokeTokenView as BaseRevokeTokenView
from urllib.parse import urlencode
import json

# Create your views here.


class Auth0nView(View):
    def setup(self, request, *args, **kwargs):
        view = resolve(request.path)
        self.url = view.url_name
        if getattr(request, 'user'):
            self.user = request.user
        return super().setup(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = self.url
        if hasattr(self, 'user'):
            context['user'] = self.user
        return context


class AuthorizationView(BaseAuthorizationView):
    template_name = 'core/authorize.html'


class TokenView(BaseTokenView):
    
    def post(self, request, *args, **kwargs):
        content_type = request.headers.get('Content-Type', None)
        if content_type == 'application/json':
            body = json.loads(request.body)
            items = urlencode(body)
            request.POST = QueryDict(items)
            
        return super().post(request, *args, **kwargs)
    

class RevokeTokenView(BaseRevokeTokenView):

    def post(self, request, *args, **kwargs):
        content_type = request.headers.get('Content-Type', None)
        if content_type == 'application/json':
            body = json.loads(request.body)
            items = urlencode(body)
            request.POST = QueryDict(items)
            
        return super().post(request, *args, **kwargs)
