from django.db import models
from django.forms import CharField

from products.models import *

# Create your models here.
class Orders(models.Model):
    status = (
        ("Pending" , "Pending"),
        ("Done" , "Done"),
        ("Cancelled" , "Cancelled"),
        ("Late" , "Late")
    )
    customer_name = models.CharField(max_length=255)
    customer_address = models.CharField(max_length=255)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    no_of_order = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateField(auto_now_add=True)
    pickup_date = models.DateField(auto_now_add=False)
    processed_by = models.CharField(max_length=255)
    notes = models.TextField()
    status = models.CharField(max_length=255, choices=status)

    class Meta:
        verbose_name = "Orders"

    def __str__(self):
        return f"Customer Name: {self.customer_name}"
