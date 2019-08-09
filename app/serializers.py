from .models import Student, Grade
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Student
        fields = ['name', 'email', 'department', 'enrollment','id', 'grade']



class GradeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Grade
        fields = ['grade']

class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['name', 'enrollment', ]