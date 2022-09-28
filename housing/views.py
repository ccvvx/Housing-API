from turtle import home
from django.http import JsonResponse

import housing
from .models import Home
from .serializers import HomeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from housing import serializers




# Get all homes
# serialize them
# return Json

@api_view(['GET', 'POST'])
def housing_list(request):

    if request.method == 'GET':
        housing = Home.objects.all()
        serializer = HomeSerializer(housing, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = HomeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def housing_detail(request, id):

    try:
        home = Home.objects.get(pk=id) 
    except Home.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HomeSerializer(home)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HomeSerializer(home, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        home.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
