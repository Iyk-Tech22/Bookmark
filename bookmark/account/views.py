from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
from django.urls import reverse
# LOGIN VIEW
def user_login(request):
    """ Handle login of users """
    
    if request.method == "POST":
        """ checks for post request """
        
        form = LoginForm(request.POST)
        if form.is_valid:
            form_data = form.cleaned_data
            user = authenticate(
                request,
                username=form_data["username"],
                password=form_data["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authentication Successful...")
                else:
                    return HttpResponse("Account Disabled")
            else:
                HttpResponse("Invalid Login Details")
    else:
        form = LoginForm()
    context = {
        "form":form
    }
    return render(request, "account/login.html", form)
    
# DASHBOARD VIEW
@login_required
def dashboard(request):
    """ handle request to dashboard route """
    context = {
       "section":"dashboard",
       "title":"Dashboard"
    }
    return render(request, "account/dashboard.html", context)

# USER REGISTRATION
def user_registration(request):
    """ handles user registrtion request """
    if request.user.is_authenticated:
        return redirect(reverse("dashboard"))
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            password = form.clean_password_confirm()
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            return render(request, "registration/register_done.html", {"user": user})
    else:
        form = UserRegistrationForm()
    context = {
        "form" : form
    }
    return render(request, "registration/register.html", context)