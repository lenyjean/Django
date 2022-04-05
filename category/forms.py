from django import forms
from products.models import *

class CategoryForms(forms.ModelForm):
    class Meta: 
        model = Category
        fields = "__all__"