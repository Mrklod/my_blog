from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from .models import Users

class FormRegister(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    }))
    class Meta:
        model = Users
        fields = ('username','email','password1','password2')


class FormLogin(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
    }))
    class Meta:
        model = Users
        fields = ('username','password')