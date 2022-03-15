from django.db import models


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Category"

    def __str__(self):
        return self.category

class Products(models.Model):
    status = (
        ("Available", "Available"),
        ("Not Available", "Not Available")
    )
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255, choices=status)

    class Meta:
        verbose_name = "Products"

    def __str__(self):
        return self.product_name