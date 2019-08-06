import pytest
import factory
from django.test import Client
from django.shortcuts import reverse
from http.client import responses

from app.views import ResultDetailView,ResultFormView,StudentDetailView,StudentRegisterationCreateView 
from app.models import Grade,Student
from app.forms import ResultForm, StudentForm
from app.factories import GradeFactory,StudentFactory


pytestmark = pytest.mark.django_db

class TestIndexViews:

    def setup_method(self):

        self.client = Client()

    def test_get(self):
        
        response = self.client.get('/student/')
        assert response.status_code == 200

    def test_invalid_form(self):

        student_before = Student.objects.all().count()
        student = {

            'name': 'jack',
        }
        response = self.client.post('/student/', student)
        assert response.status_code == 200 # 404 with simple class view
        assert student_before == Student.objects.all().count()

    def test_Valid_form(self):

        student_before = Student.objects.all().count()
        student = factory.build(dict, FACTORY_CLASS=StudentFactory)
        response = self.client.post('/student/', student)
        student_after = Student.objects.all().count()
        assert response.status_code == 302 # 200 with simple class view
        assert student_before < student_after

    def test_two_entries(self):

        student = factory.build(dict,  FACTORY_CLASS=StudentFactory)
        response_one = self.client.post('/student/', student)
        response_two = self.client.post('/student/', student)

        assert Student.objects.all().count() == 1
    
    def test_thanks(self):
        with pytest.raises(AssertionError):
            response = self.client.get('/student/thanks/')
            assert response.content == 'Helllo0 Thankyou very mUch'


class TestResultView:


    def setup_method(self):
        self.client = Client()

    def test_get(self):

        response = self.client.get('/student/result/')
        assert response.status_code == 200

    def test_invalid_form(self):

        student = {

            'enrollment':'124'
        }
        response = self.client.post('/student/result/', student)

        assert response.status_code == 302 # 400 with simple class view 

    def test_valid_form(self):
        with pytest.raises(AssertionError):
            student = {

                'name':'martin',
                'enrollment':'1233'
            }
            response = self.client.post('/student/result/', student)

            assert response.status_code == 200
            assert response.content == "'No Data Found under This enrollment number.."

    def test_result_output(self):

        student_before = Student.objects.all().count()
        student = factory.build(dict, FACTORY_CLASS=StudentFactory)
        grades = Grade.objects.create()
        grades.grade = '2'
       
        student_result_form = {

            'name':student['name'],
            'enrollment':student['enrollment'],
        }
        enrol =  student['enrollment']

        response_for_student= self.client.post('/student/', student)

       
        for students in Student.objects.all():
            if students.enrollment == student['enrollment']:
                students.grade = grades

        response = self.client.get(f'/student/view_result/{enrol}')
        student_after = Student.objects.all().count()
        assert response.status_code == 200
        assert response_for_student.status_code == 302 # It was 200 in testing views with class (Views) only
        assert student_before < student_after 
        assert Student.objects.all().count() == 1
