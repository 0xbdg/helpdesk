from django import forms
from django.forms.widgets import *
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class ProblemForm(forms.Form):
    title = forms.CharField(required=True, widget=TextInput(attrs={"class":"form-control"}))
    description = forms.CharField(required=True, widget=Textarea(attrs={"class":"form-control"}))
    date = forms.DateField(widget=DateInput(attrs={"class":"form-control", "type":"date"}))

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(required=True, widget=PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ["username", "password"]

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=PasswordInput(attrs={"class":"form-control"}))
    new_password1 = forms.CharField(widget=PasswordInput(attrs={"class":"form-control"}))
    new_password2 = forms.CharField(widget=PasswordInput(attrs={"class":"form-control"}))

class UpdateProfile(UserChangeForm):
    first_name = forms.CharField(required=True, widget=TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(required=True, widget=TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(required=True, widget=TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(required=True, widget=EmailInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ["username", "first_name","last_name","email"]