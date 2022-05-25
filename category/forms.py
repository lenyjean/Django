from django import forms
from products.models import *

class CategoryForms(forms.ModelForm):
    class Meta: 
        model = Category
        fields = ["category"]

    class Meta:
        verbose_name = "Category"

    def __str__(self):
        return f"Category: {self.category}"

