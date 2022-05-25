from django import forms
from products.models import *

class CategoryForms(forms.ModelForm):
    status = forms.BooleanField(label="Activate this category?", required=False)
    class Meta: 
        model = Category
        fields = ["category", "status"]



