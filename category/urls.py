from django.urls import path

from .views import *

urlpatterns = [
    path("category-list", category, name="category-list"),
    path("category-add", category_add, name="category-add"),
    path("category-view/<int:pk>", category_view, name="category-view"),
    path("category-update/<int:pk>", category_update, name="category-update"),
    path("category-delete/<int:pk>", category_delete, name="category-delete"),
]