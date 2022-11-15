from django.urls import path

from .views import *

urlpatterns = [
    path("products-list", products, name="products-list"),
    path("products-add", products_add, name="products-add"),
    path("products-view/<int:pk>", products_view, name="products-view"),
    path("products-update/<int:pk>", products_update, name="products-update"),
    path("products-delete/<int:pk>", products_delete, name="products-delete"),
]