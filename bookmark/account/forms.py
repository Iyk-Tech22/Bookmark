""" 
    This module handles the generating forms,
    pass data from user into the app
"""
from django import forms

#LOGIN FORM
class LoginForm(forms.Form):
    """ Generate user login form """
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

