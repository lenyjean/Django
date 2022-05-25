from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from .models import *
from .forms import *
# Create your views here.
def accounts(request):
    template_name = "user_accounts/accounts.html"
    accounts = User.objects.all()
    active_user = User.objects.filter(status=True)
    inactive_user = User.objects.filter(status=False)
    context = {
        "active_user": active_user,
        "inactive_user" : inactive_user,
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
     user = User.objects.filter(id=pk).update(status=False)
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


def update_password(request):
    template_name =  "user_accounts/update_password.html"
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('view-profile')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('update_password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, template_name, {
        'form': form
    })
