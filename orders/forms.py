from django import forms
from .models import *
import datetime
from django.utils import timezone
import pytz

utc=pytz.UTC
now = timezone.now()

class DateInput(forms.DateInput):
    input_type = 'date'

class OrderForms(forms.ModelForm):
    class Meta: 
        model = Orders
        fields = [
            "customer_name", "customer_address" , "products", "no_of_order", "total_amount", "pickup_date", "status"
        ]
        widgets = {
            "pickup_date" : DateInput()
        }

        def clean(self):
            cleaned_data = super().clean()
            pickup_date = cleaned_data.get("pickup_date")

            if pickup_date < datetime.date.today():
                raise forms.ValidationError("Pick-up Date should not be later than date today")