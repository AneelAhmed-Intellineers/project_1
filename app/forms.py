from django import forms
from django.core.exceptions import ValidationError


from .models import Student, Grade


class StudentForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = ('name', 'department','email', 'enrollment')

class ResultForm(forms.ModelForm):

    class Meta:

        model = Student

        fields = ('name', 'enrollment')