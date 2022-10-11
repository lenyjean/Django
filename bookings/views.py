from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q

from .forms import *

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

@login_required(login_url='/accounts/login')
def bookings_update(request, pk):
    template_name = "bookings/bookings_update.html"
    bookings = get_object_or_404(Bookings, pk=pk)
    form = BookingsForms(request.POST or None, instance=bookings)
    if form.is_valid():
         form.save()
         return redirect("bookings-list")
    context = {
        "form" : form
    }
    return render (request, template_name, context)

