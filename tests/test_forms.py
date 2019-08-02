import pytest
from app.forms import StudentForm, ResultForm
from app.models import Student, Grade
from app.factories import GradeFactory, StudentFactory

pytestmark = pytest.mark.django_db


def test_studentform_init():
    form =  StudentForm()
    assert form is not None


def test_form_valid():

    form = StudentForm(data={
        'name':'jack',
        'email':'jack@hh.com',
        'department':'chemistry',
        'enrollment':'2421',
        'grade':GradeFactory.create()
    })

    assert form.is_valid()

def test_form_invalid():

    form = StudentForm(data={
        'name':'jack',
        'email':'jack@hh.com',
        'department':'chemistry',

    })

    assert form.is_valid() == False

def test_deprtmant_entry():
    form = StudentForm(data={
        'name':'andy',
        'email':'andy@jj.com',
        'department':'phy',
        'enrollment':'2333',

    })

    assert form.is_valid() == False