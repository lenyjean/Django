from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from orders.models import *
from django.db.models import Q

from .forms import *
from datetime import datetime

# Create your views here.
@login_required(login_url='/accounts/login')
def orders_list(request):
    template_name = "orders/orders_list.html"
  # A filter for the date range.
    if 'from_date' in request.GET or  'to_date' in request.GET:
        from_date = request.GET['from_date']
        to_date = request.GET['to_date']
        multiple_q = Q(Q(date_ordered__range=[datetime.strptime(from_date, '%Y-%m-%d').date(), datetime.strptime(to_date, '%Y-%m-%d').date()]) & Q(status="Pending") | Q(status="Late"))
        active_orders = Orders.objects.filter(multiple_q)
        inactive_orders = Orders.objects.filter(status="Done")
        filtered = True
        filter_info = f"{from_date} to {to_date}"
        inactive = "No"


    elif 'from_date_history' in request.GET or  'to_date_history' in request.GET:
        from_date_history = request.GET['from_date_history']
        to_date_history = request.GET['to_date_history']
        multiple_q_history = Q(Q(date_ordered__range=[datetime.strptime(from_date_history, '%Y-%m-%d').date(), datetime.strptime(to_date_history, '%Y-%m-%d').date()]) & Q(status="Done") | Q(status="Cancelled") | Q(status="Late"))
        inactive_orders = Orders.objects.filter(multiple_q_history)
        active_orders = Orders.objects.filter(status="Pending")
        filtered = True
        filter_info = f"{from_date_history} to {to_date_history}"
        inactive = "Yes"
    else:
        active_orders = Orders.objects.filter(status__in=["Pending", "Late"])
        inactive_orders = Orders.objects.filter(status__in=["Done","Cancelled"])
        filtered = False
        filter_info = None
        inactive = None

    print(inactive)
    context = {
        "active_orders": active_orders,
        "inactive_orders" : inactive_orders,
        "filtered" : filtered,
        "filter_info" : filter_info,
        "inactive" : inactive
    }
    return render(request, template_name, context)


@login_required(login_url='/accounts/login')
def orders_add(request):
    template_name = "orders/orders_add.html"
    form = OrderForms(request.POST or None)
    if form.is_valid():
        get_price = Products.objects.get(product_name=form.cleaned_data['product'])
        customer_name = form.cleaned_data['customer_name']
        customer_address = form.cleaned_data['customer_address']
        products = form.cleaned_data['product']
        no_of_order = form.cleaned_data['no_of_order']
        total_amount = get_price.price  *  form.cleaned_data['no_of_order']
        pickup_date = form.cleaned_data['pickup_date']
        processed_by = request.user.username
        status = form.cleaned_data['status']
        
        orders = Orders.objects.get_or_create(
            customer_name=customer_name, customer_address=customer_address, product=products,
            no_of_order=no_of_order, total_amount=total_amount, pickup_date=pickup_date, processed_by=processed_by, status=status
        )

        return redirect("orders-list")
    context = {
        "form":  form
    }
    return render(request, template_name, context)


@login_required(login_url='/accounts/login')
def orders_view(request, pk):
    template_name = "orders/orders_view.html"
    orders = Orders.objects.filter(id=pk)
    context = {
        "orders": orders
    }
    return render(request, template_name, context)


@login_required(login_url='/accounts/login')
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

@login_required(login_url='/accounts/login')
def orders_delete(request, pk):
    orders = Orders.objects.filter(id=pk).update(status="Done")
    return redirect("orders-list")

@login_required(login_url='/accounts/login')
def messenger_list(request):
    template_name = "messenger_orders/m-orders_list.html"
    messenger_orders = MessengerOrders.objects.all()
    context = {
        "messenger_orders":  messenger_orders
    }
    return render(request, template_name, context)

@login_required(login_url='/accounts/login')
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

@login_required(login_url='/accounts/login')
def messenger_view(request, pk):
    template_name = "messenger_orders/m-orders_view.html"
    messenger_orders = MessengerOrders.objects.filter(id=pk)
    context = {
        "messenger_orders": messenger_orders
    }
    return render(request, template_name, context)

@login_required(login_url='/accounts/login')
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
    
@login_required(login_url='/accounts/login')
def messenger_delete(request, pk):
    messenger_orders = MessengerOrders.objects.filter(id=pk).update(status=False)
    return redirect("m-orders-list")