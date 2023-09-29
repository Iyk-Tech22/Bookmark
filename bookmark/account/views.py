from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.urls import reverse
from .models import Profile
from django.contrib import messages


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
            profile = Profile(user=user)
            profile.save()
            return render(request, "registration/register_done.html", {"user": user})
    else:
        form = UserRegistrationForm()
    context = {
        "form" : form
    }
    return render(request, "registration/register.html", context)

# EDIT USER PROFILE
@login_required
def edit(request):
    """ Handles profile edit request """
    auth_user = request.user
    post_data = request.POST
    if request.method == "POST":
        profile_photo = request.FILES
        user_form = UserEditForm(instance=auth_user, data=post_data)
        profile_form = ProfileEditForm(instance=auth_user.profile, data=post_data, files=profile_photo)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile Update, Successfully!")
        else:
            messages.error(request, "Error updating your profile")
            
    else:
        user_form = UserEditForm(instance=auth_user)
        profile_form = ProfileEditForm(instance=auth_user.profile)
    context = {
        "user_form":user_form,
        "profile_form":profile_form
    }
    return render(request, "account/edit.html", context)