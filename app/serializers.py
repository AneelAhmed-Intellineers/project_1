from .models import Student, Grade
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class StudentSerializer(serializers.ModelSerializer):
    class Meta:

        model = Student
        fields = ['name', 'email', 'department', 'enrollment']


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['name', 'enrollment', ]