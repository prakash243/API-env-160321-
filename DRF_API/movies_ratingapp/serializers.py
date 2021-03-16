from rest_framework import serializers
from movies_ratingapp.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"