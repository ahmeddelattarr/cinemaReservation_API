from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED

from .models import Movie,Guest,Reservation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GuestSerializer,MovieSerializer,ReservationSerializer

# Create your views here.
@api_view(['GET','POST'])

def FBV_List(request):
    if request.method=='GET':
        guests=Guest.objects.all()
        serializer=GuestSerializer(guests,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view()
#post-put-get
#todo def FBV_List(request):




