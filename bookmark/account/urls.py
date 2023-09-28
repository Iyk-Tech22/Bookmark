from typing import Any
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls as auth_urls
from . import views

auth_views.LoginView.redirect_authenticated_user = True

urlpatterns = [
    path("", include(auth_urls)),
    path("", views.dashboard, name="dashboard"),
    # # LOGOUT AND LOGIN ROUTES
    # path("login", auth_views.LoginView.as_view(redirect_authenticated_user=True), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # # PASSWORD CHANGE ROUTES
    # path("password-change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    # path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    # # PASSWORD RESET ROUTES
    # path("password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    # path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path("password-reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_comfirm"),
    # path("password-reset/complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
