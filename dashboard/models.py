from django.db import models

# Create your models here.
class Products(models.Model):
    label = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.label} | {self.category} | {self.quantity} | {self.price}"
