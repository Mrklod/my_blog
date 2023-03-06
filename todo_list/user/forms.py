from django import forms
from .models import Users

class FormRegister(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    }))
    class Meta:
        model = Users
        fields = ('username','email','password1','password2')


class FormLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
    }))
    class Meta:
        model = Users
        fields = ('username','password')