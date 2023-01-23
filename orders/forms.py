from django import forms
from .models import *
import datetime
from products.models import *

 
class DateInput(forms.DateInput):
    input_type = 'date'
 
class OrderForms(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Products.objects.filter(status="Available"))
    class Meta: 
        model = Orders
        fields = [
            "customer_name", "customer_address" , "product", "no_of_order", "pickup_date", "contact_number", "status"
        ]
        widgets = {
            "pickup_date" : DateInput()
        }
 
    def clean(self):
        cleaned_data = super().clean()
        pickup = cleaned_data.get("pickup_date")
 
        if pickup < datetime.date.today():
            raise forms.ValidationError('Pick up date must not be later than today')


class MessengerOrdersForm(forms.ModelForm):
    class meta: 
        model = MessengerOrders
        fields = [
             "customer_name", "customer_address" , "product", "no_of_order", "total_amount", "pickup_date", "status", "remarks"
        ]