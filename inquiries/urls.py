from django.urls import path
from .views import *

urlpatterns = [
    path("inquiries-list", inquiries, name="inquiries_list")
]