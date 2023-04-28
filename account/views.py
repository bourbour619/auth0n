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
        return super().form_valid(form)

            

class LoginView(FormView):
    form_class = LoginAccountForm
    template_name = 'account/login.html'
    success_url = '/account/profile/'



