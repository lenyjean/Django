from django import forms
from .models import *

class ProductForms(forms.ModelForm):
    class Meta: 
        model = Products
        fields = "__all__"