from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def bookings(request):
    template_name = "bookings/bookings_list.html"
    active_bookings = Bookings.objects.filter(Q(status="Pending") | Q(status="Late"))
    inactive_bookings = Bookings.objects.filter(Q(status="Done") | Q(status="Cancelled"))
    context = {
        "active_bookings": active_bookings,
        "inactive_bookings" : inactive_bookings
    }
    return render (request, template_name, context)

