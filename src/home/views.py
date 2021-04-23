from django.shortcuts import render


def home(request):
    path = "home.html"

    ctx = {}

    return render(request, path, ctx)