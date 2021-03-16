from django.shortcuts import render, redirect

from  movies_ratingapp.models import *
from  movies_ratingapp.serializers import *

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin , DestroyModelMixin
# Create your views here.

class LC_Student_mixins(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class  RUD_Student_mixins(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk , *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, pk,  *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, pk,  *args, **kwargs):
        return self.destroy(request, *args, **kwargs)