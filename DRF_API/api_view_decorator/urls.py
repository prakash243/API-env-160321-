from django.urls import path, include
# from movies_ratingapp import views
from api_view_decorator import views


urlpatterns = [

    # @api_view (from rest_framework.decorators import api_view)
    path('apiview/', views.student_api_view),
    path('apiview/<int:pk>', views.student_api_view),
   
]
