from rest_framework import serializers
from .models import StudentDetails,ExamDetails


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = '__all__'


class ExamDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamDetails
        fields = '__all__'