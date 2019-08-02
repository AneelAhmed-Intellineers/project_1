from django import forms
from django.core.exceptions import ValidationError


from .models import Student, Grade


class StudentForm(forms.ModelForm):

    def clean_department(self):
        data = self.cleaned_data['department']

        if len(data) <= 5:
            raise ValidationError("The Department You entered is too Short.")
        return data    

    
    
    class Meta:

        model = Student
        fields = ('name', 'department','email', 'enrollment')

        

class ResultForm(forms.ModelForm):

    class Meta:

        model = Student
        fields = ('name', 'enrollment')