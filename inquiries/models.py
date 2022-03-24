from django.db import models

# Create your models here.
class Inquiries(models.Model):
    customer_name = models.CharField(max_length=225)
    product_ordered = models.CharField(max_length=225)
    category = models.CharField(max_length=225)
    pickup_date = models.DateField(auto_now_add=False)
    status = models.CharField(max_length=225)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Inquiries"

    def __str__(self):
        return f"Customer Name: {self.customer_name}"
