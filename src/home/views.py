from django.shortcuts import render
from src.store.models import Product


def home(request):
    path = "home.html"
    products = Product.objects.all().filter(is_available=True)

    ctx = {"products": products}

    return render(request, path, ctx)