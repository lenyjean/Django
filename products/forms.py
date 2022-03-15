from django import forms
from .models import *

class CategoryForms(forms.ModelForm):
    class Meta: 
        model = Category
        fields = "__all__"

class ProductForms(forms.ModelForm):
    class Meta: 
        model = Products
        fields = "__all__"