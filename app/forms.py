from django import forms
from django.core.exceptions import ValidationError


from .models import Student, Grade


class StudentForm(forms.ModelForm):

    grade = forms.ModelChoiceField(queryset=Grade.objects.all(), label='Grade')

    class Meta:

        model = Student

        fields = ('name', 'department','email', 'enrollment','grade')