from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from orders.models import *
from products.models import *

# Create your views here.
@login_required
def homepage(request):
    template_name = "dashboard/homepage.html"
    orders = Orders.objects.all()[:5]
    products = Products.objects.all()[:5]
    context = {
        "orders" : orders,
        "products" : products
    }
    return render(request, template_name, context)


