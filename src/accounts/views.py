from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from .models import Account
from .forms import RegistrationForm


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            username = email.split("@")[0]
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            user.phone_number = phone_number
            user.save()
            messages.success(request, "Registration suceesful")
            return redirect("accounts:register")
            # Create a user profile
    else:
        form = RegistrationForm()

    ctx = {
        "form": form,
    }

    return render(request, "accounts/register.html", ctx)


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect("home:home")
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect("accounts:login")

    return render(request, "accounts/login.html")


@login_required(login_url="accounts:login")
def logout(request):
    auth.logout(request)
    messages.success(request, "You are logged out.")
    return redirect("accounts:login")
