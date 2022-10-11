from django import forms
from .models import *

class BookingsForms(forms.ModelForm):
    class Meta: 
        model = Bookings
        fields = [
            "customer_name", "cake_name" , "cake_size", "category", "quantity", "total_amount", "mode_of_payment", "pickup_date","phone", "status"
        ]

        