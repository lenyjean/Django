from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import *
from orders.models import *
from products.models import *
from category.models import *
from bookings.models import *
# from inquiries.models import *

import datetime

# Create your views here.
@login_required(login_url='/accounts/login')
def homepage(request):
    template_name = "dashboard/homepage.html"
    date = datetime.date.today()
    orders = Orders.objects.filter(status__in=["Pending", "Late"])[:5]
    products = Products.objects.filter(status__in=["Available"])[:5]
    orders_date = Orders.objects.filter(pickup_date=date, status="Pending")
    orders_today = Orders.objects.filter(pickup_date=date, status="Pending").count()

    total_orders = Orders.objects.filter(status__in=['Done', 'Pending', 'Cancelled', 'Late']).aggregate(Sum('no_of_order'))
    total_sales = Orders.objects.filter(status="Done").aggregate(Sum('total_amount'))
    total_products = Products.objects.filter(status="Available").count()
    # total_inquiries = Inquiries.objects.all().count()
    total_bookings = Bookings.objects.all().count()
    

    context = {
        "orders" : orders,
        "products" : products,
        "total_orders" : total_orders,
        "total_sales" : total_sales,
        "total_products" : total_products,
        # "total_inquiries" : total_inquiries,
        "total_bookings" : total_bookings,
        "orders_date" : orders_date,
        "date" : date,
        "orders_today" : orders_today,
        "dashboard_state" : "background-color: #dbeafe;"
    }
    return render(request, template_name, context)


