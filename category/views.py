from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from products.models import *
from .forms import *
# Create your views here.
@login_required(login_url='/accounts/login')
def category(request):
    template_name = "category/category_list.html"
    active_category = Category.objects.filter(status=True)
    inactive_category = Category.objects.filter(status=False)
    context = {
        "active_category": active_category,
        "inactive_category" : inactive_category
    }
    return render (request, template_name, context)

@login_required(login_url='/accounts/login')
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

@login_required(login_url='/accounts/login')
def category_view(request, pk):
     template_name = "category/category_view.html"
     category = Category.objects.filter(id=pk)
     context = {
         "category" : category
     }
     return render (request, template_name, context)

@login_required(login_url='/accounts/login')
def category_update(request, pk):
    template_name = "category/category_update.html"
    category = get_object_or_404(Category, id=pk)
    form = CategoryForms(request.POST or None, instance=category)
    if form.is_valid():
         form.save()
         return redirect("category-list")
    context = {
        "form" : form
    }
    return render (request, template_name, context)

@login_required(login_url='/accounts/login')
def category_delete(request, pk):
    category = Category.objects.filter(id=pk).update(status=False)
    return redirect("category-list")