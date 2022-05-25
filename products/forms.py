from django import forms
from .models import *

class ProductForms(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(status=True))
    class Meta: 
        model = Products
        fields = ["product_name", "category", "price", "size"]

       
   
