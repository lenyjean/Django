from django.shortcuts import render
from .models import *

# Create your views here.
def bookings(request):
    template_name = "bookings/bookings_list.html"
    bookings = Bookings.objects.all()
    context = {
        "bookings" :  bookings
    }
    return render (request, template_name, context)

