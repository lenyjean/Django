from django.urls import path
from .views import *

urlpatterns = [
    path("account-list", accounts, name="account-list"),
    path("view-profile", viewprofile, name="view-profile"),
    path("update-profile/<int:pk>", profile_update, name="update-profile"),
    path("update-account/<int:pk>", user_update, name="update-account"),
    path("delete-account/<int:pk>", user_delete, name="delete-account"),
    path("create-admin-account", AdminSignUpView.as_view(), name="admin-sign-up"),
    path("create-staff-account", StaffSignUpView.as_view(), name="staff-sign-up"),
    path("update-password", update_password, name="update_password"),
    path("delete-user/<int:pk>", UserDetailView.as_view(), name="delete_user"),
]