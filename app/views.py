from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Student, Grade
from .forms import StudentForm

def index(request):
    flag = 0
    grade = Grade("")
    if request.method == 'POST':
        enrollment = request.POST.get('enrollment_field')
        data = Student.objects.all()
        count = flag
        for student in data:
            print (count)
            if enrollment == student.enrollment is True:
                count = 1
                flag = count
                print(count)
                return HttpResponse("Your Data already Found in our DataPool Please use your Key to view Result or wait..")
        if flag == 0:
            data = Student()
            data.name = request.POST.get('name_field')
            data.email = request.POST.get('email_field')
            data.grade = grade
            data.save()

            return  render(request, '/home/aneel/Development/project_1/project_1/app/templates/index.html')

    else:
        return  render(request, '/home/aneel/Development/project_1/project_1/app/templates/index.html')

def detail(request, student_id):
    data = Student.objects.all()
    flage = False
    for student in data:
        if student_id == student.id:

            string = student.grade
            flage = True
            return HttpResponse("Your grade is %s:" % string)
    if flage == False:
        return HttpResponse("Please Enter correct Data or Your result May have not yet Updated.....")

