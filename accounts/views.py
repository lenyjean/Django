from django.shortcuts import render
from .models import *

# Create your views here.
def accounts(request):
    template_name = "user_accounts/accounts.html"
    accounts = Accounts.objects.all()
    context = {}
    return render (request. template_name, context)