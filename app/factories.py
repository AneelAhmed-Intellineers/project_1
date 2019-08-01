from .models import Grade, Student
import factory



class GradeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Grade
    
    grade = factory.Faker('month')



class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    name = factory.Faker('name')
    email = factory.Faker('email')
    department = factory.Faker('job')
    enrollment = factory.Faker('ssn')
    
