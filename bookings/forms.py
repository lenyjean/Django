from django import forms
from .models import *

class BookingsForms(forms.ModelForm):
    bookings = forms.ModelChoiceField(queryset=Bookings.objects.filter(status=True))
    class Meta: 
        model = Bookings
        fields = [
            "customer_name", "cake_name" , "category", "quantity", "total_amount", "pickup_date", "name_on_cake", "phone", "status"
        ]