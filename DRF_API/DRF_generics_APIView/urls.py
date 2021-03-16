from django.urls import path, include
from . import views


urlpatterns = [
    path('genericsapiview/', views.LC_Student_APIView.as_view()),
    path('genericsapiview/<int:pk>', views.RUD_Student_APIView.as_view()),
]