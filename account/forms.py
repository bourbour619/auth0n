from django import forms
from django.core.exceptions import ValidationError

from core.models import User

class RegisterAccountForm(forms.ModelForm):
    template_name = 'account/form_snippet.html'
    
    gender = forms.ChoiceField(label='جنسیت', choices=User.GenderType.choices, widget=forms.RadioSelect)
    password = forms.CharField(label='گذرواژه', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='تایید گذرواژه', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'gender', 'email', 'password', 'confirm_password',]
        
    
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password', None)
        confirm_password = cleaned_data.get('confirm_password', None)
        
        if password != confirm_password:
            raise ValidationError('رمز های عبور یکسان نیست.')

        return cleaned_data

        




class LoginAccountForm(forms.Form):
    template_name = 'account/form_snippet.html'
    
    username = forms.CharField(label='نام کاربری')
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)