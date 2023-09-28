from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    # LOGOUT AND LOGIN ROUTES
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # PASSWORD CHANGE ROUTES
    path("password-change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    # PASSWORD RESET ROUTES
    path("password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password-reset/<uuid64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_comfirm"),
    path("password-reset/complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
