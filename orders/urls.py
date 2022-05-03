from django.urls import path

from .views import *

urlpatterns = [
    path("orders-list", orders_list, name="orders-list"),
    path("orders-add", orders_add, name="orders-add"),
    path("orders-view/<int:pk>", orders_view, name="orders-view"),
    path("orders-update/<int:pk>", orders_update, name="orders-update"),
    path("orders-delete/<int:pk>", orders_delete, name="orders-delete"),
    path("m-orders-list", messenger_list, name="m-orders-list"),
    path("m-orders-add", messenger_add, name="m-orders-add"),
    path("m-orders-view/<int:pk>", messenger_view, name="m-orders-view"),
    path("m-orders-update/<int:pk>", messenger_update, name="m-orders-update"),
    path("m-orders-delete/<int:pk>", messenger_delete, name="m-orders-delete"),
]
