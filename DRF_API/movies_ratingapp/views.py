from django.shortcuts import render, redirect
from .models import *
from .serializers import *
import requests

#Create api without using DRF
from django.http import HttpResponse, JsonResponse

# common import for Response in DRF
from rest_framework.response import Response
from rest_framework import status


# viewsets(ModelViewSet)  Create api with using DRF (Using Viewsets (Class Based Views))
from rest_framework import viewsets

# APIView  Create api with using DRF (Using views (Class Based Views)) 
from rest_framework.views import APIView

# GenericAPIView (mixins) from DRF
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView

# for Django REST Api Authentication
from rest_framework.authentication import BasicAuthentication

# for Django REST Api Permissions after authenticated
from rest_framework.permissions import IsAuthenticated




def home(request):
    url = "http://127.0.0.1:8000/students/"
    res = requests.get(url)
    students = res.json()
    print(students)
    return render(request, 'home.html', {'students': students})

def add(request):
    if request.method == 'POST':
        student = Student()
        student.name = request.POST['name']
        student.roll = request.POST['roll']
        student.city = request.POST['city']
        # stu = Student(name=name, roll=roll, city=city)
        student.save()
        return redirect(home)
    return render(request, 'add.html')

def update(request,pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.roll = request.POST['roll']
        student.city = request.POST['city']
        student.save()
        return redirect(home)
    return render(request, 'update.html', {'student':student})



def delete(request,pk):
    stu = Student.objects.get(id=pk)
    stu.delete()
    return redirect(home)
    
# ListAPIView (generics view from DRF)
class Studentlistapiview(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentlistapiviewRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer




# GenericAPIView (mixins) from DRF (individual functions to CRUD)
class ListStudentGenericAPI(GenericAPIView, ListModelMixin ):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class CreateStudentGenericAPI(GenericAPIView, CreateModelMixin ):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class RetrieveStudentGenericAPI(GenericAPIView, RetrieveModelMixin ):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class UpdateStudentGenericAPI(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request , *args, **kwargs):
        return self.update(request, *args , **kwargs)

class DeleteStudentGenericAPI(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request , *args, **kwargs):
        return self.destroy(request, *args , **kwargs)

# GenericAPIView (mixins) from DRF Grouped
# when id(pk) is not required like in listview and creating of student model instance
class CLStudentGenericGrp(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# GenericAPIView (mixins) from DRF Grouped
# when id(pk) is required like in retrieve , update and deleting of student model instance
class RUDStudentGenericGrp(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    



# APIView  Create api with using DRF (Using views (Class Based Views)) 
class StudentAPIView(APIView):
    def get(self, request , pk=None, format=None):
        stu_id = pk
        if stu_id is not None:
            stu = Student.objects.get(id=stu_id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def put(self, request, pk, format=None):
        stu_id = pk
        stu = Student.objects.get(id=stu_id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)

    def patch(self, request, pk, format=None):
        stu_id = pk
        stu = Student.objects.get(id=stu_id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)

    def delete(self, request, pk ,format=None):
        stu_id = pk
        stu = Student.objects.get(id=stu_id)
        stu.delete()
        return Response({"msg":"{} is deleted successfully".format(stu)})



# API for Student model using Class based Views (viewsets)
class Student_api_cbv(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer





# # API for Student model using Class based Views (viewsets)
# class Student_api_cbv(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     # for a particular class
#     authentication_classes = [BasicAuthentication,]
#     permission_classes = [IsAuthenticated]

# # API for Student model using Class based Views (viewsets)
# class Student_api_cbv(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     # API for Student model using Class based Views (viewsets)
# class Student_api_cbv(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


#     # API for Student model using Class based Views (viewsets)
# class Student_api_cbv(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


#     # API for Student model using Class based Views (viewsets)
# class Student_api_cbv(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     # API for Student model using Class based Views (viewsets)
# class Student_api_cbv(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     # API for Student model using Class based Views (viewsets)
# class Student_api_cbv(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
