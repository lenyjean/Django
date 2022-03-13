from django.shortcuts import render, redirect, get_object_or_404

from .models import *

from .forms import *
# Create your views here.
def homepage(request):
    template_name = "dashboard/homepage.html"
    products = Products.objects.all().count()
    
    context = {
        "products": products
    }
    return render(request, template_name, context)

def create_product(request):
    template_name = "dashboard/create_product.html"
    form = ProductForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("homepage")
    context = {
        "form": form
    }
    return render(request, template_name, context)

def view_product(request, pk):
    template_name = "dashboard/view_product.html"
    product = Products.objects.filter(id=pk)
    context = {
        "product": product
    }
    return render(request, template_name, context)

def update_product(request, pk):
    template_name = "dashboard/update_product.html"
    product = get_object_or_404(Products, pk=pk)
    form = ProductForms(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect("homepage")

    context = {
        "form": form
    }
    return render(request, template_name, context)

def delete_product(request, pk):
    product = Products.objects.filter(id=pk)
    product.delete()
    return redirect("homepage")