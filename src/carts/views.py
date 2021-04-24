from django.shortcuts import render


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
    except ObjectDoesNotExist:
        pass  # just ignore

    ctx = {}
    return render(request, "store/cart.html", ctx)
