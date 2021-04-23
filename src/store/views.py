from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


from src.category.models import Category
from .models import Product


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug
        )
    except Exception as e:
        raise e

    ctx = {
        "single_product": single_product,
    }
    return render(request, "store/product_detail.html", ctx)


def store(request, category_slug=None):
    # search by categories
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 10)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by("id")
        paginator = Paginator(products, 10)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
        product_count = products.count()

    ctx = {
        "products": paged_products,
        "product_count": product_count,
    }
    # end search by categories
    return render(request, "store/store.html", ctx)
