from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    status = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    )
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    status = models.BooleanField(default=True)


class PasswordResetRequest(models.Model):
    token = models.CharField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    is_expired = models.BooleanField(default=False)