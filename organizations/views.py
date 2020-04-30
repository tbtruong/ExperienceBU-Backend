from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Club
# Create your views here.

@api_view(['GET', 'POST'])
def show_clubs(request):
    # request_instance = Event.objects.create()
    if request.method == 'GET':
        data = Club.objects.all()

        serializer = ClubSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClubSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def club_info(request,pk):
    if request.method == 'GET':
        data = Club.objects.get(pk=pk)

        serializer = ClubSerializer(data, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClubSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT', 'DELETE'])
def clubs_detail(request, pk):
    try:
        event = Club.objects.get(pk=pk)
    except Club.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ClubSerializer(event, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)