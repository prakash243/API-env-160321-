from django.shortcuts import render, redirect
from movies_ratingapp.models import *
from movies_ratingapp.serializers import *

from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

# Create your views here.

class Student_APIView(APIView):

    def get(self, request, pk=None, format=None):
        stu_id = pk
        if stu_id is not None:
            stu = Student.objects.get(id=stu_id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all().order_by('-id')
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None, format=None):
        stu_id = pk
        if stu_id is not None:
            stu = Student.objects.get(id=stu_id)
            serializer = StudentSerializer(stu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)


    def patch(self, request, pk=None, format=None):
        stu_id = pk
        if stu_id is not None:
            stu = Student.objects.get(id=stu_id)
            serializer = StudentSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk=None, format=None):
        stu_id = pk
        stu = Student.objects.get(id=stu_id)
        stu.delete()
        return Response({'msg':'{} is deleted successfully'.format(stu.name)})
