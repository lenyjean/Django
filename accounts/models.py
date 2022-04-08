from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    status = models.BooleanField(default=True)