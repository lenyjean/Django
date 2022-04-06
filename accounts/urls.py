from django.urls import path
from .views import *

urlpatterns = [
    path("account-list", accounts, name="account-list"),
    path("update-account/<int:pk>", user_update, name="update-account"),
    path("delete-account/<int:pk>", user_delete, name="delete-account"),
    path("create-admin-account", AdminSignUpView.as_view(), name="admin-sign-up"),
    path("create-staff-account", StaffSignUpView.as_view(), name="staff-sign-up"),
]