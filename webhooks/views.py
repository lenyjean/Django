from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from .serializers import *


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
            return Response(serializers.data, status=status.HTTP_201_CREATED)
