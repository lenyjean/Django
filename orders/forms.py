from django import forms
from .models import *

class OrderForms(forms.ModelForm):
    class Meta: 
        model = Orders
        fields = "__all__"

