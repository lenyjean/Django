from django.urls import path

from .views import *

urlpatterns = [
    path('api/webhooks/hub.mode=<str:mode>&hub.verify_token=<str:token>&hub.challenge=<str:challenge>', Webhooks, name='webhooks_verify'),
]