from app.models import Student, Grade
import pytest


@pytest.mark.django_db
class TestModels:

    def test_str_(self):
        grade=Grade()
        grade.grade='23'
        student = Student()
        student.name = 'Neel'
        student.email = 'a@bh.com'
        student.department = 'Medicine'
        student.enrollment='4213'
        student.grade=grade

        assert student.grade == None