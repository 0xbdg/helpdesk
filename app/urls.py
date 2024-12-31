from django.urls import path
from django.contrib.auth.views import PasswordChangeDoneView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path('accounts/login/', signin, name="login"),
    path("logout/", signout, name="logout"),
    path("profile/", profile, name="profile"),

    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path("password_reset/",PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/",PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', PasswordResetCompleteView.as_view(), name="password_reset_complete")
]