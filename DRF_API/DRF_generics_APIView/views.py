from django.shortcuts import render

from  movies_ratingapp.models import *
from  movies_ratingapp.serializers import *

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.

class LC_Student_APIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RUD_Student_APIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

