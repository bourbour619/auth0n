from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.views import Auth0nView

class OverviewView(LoginRequiredMixin, Auth0nView, TemplateView):
    template_name = 'dashboard/overview.html'