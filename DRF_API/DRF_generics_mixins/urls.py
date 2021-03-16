from django.urls import path, include
from . import views


urlpatterns = [
    path('mixins/', views.LC_Student_mixins.as_view()),
    path('mixins/<int:pk>', views.RUD_Student_mixins.as_view()),
]