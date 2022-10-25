from django import forms
from .models import *

class BookingsForms(forms.ModelForm):
    customer_name = forms.CharField(disabled=True)
    cake_name = forms.CharField(disabled=True)
    cake_size = forms.CharField(disabled=True)
    category = forms.CharField(disabled=True)
    quantity = forms.CharField(disabled=True)
    total_amount = forms.CharField(disabled=True)
    mode_of_payment = forms.CharField(disabled=True)
    pickup_date = forms.CharField(disabled=True)
    phone = forms.CharField(disabled=True)
    class Meta: 
        model = Bookings
        fields = [
            "customer_name", "cake_name" , "cake_size", "category", "quantity", "total_amount", "mode_of_payment", "pickup_date","phone", "status"
        ]
        

        