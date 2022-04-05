from django.db import models

# Create your models here.
class Bookings(models.Model):
    messenger_id  = models.IntegerField()
    customer_name = models.CharField(max_length=225)
    product_ordered = models.CharField(max_length=225)
    category = models.CharField(max_length=225)
    pickup_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=225)
    created_date = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name = "Bookings"

    def __str__(self):
        return f"Customer Name: {self.customer_name} | Product Ordered: {self.product_ordered}"
