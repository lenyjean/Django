from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from .serializers import *

from bookings.models import *


class Webhooks(viewsets.ViewSet):

    def list(self, request):
        ''' Connect webhooks to api '''
        mode = self.request.query_params.get('hub.mode')
        verify_token = self.request.query_params.get('hub.verify_token')
        challenge = self.request.query_params.get('hub.challenge')

        if mode == "subscribe" and verify_token == "bW9uZXR0ZXNjYWtlc2hvcG1vbmV0dGVzY2FrZXNob3Btb25ldHRlc2Nha2VzaG9w":
            return HttpResponse(challenge)
        return HttpResponse(challenge)

    def create(self, request):
        if request.method == "POST":
            serializers = Webhooks(data=request.data)
            print(serializers.data)
            messenger_id = serializers.data['entry'][0]['messaging'][0]["sender"]["id"]
            message = serializers.data['entry'][0]['messaging'][0]["message"]["text"]
            check_data = Bookings.objects.filter(messenger_id=messenger_id)

            restrict_msg = [
                "Please enter your full name",
                "Nice meeting you! How can we help you for today?",
                "Please enter your full name (Last name, First Name, M.I)"
            ]

            if not check_data and message not in restrict_msg:
                Bookings.objects.create(
                    messenger_id=serializers.data['entry'][0]['messaging'][0]["sender"]["id"]
                )
            else:
                if message not in restrict_msg:
                    Bookings.objects.filter(messenger_id=messenger_id).update(
                        customer_name=serializers.data['entry'][0]['messaging'][0]["message"]["text"]
                    )
            print(serializers.data['entry'][0]
                  ['messaging'][0]["message"]["text"])
            return Response(serializers.data, status=status.HTTP_201_CREATED)
