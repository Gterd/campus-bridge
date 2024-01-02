from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form
    

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'id':'LoginUsername',
            'type':"text",
            'required':'',
            'maxlength':'16',
        })
        self.fields['password'].widget.attrs.update({
            'id':'LoginPassword',
            'type':"password",
            'required':'',
        })
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'id':'RegisterUsername',
            'type':"text",
            'required':'',
            'maxlength':'16',
            'minlength':'4   ',
        })
        self.fields['email'].widget.attrs.update({
            'id':'RegisterEmail',
            'type':"email",
            'required':'',
        })
        self.fields['password1'].widget.attrs.update({
            'id':'RegisterPassword',
            'type':"password",
            'required':'',
        })
        self.fields['password2'].widget.attrs.update({
            'id':'RegisterPassword2',
            'type':"password",
            'required':'',
        })
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']