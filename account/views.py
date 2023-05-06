from typing import Any, Dict
from core.models import User
from django.views.generic import FormView, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from .forms import *

# Create your views here.

class RegisterAccountView(FormView):
    form_class = RegisterAccountForm
    template_name = 'account/register.html'
    success_url = '/account/login/'
    


    def form_valid(self, form):
        user = form.save(commit=False)
        user.type = User.UserType('STAFF')
        password = form['password'].value()
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
    success_url = '/account/'

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
            form.add_error(None, 'نام کاربری یا رمز عبور اشتباه است')
            return super().form_invalid(form)
        return super().form_valid(form)
        


class ProfileAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        return context
    
def logout_view(request):
    logout(request)
    return redirect(reverse('index'))


