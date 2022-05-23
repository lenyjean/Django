from rest_framework import serializers

from inquiries.models import *


class InquriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiries
        fields ="__all__"
