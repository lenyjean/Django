from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.forms import *

from .models import *

# Create your views here.
@login_required
def category(request):
   template_name = "category/category_list.html"
   category = Category.objects.all()
   context = {
       "category" : category
   }
   return render (request, template_name, context)

@login_required
def category_add(request):
    template_name = "category/category_add.html"
    form = CategoryForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("category-list")
    context = {
       "form" :  form
    }
    return render (request, template_name, context)

@login_required
def category_view(request, pk):
     template_name = "category/category_view.html"
     category = Category.objects.filter(id=pk)
     context = {
         "category" : category
     }
     return render (request, template_name, context)

@login_required
def category_update(request, pk):
    template_name = "category/category_update.html"
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForms(request.POST or None, instance=category)
    if form.is_valid():
         form.save()
         return redirect("category-list")
    context = {
        "form" : form
    }
    return render (request, template_name, context)

@login_required
def category_delete(request, pk):
     category = Category.objects.filter(id=pk)
     category.delete()
     return redirect("category-list")

@login_required
def products(request):
   template_name = "products/products_list.html"
   products = Products.objects.all()[:5]
   context = {
       "products" : products
   }
   return render (request, template_name, context)

@login_required
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

@login_required
def products_view(request, pk):
     template_name = "products/products_view.html"
     products = Products.objects.filter(id=pk)
     context = {
         "products" : products
     }
     return render (request, template_name, context)

@login_required
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
    
@login_required
def products_delete(request, pk):
     products = Products.objects.filter(id=pk)
     products.delete()
     return redirect("products-list")
