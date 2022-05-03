from django import forms
from .models import *
import datetime
from products.models import *

 
class DateInput(forms.DateInput):
    input_type = 'date'
 
class OrderForms(forms.ModelForm):
    products = forms.ModelChoiceField(queryset=Products.objects.filter(status=True))
    class Meta: 
        model = Orders
        fields = [
            "customer_name", "customer_address" , "products", "no_of_order", "pickup_date", "status"
        ]
        widgets = {
            "pickup_date" : DateInput()
        }
 
    def clean(self):
        cleaned_data = super().clean()
        pickup = cleaned_data.get("pickup_date")
 
        if pickup < datetime.date.today():
            raise forms.ValidationError('Pick up date must not be later than today')