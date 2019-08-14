import pytest
import factory
from django.test import Client
from django.shortcuts import reverse
from http.client import responses

from app.views import StudentModelViewSet, ResultView
from app.models import Grade, Student
from app.factories import GradeFactory, StudentFactory

pytestmark = pytest.mark.django_db

class TestStudentModelViewSet:

    def setup_method(self):

        self.client = Client()

    def test_get(self):

        response = self.client.get('/api/student/')
        assert response.status_code == 200

    def test_invalid_data(self):

        student_before = Student.objects.all().count()
        student = {

            'name':'jack',
        }
        response = self.client.post('/api/student/', student)
        
        assert student_before == Student.objects.all().count()
        assert response.status_code == 400
    def test_valid_data(self):
        
        student_before = Student.objects.all().count()
        student = factory.build(dict, FACTORY_CLASS=StudentFactory)
        response = self.client.post('/api/student/', student)

        assert Student.objects.all().count() > student_before


class TestResultView:

    def setup_method(self):

        self.client = Client()

    def test_get(self):

        response = self.client.get('/api/student_result/')
        assert response.status_code == 200

    def test_invalid_login_data(self):

        student = {

            'enrollment':'2323'
        }

        response = self.client.post('/api/student_result', student)
        assert response.status_code == 301
        assert response.context == None

    def test_valid_login_data(self):

        student = factory.build(dict, FACTORY_CLASS=StudentFactory)
        grade = Grade.objects.create()
        grade.grade = '2'
        response_for_student = self.client.post('/api/student/',student)
        Student.objects.get(enrollment=student['enrollment']).grade=grade    
        student_login = {

            'name':student['name'],
            'enrollment':student['enrollment'],
        }

        response = self.client.post('/api/student_result/', student_login)

        assert response.status_code == 200


