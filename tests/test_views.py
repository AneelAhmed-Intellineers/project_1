import pytest
import factory
from django.test import Client
from django.shortcuts import reverse
from http.client import responses

from app.views import detail,index,thanks
from app.models import Grade,Student
from app.forms import ResultForm, StudentForm
from app.factories import GradeFactory,StudentFactory


pytestmark = pytest.mark.django_db

class TestIndexViews:

    def setup_method(self):
        self.client = Client()


    def test_get_response(self):
        response = self.client.get('/student/student/')
        assert response.status_code == 200
        
    def test_form_validation(self):

        student_before = Student.objects.all().count()
        student = StudentFactory.create()
        response = self.client.post('/student/thanks/')
        student_total = Student.objects.all().count()

        
        assert response.status_code == 200
        assert student_before < student_total

    def test_form_invalidation(self):

        student_before = Student.objects.all().count()
        student = Student.objects.create(
        )
        student_dict = {'student':student}

        response = self.client.post(reverse('app:detail'), student_dict)
        student_total = Student.objects.all().count()
        assert response.status_code == 200
        assert student_before < student_total
    def test_create_result_request(self):

        grades = GradeFactory.create()
        student = StudentFactory.create(
            grade = grades
        )
        
        student_dict = {
            'student' : student
        }

        student_number = Student.objects.all().count()

        response = self.client.post('/student/thanks/', student_dict)
        assert response.status_code == 200
        assert student_number <= Student.objects.all().count()


class TestDetailView:

    def setup_method(self):
        self.client = Client()

    def test_get(self):

        response = self.client.get('/student/result/')
        assert response.status_code == 200

    def test_get_result(self):
    
        Student.objects.create(

            name = 'jhon',
            email = 'j@bb.com',
            department = 'chem',
            enrollment=' 2342',
            grade = Grade.objects.create(grade='2')
        )
    
        result_form={'name': 'jhon','enrollment':'2342'}
        response = self.client.post('/student/result/', result_form)
        assert response.status_code == 200

