from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Register Student Viewsets with router
router = DefaultRouter()
router.register('viewsets', views.Student_viewsets, basename='student')


urlpatterns = [
    path('', include(router.urls)),
    
]
