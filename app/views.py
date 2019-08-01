from django.shortcuts import render, get_object_or_404,  redirect
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseBadRequest
from django.urls import reverse
from django.views import generic,View
from django.template import loader
from .models import Student, Grade
from .forms import StudentForm, ResultForm
from django.contrib import messages
from django.views.generic.edit import FormView, CreateView


# TODO: Create CBVs

class IndexCreateView(View):
        model = Student
        form_class = StudentForm
        template_name = '/home/aneel/Development/project_1/project_1/app/templates/forms.html'

        def get(self, request, *args, **kwargs):

                form = self.form_class
                return render(request, self.template_name, {'form': form})

        def post(self, request, *args, **kwargs):

                form  = self.form_class(request.POST)
                if form.is_valid():
                        context = {
                            'name': form.cleaned_data['name'],
                            'email': form.cleaned_data['email'],
                            'department': form.cleaned_data['department'],
                            'enrollment':form.cleaned_data['enrollment'],

                    }     
                        flag = True
                        for students in Student.objects.all():
                                if students.enrollment == form.cleaned_data['enrollment']:
                                        flag = False
                        if flag is True:
                                form.save()
                        template = loader.get_template('/home/aneel/Development/project_1/project_1/app/templates/thanks.html')
                        return HttpResponse(template.render(context, request))

                else :
                        return HttpResponse("The Data You Tryied to Enter is Already Register.. OR in Invalid")
                


        def thanks(request):
                return HttpResponse("Helllo0 Thankyou very mUch")

class ResultcreateView(View):

        form_class = ResultForm
        template_name = '/home/aneel/Development/project_1/project_1/app/templates/result.html'

        def get(self, request, *args, **kwargs):

                form = self.form_class
                return render(request, self.template_name, {'form': form})

        def post(self, request, *args, **kwargs):
                
                form = self.form_class(request.POST)
                if form.is_valid():
                        flag = True
                        for obj in Student.objects.all():
                                if obj.enrollment == form.cleaned_data['enrollment']:
                                        flag = False
                                        context = {
                                                'name':obj.name,
                                                'email':obj.email,
                                                'department':obj.department,
                                                'enrollment':obj.enrollment,
                                                'grade':obj.grade
                                        }
                                        
                                        template = loader.get_template('/home/aneel/Development/project_1/project_1/app/templates/resultsummary.html')
                                        return HttpResponse(template.render(context, request))   

                        if flag is True:

                                return HttpResponse("NO Student Registered With That Enrollment....")

                return HttpResponseBadRequest()