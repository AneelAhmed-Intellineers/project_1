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
        
        response = self.client.get('')
        assert response.status_code == 200

    def test_invalid_form(self):

        student_before = Student.objects.all().count()
        student = {

            'name': 'jack',
        }
        response = self.client.post('', student)
        assert response.status_code == 200 # 404 with simple class view
        assert student_before == Student.objects.all().count()

    def test_Valid_form(self):

        student_before = Student.objects.all().count()
        student = factory.build(dict, FACTORY_CLASS=StudentFactory)
        response = self.client.post('', student)
        student_after = Student.objects.all().count()
        assert response.status_code == 302 # 200 with simple class view
        assert student_before < student_after

    def test_two_entries(self):

        student = factory.build(dict,  FACTORY_CLASS=StudentFactory)
        response_one = self.client.post('', student)
        response_two = self.client.post('', student)

        assert Student.objects.all().count() == 1
    
    def test_thanks(self):
        with pytest.raises(AssertionError):
            response = self.client.get('/thanks/')
            assert response.content == 'Helllo0 Thankyou very mUch'


class TestResultView:


    def setup_method(self):
        self.client = Client()

    def test_get(self):

        response = self.client.get('/search/')
        assert response.status_code == 200

    def test_invalid_form(self):

        student = {

            'enrollment':'124'
        }
        response = self.client.post('/search/', student)

        assert response.status_code == 302 # 400 with simple class view 

    def test_valid_form(self):
        with pytest.raises(AssertionError):
            student = {

                'name':'martin',
                'enrollment':'1233'
            }
            response = self.client.post('/search/', student)

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

        response_for_student= self.client.post('', student)

       
        for students in Student.objects.all():
            if students.enrollment == student['enrollment']:
                students.grade = grades

        response = self.client.get(f'/view_result/{enrol}')
        student_after = Student.objects.all().count()
        assert response.status_code == 200
        assert response_for_student.status_code == 302 # It was 200 in testing views with class (Views) only
        assert student_before < student_after 
        assert Student.objects.all().count() == 1

    def test_update_student(self):

        student = factory.build(dict, FACTORY_CLASS=StudentFactory)
        response = self.client.post('', student)
        assert Student.objects.all().count() == 1


class TestStudentUpdateView:

    def setup_method(self):
        self.client = Client()

    def test_student_update(self):

        student = factory.build(dict, FACTORY_CLASS=StudentFactory)
        response = self.client.post('', student)
        student_update = {

            'name':student['name'],
            'enrollment':student['enrollment'],
        }
        
        student_new_data = {

            'name':student['name'],
            'email':student['email'],
            'department':'Micro-Biology',
            'enrollment':student['enrollment'],
        }

        enrol = student_update['enrollment']      
        response_update = self.client.post('/student_update/', student_update)
        response_update_redirect = self.client.post(f'/student_update/{enrol}',student_new_data)
        response_redirect = self.client.get(f'/{1}/')
        
        assert Student.objects.get(id=1).department == student_new_data['department']

        for students in Student.objects.all():
            if students.pk == 1:
                assert students.department == student_new_data['department']

        assert Student.objects.all().count() == 1
         
    def test_student_update_invalid_data(self):
        with pytest.raises(AssertionError):
            student_update = {
                
                'name': 'jack',
                'enrollment':'1234'
            }

            response = self.client.post('/student_update/', student_update)
            assert response.content == 'No Data Found under This enrollment number..'


class TestStudentDeleteView:

    def setup_method(self):
        self.client = Client()

    def test_delete_student(self):

        student = factory.build(dict, FACTORY_CLASS=StudentFactory)
        response = self.client.post('', student)
        student_before = Student.objects.all().count()
        student_delete = {

            'name':student['name'],
            'enrollment':student['enrollment']
        }

        enrol = student_delete['enrollment']
        response_for_delete_request = self.client.post('/student_delete/', student_delete)
        response_delete = self.client.post(f'/student_delete/{enrol}')
        student_after = Student.objects.all().count()
        assert student_before > student_after
        assert response_delete.status_code == 302

    def test_delete_student_invalid(self):

        student = {

            'name': 'Jhon',
            'enrollment':'232',
        }

        response_delete = self.client.post(f'/student_delete/', student)
        response =  str(response_delete.content)
        assert response.find('No Data Found under this enrollment')

    def test_deleted_response(self):

        response = self.client.get('/student_delete/deleted/')
        assert response.status_code == 200 