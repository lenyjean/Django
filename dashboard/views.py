from django.shortcuts import render, redirect, get_object_or_404

from .models import *

# Create your views here.
def homepage(request):
    template_name = "dashboard/homepage.html"
    context = {}
    return render(request, template_name, context)