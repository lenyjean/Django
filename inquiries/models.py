from django.db import models

# Create your models here.
class Inquiries(models.Model):
    customer_name = models.CharField(max_length=225)
    flavor = models.CharField(max_length=225)
    custom_decoration = models.CharField(max_length=225)
    describe_decoration = models.CharField(max_length=225)
    delivery_date = models.CharField(max_length=225)
    name_on_cake = models.CharField(max_length=225)
    created_date = models.DateField(auto_now_add=True)
    

    class Meta:
        verbose_name = "Inquiries"

    def __str__(self):
        return f"Customer Name: {self.customer_name}"
