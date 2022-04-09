from django import forms
from .models import *

class ProductForms(forms.ModelForm):
    class Meta: 
        model = Products
        fields = ["product_name", "category", "price", "size"]
