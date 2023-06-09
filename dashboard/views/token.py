from django.shortcuts import render
from oauth2_provider.views.token import AuthorizedTokensListView, AuthorizedTokenDeleteView
from django.contrib import messages
from django.utils.translation import gettext as _
from django.urls import reverse_lazy

from core.views import Auth0nView


class TokenListView(Auth0nView, AuthorizedTokensListView):
    template_name = 'dashboard/tokens/list.html'



class TokenDeleteView(Auth0nView, AuthorizedTokenDeleteView):
    success_url = reverse_lazy('dashboard:tokens')

    def form_valid(self, form):
        authorized_token = super().get_object()
        messages.error(self.request,
                     _('Token %(token)s for user %(user)s deleted.' ) % {
                                                            "token": authorized_token.token,
                                                            "user": authorized_token.user
                                                        })
        return super().form_valid(form)