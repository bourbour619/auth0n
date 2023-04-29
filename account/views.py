from typing import Any, Dict
from core.models import User
from django.views.generic import FormView
from .forms import *

# Create your views here.

class RegisterView(FormView):
    form_class = RegisterAccountForm
    template_name = 'account/register.html'
    success_url = '/account/login/'
    


    def form_valid(self, form):
        user = form.save(commit=False)
        user.type = User.UserType('STAFF')
        user.save()
        self.username = user.username
        return super().form_valid(form)
    
    def get_success_url(self):
        url = self.success_url
        if self.username:
            url += f'?username={self.username}'
        return url

    

            

class LoginView(FormView):
    form_class = LoginAccountForm
    template_name = 'account/login.html'
    success_url = '/account/profile/'

    def get_initial(self):
        form_initial = super().get_initial()
        if self.request.method == 'GET':
            username = self.request.GET.get('username')
            form_initial['username'] = username
        return form_initial



