from django.views.generic.base import RedirectView
from django.urls import reverse_lazy

class DashboardRedirectView(RedirectView):
    url = reverse_lazy('dashboard:overview')



from .application import ApplicationCreateView, ApplicationListView, ApplicationUpdateView, ApplicationDeleteView
from .overview import OverviewView
from .token import TokenListView, TokenDeleteView