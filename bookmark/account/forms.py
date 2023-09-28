""" 
    This module handles the generating forms,
    pass data from user into the app
"""
from django import forms
from django.contrib.auth.models import User

#LOGIN FORM
class LoginForm(forms.Form):
    """ Generate user login form """
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

# USER REGISTRATION
class UserRegistrationForm(forms.ModelForm):
    """ Generate a form to allow user to create a account """
    password = forms.CharField(label="Enter Your Password", widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirm Your Password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "first_name", "email"]
    
    def clean_password_confirm(self):
        """ Check match for both inputed password """
        cd = self.cleaned_data
        if cd["password"] != cd["password_confirm"]:
            raise forms.ValidationError("password not match")
        return cd["password_confirm"]
