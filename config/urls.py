"""Main URLs module."""

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin


# import ipdb; ipdb.set_trace()

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path("", include(("src.home.urls", "home"), namespace="home")),
    path("store/", include(("src.store.urls", "store"), namespace="store")),
    path("cart/", include(("src.carts.urls", "cart"), namespace="cart")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
