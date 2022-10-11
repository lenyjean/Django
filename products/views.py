from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.forms import *

from .models import *

# Create your views here.
@login_required(login_url='/accounts/login')
def products(request):
    template_name = "products/products_list.html"
    available_products = Products.objects.filter(status=True)
    not_available_products = Products.objects.filter(status=False)
    context = {
        "available_products": available_products,
        "not_available_products" : not_available_products
    }
    return render (request, template_name, context)

@login_required(login_url='/accounts/login')
def products_add(request):
    template_name = "products/products_add.html"
    form = ProductForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("products-list")
    context = {
       "form" :  form
    }
    return render (request, template_name, context)

@login_required(login_url='/accounts/login')
def products_view(request, pk):
     template_name = "products/products_view.html"
     products = Products.objects.filter(id=pk)
     context = {
         "products" : products
     }
     return render (request, template_name, context)

@login_required(login_url='/accounts/login')
def products_update(request, pk):
    template_name = "products/products_update.html"
    products = get_object_or_404(Products, pk=pk)
    form = ProductForms(request.POST or None, instance=products)
    if form.is_valid():
         form.save()
         return redirect("products-list")
    context = {
        "form" : form
    }
    return render (request, template_name, context)
    
@login_required(login_url='/accounts/login')
def products_delete(request, pk):
    products = Products.objects.filter(id=pk).update(status=False)
    return redirect("products-list")
