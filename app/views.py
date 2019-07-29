from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.template import loader
from .models import Student, Grade
from .forms import StudentForm, ResultForm


def index(request):
    
    if request.method == 'POST':
            form = StudentForm(request.POST)
            if form.is_valid():
                    name = form.cleaned_data['name']
                    enrollment = form.cleaned_data['enrollment']
                    email = form.cleaned_data['email']
                    department = form.cleaned_data['department']
                    students = Student.objects.all()
                    flag = True
                    for std in students:
                            if std.enrollment == enrollment:
                                    flag = False
                                    print(flag)    
                    
                    context = {
                            'name': name,
                            'email': email,
                            'department': department,
                            'enrollment':enrollment,

                    }
                    if flag:
                        form.save()
                    template = loader.get_template('/home/aneel/Development/project_1/project_1/app/templates/thanks.html')
                    return HttpResponse(template.render(context, request))
    else:
        form = StudentForm()
        template = loader.get_template('/home/aneel/Development/project_1/project_1/app/templates/forms.html')
        return HttpResponse(template.render({'form':form}, request))
                



def detail(request):

        if request.method == 'POST':
                student = Student.objects.all()
                form = ResultForm(request.POST)
                for data in student:
                        if data.enrollment == request.POST.get('enrollment'):
                             name = data.name
                             enrollment = data.enrollment
                             email = data.email
                             department = data.department
                             grade = data.grade
                             context = {
                                'name': name,
                                'email': email,
                                'department': department,
                                'enrollment':enrollment,
                                'grade':grade
                                }

                             template = loader.get_template('/home/aneel/Development/project_1/project_1/app/templates/resultsummary.html')
                             return HttpResponse(template.render(context, request))   

        else:
            form = ResultForm
            return render(request, '/home/aneel/Development/project_1/project_1/app/templates/result.html', {'form' : form})

    


def thanks(request):

        return HttpResponse("Helllo0 Thankyou very mUch")