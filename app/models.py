from django.db import models



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

    name = models.CharField(max_length=30) 
    email = models.EmailField(max_length=30)
    department = models.CharField(max_length=40)
    enrollment = models.CharField(max_length=10, null=False)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)


    def __str__(self):

        return self.name
        


    