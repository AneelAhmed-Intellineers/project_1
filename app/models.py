from django.db import models
from django.urls import reverse



class Grade(models.Model):

    GRADE_CHOICES = (
        ("1", 1),
        ("1.5", 1.5),
        ("2", 2),
        ("2.5", 2.5),
        ("3", 3),
        ("3.5", 3.5),
        ("4",4)

    )

        
    grade = models.CharField(max_length=5, choices=GRADE_CHOICES, default='Not Yet Updated')


    def __str__(self):

        return str(self.grade)

class Student(models.Model):

    name = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50)
    department = models.CharField(max_length=50)
    enrollment = models.CharField(max_length=50, null=False, unique=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)
    
    def get_absolute_url(self):
        return ( reverse("app:resultview", kwargs={"enrollment": self.enrollment}))   

    def __str__(self):

        return self.name
        


    