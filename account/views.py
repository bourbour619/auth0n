from django.views.generic import FormView, RedirectView, View, ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.urls import reverse, resolve
from django.contrib import messages

from core.models import User
from .forms import *


# Create your views here.

class RegisterAccountView(FormView):
    form_class = RegisterAccountForm
    template_name = 'account/register.html'
    success_url = '/account/login/'
    


    def form_valid(self, form):
        user = form.save(commit=False)
        user.type = User.UserType('STAFF')
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
        


class ProfileAccountView(LoginRequiredMixin, View):
    
    def setup(self, request, *args, **kwargs):
        self.user = request.user
        view = resolve(request.path)
        self.url = view.url_name
        return super().setup(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['url'] = self.url
        return context

class ProfileAccountRedirectView(RedirectView):

    def get_redirect_url(self):
        return reverse('account:edit')
    
class EditAccountView(ProfileAccountView, FormView):
    template_name = 'account/profile/edit.html'
    form_class = EditAccountForm

    success_url = '/account/edit/'

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
        messages.success(self.request, 'حساب کاربری به روزرسانی شد.')
        return super().form_valid(form)
        

    
        

class GroupsAccountView(ProfileAccountView, ListView):
    template_name = 'account/profile/groups.html'
    model = Group
    context_object_name = 'groups'

    def get_queryset(self):
        queryset = Group.objects.filter(user=self.user)
        return queryset
    
    

class PermissionsAccountView(ProfileAccountView):
    pass


class SessionsAccountView(ProfileAccountView):
    
    pass

    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


