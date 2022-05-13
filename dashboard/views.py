from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from orders.models import *
from products.models import *
from category.models import *
from bookings.models import *
# Create your views here.
@login_required
def homepage(request):
    template_name = "dashboard/homepage.html"
    orders = Orders.objects.all()[:5]
    products = Products.objects.all()[:5]

    total_orders = Orders.objects.all().count()
    total_sales = Orders.objects.filter(status="Done").count()
    total_category = Category.objects.filter(status=True).count()
    total_bookings = Bookings.objects.filter(status=True).count()
    
    context = {
        "orders" : orders,
        "products" : products,
        "total_orders" : total_orders,
        "total_sales" : total_sales,
        "total_category" : total_category,
        "total_bookings" : total_bookings
    }
    return render(request, template_name, context)


