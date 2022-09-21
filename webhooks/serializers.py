from rest_framework import serializers

from inquiries.models import *
from bookings.models import *


# class InquriesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Inquiries
#         fields ="__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields ="__all__"
