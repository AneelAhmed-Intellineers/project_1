from app.models import Student, Grade
import pytest
from app.factories import GradeFactory, StudentFactory

pytestmark = pytest.mark.django_db

def test_student_without_grade():

    student = Student()
    student.name = 'jack'
    assert student.grade is None

def test_student_with_grade():

    grades = GradeFactory.create()
    student = StudentFactory.create(
        grade = grades
    )
    assert student.grade is not None

def test_student_with_id():

    student = StudentFactory.create()
    assert student.id is not None

def test_student_str():

    student = Student.objects.create(
        name = 'jack'
    )
    assert str(student) == student.name

def test_grade_id_none():

    grades = Grade()
    grades.grade='2'

    assert grades.id is None

def test_grade_id():

    grade = Grade.objects.create()
    assert grade.id is not None
    
def test_grade_null():
    with pytest.raises(AssertionError):
        grade = Grade.objects.create()
        assert grade.grade is None