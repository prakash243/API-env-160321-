from django.shortcuts import render, redirect
from movies_ratingapp.models import  *
from movies_ratingapp.serializers import  *

from rest_framework import viewsets
# Create your views here.

class Student_viewsets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer