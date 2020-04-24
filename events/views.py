from django.shortcuts import render
from django.views.generic import ListView
from .models import Event
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# from userAccount import Account as user
# Create your views here.

@api_view(['GET', 'POST'])
def show_events(request):
    # request_instance = Event.objects.create()
    if request.method == 'GET':
        data = Event.objects.all()

        serializer = EventSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def event_info(request,pk):
    if request.method == 'GET':
        data = Event.objects.get(pk=pk)

        serializer = EventSerializer(data, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def events_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = EventSerializer(event, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
