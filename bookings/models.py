from django.db import models

# Create your models here.
class Bookings(models.Model):
    status = (
        ("Pending" , "Pending"),
        ("Done" , "Done"),
        ("Cancelled" , "Cancelled"),
        ("Late" , "Late"),
    )
    customer_name = models.CharField(max_length=225)
    cake_name = models.CharField(max_length=225)
    category = models.CharField(max_length=225)
    cake_size = models.CharField(max_length=225)
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pickup_date = models.CharField(max_length=225)
    name_on_cake = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)
    status = models.CharField(max_length=225, choices=status)
    created_date = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name = "Bookings"

