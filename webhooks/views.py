from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from ninja import NinjaAPI


from .serializers import *
from .models import *
from bookings.models import *
from .schema import *

api = NinjaAPI(csrf=True)
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
            print(request.data)

            # if request.data['type'] == "custom_yes":
            #     MessengerData.objects.create(data=request.data)
            #     # serializers = InquriesSerializer(data=request.data)
                
            #     if serializers.is_valid():
            #         serializers.save()
            #         return Response(serializers.data, status=status.HTTP_201_CREATED)
            #     else:
            #         return Response(serializers.errors, status=status.HTTP_201_CREATED)

            # if request.data["type"] == "custom_no":
            #     MessengerData.objects.create(data=request.data)
            #     return Response(request.data, status=status.HTTP_201_CREATED)

            # elif request.data["type"] == "bookings_custom_yes":
            #     MessengerData.objects.create(data=request.data)
            #     return Response(request.data, status=status.HTTP_201_CREATED)

            # elif request.data["type"] == "bookings_custom_no":
            #     MessengerData.objects.create(data=request.data)
            #     serializers = BookingSerializer(data=request.data)
                
            #     if serializers.is_valid():
            #         serializers.save()
            #         return Response(serializers.data, status=status.HTTP_201_CREATED)
            #     else:
            #         print(serializers.errors)
            #         return Response(serializers.errors, status=status.HTTP_201_CREATED)
            MessengerData.objects.create(data=request.data)
            return Response(request.data, status=status.HTTP_201_CREATED)


@api.post("/api/create-bookings", response=BookingOutputSchema)
@csrf_exempt
def create_bookings_from_chatbot(request, payload: BookingInputSchema):
    # bookings = Bookings.objects.create(
    #     customer_name = payload.customer_name,
    #     category = payload.category,
    #     cake_name = payload.cake_name,
    #     cake_size = payload.cake_size,
    #     quantity = float(payload.quantity),
    #     pickup_date = payload.pickup_date,
    #     phone = payload.phone,
    #     total_amount = payload.total_amount,
    #     mode_of_payment = payload.mode_of_payment,
    # )
    return payload
