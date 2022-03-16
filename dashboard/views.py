from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required
def homepage(request):
    template_name = "dashboard/homepage.html"
    context = {}
    return render(request, template_name, context)

