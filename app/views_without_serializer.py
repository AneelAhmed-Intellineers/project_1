from django.shortcuts import render, get_object_or_404,  redirect
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseBadRequest
from django.urls import reverse
from django.views.generic import FormView, TemplateView,DetailView,ListView
from django.template import loader
from .models import Student, Grade
from .forms import StudentForm, ResultForm
from django.contrib import messages
from django.views.generic.edit import FormView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .serializers import StudentSerializer
from rest_framework import viewsets

class StudentRegisterationCreateView(CreateView):
    form_class = StudentForm
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse ("app:student_detail", args=(self.object.id,))
    

class StudentDetailView(DetailView):

    model = Student
    template_name =  'detailview.html'   
    pk_url_kwarg = 'pk'
    

class ResultFormView(FormView):
    
    form_class = ResultForm
    template_name = 'result.html'

    def form_invalid(self, form):
        a = form.data['enrollment']
        return HttpResponseRedirect('/view_result/%s'%a)

    def form_valid(self, form):

        return HttpResponse("No Data Found under This enrollment number..")
    
class ResultDetailView(DetailView):
    model = Student
    template_name = 'resultview.html'
    pk_url_kwarg = 'enrollment'

    def get_object(self):
        obj = self.model.objects.get(enrollment=self.kwargs['enrollment'])
        return obj


def thanks(response):

    return HttpResponse("Thankyou For using this Site.....")


class StudentListView(ListView):
    context_object_name = 'student'
    template_name = 'studentlist.html'
    model = Student
    

class SearchResultView(ListView):
    context_object_name = 'student'
    template_name = 'studentlist.html'
    
    def get_queryset(self):
        return Student.objects.filter(name=self.request.user)
    

class CreateStudentUpdate(FormView):

    form_class = ResultForm
    template_name = 'student_update.html'

    def form_invalid(self, form):
        enrol = form.data['enrollment']
        return HttpResponseRedirect('/student_update/%s'%enrol)

    def form_valid(self, form):

        return HttpResponse("No Data Found under This enrollment number..")

class StudentUpdateView(UpdateView):

    model = Student
    template_name = 'student_update_form.html'
    form_class = StudentForm

    def get_object(self):

        return self.model.objects.get(enrollment=self.kwargs['enrollment'])

    def get_success_url(self):

        return reverse ("app:student_detail", args=(self.object.id,))

class CreateStudentDelete(FormView):

    form_class = ResultForm
    template_name = 'student_update.html'

    def form_invalid(self, form):
        enrol = form.data['enrollment']
        return HttpResponseRedirect('/student_delete/%s'% enrol)
    def form_valid(self, form):
        return HttpResponse("No Data Found under this enrollment number..")

class StudentDeleteView(DeleteView):

    model = Student
    template_name = 'delete_student.html'

    def get_object(self):

        return self.model.objects.get(enrollment=self.kwargs['enrollment'])

    def get_success_url(self):
        return reverse("app:deleted_data")

    def deleted_data(self):
        return HttpResponse("You'r Data Have been Deleted from our result Database..")