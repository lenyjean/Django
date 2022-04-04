from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from .models import *
from .forms import *
# Create your views here.
# def accounts(request):
#     template_name = "user_accounts/accounts.html"
#     accounts = Accounts.objects.all()
#     context = {}
#     return render (request. template_name, context)

class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('accounts-list')



class StaffSignUpView(CreateView):
    model = User
    form_class = StaffSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'staff'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('accounts-list')