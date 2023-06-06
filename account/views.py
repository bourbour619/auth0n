from django.views.generic import FormView, RedirectView, View, ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy, reverse, resolve
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.utils.translation import gettext as _

from core.views import Auth0nView
from .models import User
from .forms import *


# Create your views here.

class RegisterAccountView(FormView):
    form_class = RegisterAccountForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('account:login')
    


    def form_valid(self, form):
        user = form.save(commit=False)
        user.type = User.UserType.STAFF
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        self.username = user.username
        return super().form_valid(form)
    
    def get_success_url(self):
        url = self.success_url
        if self.username:
            url += f'?username={self.username}'
        return url

    

            

class LoginAccountView(FormView):
    form_class = LoginAccountForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('account:profile')

    def get_initial(self):
        form_initial = super().get_initial()
        if self.request.method == 'GET':
            username = self.request.GET.get('username')
            form_initial['username'] = username
        return form_initial

    def form_valid(self, form):
        username = form['username'].value()
        password = form['password'].value()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        else:
            form.add_error(None, _('Username or Password is wrong.'))
            return super().form_invalid(form)
        messages.info(self.request, _('Welcome dear user.'))
        return super().form_valid(form)

    def get_success_url(self):
        next = self.request.GET.get('next')
        return next if next else self.success_url
        

class ProfileAccountRedirectView(RedirectView):
    url = reverse_lazy('account:edit')
    
    
class EditAccountView(LoginRequiredMixin, Auth0nView, FormView):
    template_name = 'account/profile/edit.html'
    form_class = EditAccountForm
    success_url = reverse_lazy('account:edit')

    def get_initial(self):
        form_initial = super().get_initial()
        form_initial['email'] = self.user.email
        form_initial['first_name'] = self.user.first_name
        form_initial['last_name'] = self.user.last_name
        return form_initial
    
    def form_valid(self, form):
        email = form.cleaned_data['email']
        new_password = form.cleaned_data['new_password']
        try:
            user = User.objects.get(username=self.user.username)
        except User.DoesNotExist:
            return HttpResponseRedirect(reverse('account:logout'))
        if email:
            user.email = email
        if new_password:
            user.set_password(new_password)
        user.save()
        messages.success(self.request, _('Account information updated.'))
        return super().form_valid(form)
        

    
        

class GroupsAccountView(LoginRequiredMixin, Auth0nView, ListView):
    template_name = 'account/profile/groups.html'
    model = Group
    context_object_name = 'groups'

    def get_queryset(self):
        queryset = Group.objects.filter(user=self.user)
        return queryset
    
    

class PermissionsAccountView(LoginRequiredMixin, Auth0nView, ListView):
    template_name = 'account/profile/permissions.html'
    model = Permission
    context_object_name = 'permissions'

    def get_queryset(self):
        queryset = Permission.objects.filter(user=self.user)
        return queryset


class SessionsAccountView(LoginRequiredMixin, Auth0nView, ListView):
    template_name = 'account/profile/sessions.html'
    model = Session
    context_object_name = 'sessions'

    def get_queryset(self):
        queryset = Session.objects.all()
        return queryset

    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
