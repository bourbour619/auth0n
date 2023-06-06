from django.views.generic.base import View
from django.urls import resolve

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