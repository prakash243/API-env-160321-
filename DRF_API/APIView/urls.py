from django.urls import path, include
from . import views



urlpatterns = [
    path('APIView/', views.Student_APIView.as_view()),
    path('APIView/<int:pk>', views.Student_APIView.as_view()),
    
]
