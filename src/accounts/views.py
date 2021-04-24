from django.shortcuts import render, redirect
from django.contrib import messages


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
            messages.success(request, 'Registration suceesful')
            return redirect('accounts:register')
            # Create a user profile
    else:
        form = RegistrationForm()

    ctx = {
        "form": form,
    }

    return render(request, "accounts/register.html", ctx)


def login(request):

    return render(request, "accounts/login.html")


def logout(request):
    auth.logout(request)
    messages.success(request, "You are logged out.")
    return redirect("login")
