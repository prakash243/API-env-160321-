from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

#Register Student Viewsets with router
router.register('students', views.Student_api_cbv, basename='student' )

urlpatterns = [

    path('home/', views.home),
    path('home/add/', views.add, name='add'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),

    # (viewsets.ModelViewSet) from rest_framework import viewsets
    path('', include(router.urls)),

    # APIView (from rest_framework.views import APIView)
    path('studentAPIView/', views.StudentAPIView.as_view()),
    path('studentAPIView/<int:pk>', views.StudentAPIView.as_view()),

    # GenericAPIView (mixins) from DRF individually
    path('studentgenericapi/', views.ListStudentGenericAPI.as_view()),
    path('createstudentgenericapi/', views.CreateStudentGenericAPI.as_view()),
    path('retrievestudentgenericapi/<int:pk>', views.RetrieveStudentGenericAPI.as_view()),
    path('updatestudentgenericapi/<int:pk>', views.UpdateStudentGenericAPI.as_view()),
    path('deletestudentgenericapi/<int:pk>', views.DeleteStudentGenericAPI.as_view()),

    # GenericAPIView (mixins) Crud Grouped
    path('studentgenericgrp/', views.CLStudentGenericGrp.as_view()),
    path('studentgenericgrp/<int:pk>', views.RUDStudentGenericGrp.as_view()),

    # generics2
    path('studentlistapiview/', views.Studentlistapiview.as_view()),
    path('studentlistapiviewRUD/<int:pk>', views.StudentlistapiviewRUD.as_view()),
]
