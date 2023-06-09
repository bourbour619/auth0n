from django.shortcuts import render
from oauth2_provider.views.application import ApplicationRegistration , ApplicationList, ApplicationDelete, ApplicationUpdate
from django.contrib import messages
from django.utils.translation import gettext as _
from django.urls import reverse_lazy

from core.views import Auth0nView



class ApplicationCreateView(Auth0nView, ApplicationRegistration):
    template_name = 'dashboard/applications/create.html'
    success_url = reverse_lazy('dashboard:applications')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        messages.success(self.request, _('Application %(name)s created.') % {"name": name})
        return super().form_valid(form)



class ApplicationListView(Auth0nView, ApplicationList):
    template_name = 'dashboard/applications/list.html'



class ApplicationUpdateView(Auth0nView, ApplicationUpdate):
    template_name = 'dashboard/applications/edit.html'
    success_url = reverse_lazy('dashboard:applications')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        messages.success(self.request, _('Application %(name)s updated.') % {"name": name})
        return super().form_valid(form)



class ApplicationDeleteView(Auth0nView, ApplicationDelete):
    success_url = reverse_lazy('dashboard:applications')

    def form_valid(self, form):
        application = super().get_object()
        messages.error(self.request, _('Application %(name)s deleted.' ) % {"name": application.name})
        return super().form_valid(form)