from django.shortcuts import render, redirect

from movies_ratingapp.models import *
from movies_ratingapp.serializers import *

# common import for Response in DRF
from rest_framework.response import Response
from rest_framework import status

# api_view  Create api with using DRF
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api_view(request, pk=None):
    stu_id = pk
    if request.method == "GET":
        if stu_id is not None:
            stu = Student.objects.get(id=stu_id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  

    if request.method== 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT":
        stu_id = pk
        stu = Student.objects.get(id=stu_id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


    if request.method == "PATCH":
        stu_id = pk
        stu = Student.objects.get(id=stu_id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        stu_id = pk
        if stu_id:
            stu = Student.objects.get(id=stu_id)
            stu.delete()
            return Response({'msg': '{} is deleted successfully'.format(stu.name)})
        return Response({'msg': 'details not found'})