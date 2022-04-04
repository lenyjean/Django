from django.shortcuts import render
from .models import *

# Create your views here.
def inquiries(request):
    template_name = "inquiries/inquiries_list.html"
    inquiries = Inquiries.objects.all()
    context = {
        "inquiries" : inquiries
    }
    return render (request, template_name, context)

