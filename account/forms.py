from django import forms

class RegisterAccountForm(forms.Form):
    template_name = 'account/form_snippet.html'
    
    first_name = forms.CharField(label='نام', max_length=30)
    last_name = forms.CharField(label='نام خانوادگی', max_length=30)
    email = forms.CharField(label='ایمیل', widget=forms.EmailInput)
    mobile = forms.CharField(label='تلفن همراه')
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='تایید رمز عبور', widget=forms.PasswordInput)



class LoginAccountForm(forms.Form):
    template_name = 'account/form_snippet.html'
    
    email = forms.CharField(label='ایمیل', widget=forms.EmailInput)
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)