from django.urls import path
from .views import *

urlpatterns = [
    path("account-list", accounts, name="account-list"),
    path("create-admin-account", AdminSignUpView.as_view(), name="admin-sign-up"),
    path("create-staff-account", StaffSignUpView.as_view(), name="staff-sign-up"),
]