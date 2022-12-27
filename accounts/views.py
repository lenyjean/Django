from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import logout

import shortuuid
import datetime
from .models import *
from .forms import *
from .utils import send_email, encrypt_data, decrypt_data


# Create your views here.

@login_required(login_url='/accounts/login')
def accounts(request):
    template_name = "user_accounts/accounts.html"
    accounts = User.objects.all()
    active_user = User.objects.filter(status=True)
    inactive_user = User.objects.filter(status=False)
    context = {
        "active_user": active_user,
        "inactive_user": inactive_user,
        "accounts": accounts,
        "accounts_state": "background-color: #dbeafe;"
    }
    return render(request, template_name, context)


@login_required(login_url='/accounts/login')
def viewprofile(request):
    template_name = "profile/profile.html"
    return render(request, template_name)


@login_required(login_url='/accounts/login')
def user_update(request, pk):
    template_name = "user_accounts/update_account.html"
    user = get_object_or_404(User, pk=pk)
    form = AdminSignUpForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect("account-list")
    context = {
        "form": form
    }
    return render(request, template_name, context)


@login_required(login_url='/accounts/login')
def profile_update(request, pk):
    template_name = "user_accounts/update_account.html"
    user = get_object_or_404(User, pk=pk)
    form = UpdateForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect("view-profile")
    context = {
        "form": form
    }
    return render(request, template_name, context)


@login_required(login_url='/accounts/login')
def user_delete(request, pk):
    user = User.objects.filter(id=pk).update(status=False)
    return redirect("account-list")


@login_required(login_url='/accounts/login')
def user_reactivate(request, pk):
    user = User.objects.filter(id=pk).update(status=True)
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


@login_required(login_url='/accounts/login')
def update_password(request):
    template_name = "user_accounts/update_password.html"
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


class UserDetailView(DetailView):
    # specify the model to use
    template_name = 'user_accounts/delete_profile.html'
    model = User
    context_object_name = "user"


class UserReactivateView(DetailView):
    template_name = 'user_accounts/reactivate_profile.html'
    model = User
    context_object_name = "user"


def login_page(request):
    template_name = "registration/login.html"
    form = SignInForm(request.POST or None)

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            check_email = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if check_email.status:
                if user is not None:
                    login(request, user)
                    return redirect("/")
                else:
                    messages.error(request, "Invalid username or password")
            else:
                messages.error(request, "Account deactivated. Contact administrator to activate it")
        except User.DoesNotExist:
            messages.error(request, "User doesn't exists. Please contact the administrator for creating new account.")
    context = {
        "form": form
    }
    return render(request, template_name, context)


def logout_page(request):
    logout(request)
    return redirect("login")


def send_password_reset_link(request):
    template_name = "registration/result.html"
    if request.method == "POST":
        email = request.POST.get("email")

        try:
            user = User.objects.get(email=email)
            encrypt_token = encrypt_data(user.username + "|" + shortuuid.ShortUUID().random(length=100) + "|" + user.email)
            print("ENCRYPTED", encrypt_token)
            print("DECRYPTED", decrypt_data(encrypt_token))
            link = "http://localhost:8000/accounts/reset-password/" + encrypt_token
            send_email(email, link)
            PasswordResetRequest.objects.create(
                token=encrypt_token
            )
            return render(request, template_name, {"success": True, "reset": True})
        except User.DoesNotExist:
            return render(request, template_name, {"success": False, "reset": True})


def reset_password_link(request, token):
    template_name = "registration/reset_password.html"

    check_token = PasswordResetRequest.objects.filter(
        token=token, created_on__gt=datetime.datetime.now()-datetime.timedelta(minutes=10)
    )
    if check_token.exists():
        for i in check_token:
            if not i.is_expired:
                decrypted_token = decrypt_data(token)
                user_data = decrypted_token.split("|")
                user = User.objects.get(email=user_data[2])
                if request.method == "POST":
                    new_password = request.POST.get("new_password")
                    confirm_password = request.POST.get("confirm_password")

                    if new_password == confirm_password:
                        user.set_password(new_password)
                        PasswordResetRequest.objects.filter(token=token).update(is_expired=True)
                        messages.success(request, "Password changed successfully")
                        return redirect("/accounts/login")
                    else:
                        messages.error(request, "New and confirm password doesn't match")
                        return render(request, template_name)
            else:
                messages.error(request, "Password reset link already expired")
                return redirect("/accounts/login")
    else:
        messages.error(request, "Password reset link already expired")
        return redirect("/accounts/login")
    return render(request, template_name)

