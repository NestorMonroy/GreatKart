from django.urls import path

from . import views

urlpatterns = [
    path("", views.store, name="home"),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),

]