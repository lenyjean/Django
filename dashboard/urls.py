from django.urls import path

from .views import *

urlpatterns = [
    path("", homepage, name="homepage"),
    path("create-product", create_product, name="create-product"),
    path("view-product/<int:pk>", view_product, name="view-product"),
    path("update-product/<int:pk>", update_product, name="update-product"),
    path("delete-product/<int:pk>", delete_product, name="delete-product"),
]