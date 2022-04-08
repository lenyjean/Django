from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import *

class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["last_name", "first_name", "email", "username"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return user

class StaffSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["last_name", "first_name", "email", "username"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
        return user


class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["last_name", "first_name", "email", "username"]