from django import forms
from django.core.exceptions import ValidationError

from core.models import User

class RegisterAccountForm(forms.ModelForm):
    
    gender = forms.ChoiceField(label='جنسیت', choices=User.GenderType.choices, widget=forms.RadioSelect)
    password = forms.CharField(label='گذرواژه', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='تایید گذرواژه', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'gender', 'email', 'password', 'confirm_password',)
        
    
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password', None)
        confirm_password = cleaned_data.get('confirm_password', None)
        
        if password != confirm_password:
            raise ValidationError('رمز های عبور یکسان نیست.')

        return cleaned_data

        

class LoginAccountForm(forms.Form):
    
    username = forms.CharField(label='نام کاربری')
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)


class EditAccountForm(forms.ModelForm):
    
    new_password = forms.CharField(label='گذرواژه جدید', widget=forms.PasswordInput, required=False)
    confirm_new_password = forms.CharField(label='تایید گذرواژه جدید', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'new_password', 'confirm_new_password')
        widgets = {
            'first_name': forms.TextInput(attrs={'readonly': True}),
            'last_name': forms.TextInput(attrs={'readonly': True})
        }

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password', None)
        new_confirm_password = cleaned_data.get('new_confirm_password', None)
        
        if new_password and new_confirm_password and \
                        new_password != new_confirm_password:
            raise ValidationError('رمز های عبور جدید یکسان نیست.')

        return cleaned_data