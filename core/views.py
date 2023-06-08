from django.views.generic.base import View
from django.urls import resolve
from oauth2_provider.views import AuthorizationView as BaseAuthorizationView

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

    def form_valid(self, form):
        allow = form.cleaned_data.get("allow")
        return super().form_valid(form)


    def form_invalid(self, form):
        return super().form_invalid(form)