from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import User

class RegisterAccountForm(forms.ModelForm):
    
    gender = forms.ChoiceField(label=_('Gender'), choices=User.GenderType.choices, widget=forms.RadioSelect)
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    confirm_password = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'gender', 'email', 'password', 'confirm_password',)
        
    
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password', None)
        confirm_password = cleaned_data.get('confirm_password', None)
        
        if password != confirm_password:
            raise ValidationError(_('Passwords doesn\'t match.' ))

        return cleaned_data

        

class LoginAccountForm(forms.Form):
    
    username = forms.CharField(label=_('Username'))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)


class EditAccountForm(forms.ModelForm):
    
    new_password = forms.CharField(label=_('New Password'), widget=forms.PasswordInput, required=False)
    confirm_new_password = forms.CharField(label=_('Confirm New Password'), widget=forms.PasswordInput, required=False)

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
            raise ValidationError(_('Passwords doesn\'t match.' ))

        return cleaned_data