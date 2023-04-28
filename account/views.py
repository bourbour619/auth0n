from django.shortcuts import render
from django.views.generic import View
from .forms import *

# Create your views here.

class RegisterView(View):

    def get(self, request):
        form = RegisterAccountForm()
        return render(request, 'account/register.html', { 'form': form })
    
    def post(self, request):
        pass

            

class LoginView(View):

    def get(self, request):
        form = LoginAccountForm()
        return render(request, 'account/login.html', { 'form': form })



