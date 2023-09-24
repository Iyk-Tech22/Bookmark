from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

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
        