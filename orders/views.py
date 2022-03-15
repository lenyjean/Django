from django.shortcuts import render, redirect, get_object_or_404

from orders.models import *

from .forms import *

# Create your views here.
def orders_list(request):
    template_name = "orders/orders_list.html"
    orders = Orders.objects.all()
    context = {
        "orders" : orders
    }
    return render (request, template_name, context)

def orders_add(request):
    template_name = "orders/orders_add.html"
    form = OrderForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("orders-list")
    context = {
       "form" :  form
    }
    return render (request, template_name, context)


def orders_view(request, pk):
     template_name = "orders/orders_view.html"
     orders = Orders.objects.filter(id=pk)
     context = {
         "orders" : orders
     }
     return render (request, template_name, context)

def orders_update(request, pk):
    template_name = "orders/orders_update.html"
    orders = get_object_or_404(Orders, pk=pk)
    form = OrderForms(request.POST or None, instance=orders)
    if form.is_valid():
        form.save()
        return redirect("orders-list")
    context = {
       "form" :  form
    }
    return render (request, template_name, context)

def orders_delete(request, pk):
     orders = Orders.objects.filter(id=pk)
     orders.delete()
     return redirect("orders-list")