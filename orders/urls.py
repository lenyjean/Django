from django.urls import path

from .views import *

urlpatterns = [
    path("orders-list", orders_list, name="orders-list"),
    path("orders-add", orders_add, name="orders-add"),
    path("orders-view/<int:pk>", orders_view, name="orders-view"),
    path("orders-update/<int:pk>", orders_update, name="orders-update"),
    path("orders-delete/<int:pk>", orders_delete, name="orders-delete")
]
