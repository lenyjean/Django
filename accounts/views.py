from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from .models import *
from .forms import *
# Create your views here.
def accounts(request):
    template_name = "user_accounts/accounts.html"
    accounts = User.objects.all()
    context = {
        "accounts" : accounts
        }
    return render (request, template_name, context)

def viewprofile(request):
    template_name = "profile/profile.html"
    return render (request, template_name)


def user_update(request, pk):
    template_name = "user_accounts/update_account.html"
    user = get_object_or_404(User, pk=pk)
    form = AdminSignUpForm(request.POST or None, instance=user)
    if form.is_valid():
         form.save()
         return redirect("account-list")
    context = {
        "form" : form
    }
    return render (request, template_name, context)

def profile_update(request, pk):
    template_name = "user_accounts/update_account.html"
    user = get_object_or_404(User, pk=pk)
    form = UpdateForm(request.POST or None, instance=user)
    if form.is_valid():
         form.save()
         return redirect("view-profile")
    context = {
        "form" : form
    }
    return render (request, template_name, context)
    
def user_delete(request, pk):
     user = User.objects.filter(id=pk)
     user.delete()
     return redirect("account-list")

class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('account-list')

class StaffSignUpView(CreateView):
    model = User
    form_class = StaffSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'staff'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('account-list')

