from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from orders.models import *
from django.db.models import Q

from .forms import *


# Create your views here.


@login_required
def orders_list(request):
    template_name = "orders/orders_list.html"
    active_orders = Orders.objects.filter(status="Pending")
    inactive_orders = Orders.objects.filter(status="Done")
    context = {
        "active_orders": active_orders,
        "inactive_orders" : inactive_orders
    }
    return render(request, template_name, context)


@login_required
def orders_add(request):
    template_name = "orders/orders_add.html"
    form = OrderForms(request.POST or None)
    if form.is_valid():
        get_price = Products.objects.get(product_name=form.cleaned_data['products'])
        customer_name = form.cleaned_data['customer_name']
        customer_address = form.cleaned_data['customer_address']
        products = form.cleaned_data['products']
        no_of_order = form.cleaned_data['no_of_order']
        total_amount = get_price.price  *  form.cleaned_data['no_of_order']
        pickup_date = form.cleaned_data['pickup_date']
        processed_by = request.user.username
        status = form.cleaned_data['status']
        
        orders = Orders.objects.get_or_create(
            customer_name=customer_name, customer_address=customer_address, products=products,
            no_of_order=no_of_order, total_amount=total_amount, pickup_date=pickup_date, processed_by=processed_by, status=status
        )

        return redirect("orders-list")
    context = {
        "form":  form
    }
    return render(request, template_name, context)


@login_required
def orders_view(request, pk):
    template_name = "orders/orders_view.html"
    orders = Orders.objects.filter(id=pk)
    context = {
        "orders": orders
    }
    return render(request, template_name, context)


@login_required
def orders_update(request, pk):
    template_name = "orders/orders_update.html"
    orders = get_object_or_404(Orders, pk=pk)
    form = OrderForms(request.POST or None, instance=orders)
    if form.is_valid():
        form.save()
        return redirect("orders-list")
    context = {
        "form":  form
    }
    return render(request, template_name, context)

@login_required
def orders_delete(request, pk):
    orders = Orders.objects.filter(id=pk).update(status=False)
    return redirect("orders-list")

@login_required
def messenger_list(request):
    template_name = "messenger_orders/m-orders_list.html"
    messenger_orders = MessengerOrders.objects.all()
    context = {
        "messenger_orders":  messenger_orders
    }
    return render(request, template_name, context)

@login_required
def messenger_add(request):
    template_name = "messenger_orders/m-orders_add.html"
    form = MessengerOrdersForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("m-orders-list")
    context = {
       "form" :  form
    }
    return render (request, template_name, context)

@login_required
def messenger_view(request, pk):
    template_name = "messenger_orders/m-orders_view.html"
    messenger_orders = MessengerOrders.objects.filter(id=pk)
    context = {
        "messenger_orders": messenger_orders
    }
    return render(request, template_name, context)

@login_required
def messenger_update(request, pk):
    template_name = "messenger_orders/m-orders_update.html"
    messenger_orders = get_object_or_404(Category, pk=pk)
    form = MessengerOrdersForm(request.POST or None, instance=messenger_orders)
    if form.is_valid():
         form.save()
         return redirect("m-orders-list")
    context = {
        "form" : form
    }
    return render (request, template_name, context)

@login_required
def messenger_delete(request, pk):
    messenger_orders = MessengerOrders.objects.filter(id=pk).update(status=False)
    return redirect("m-orders-list")