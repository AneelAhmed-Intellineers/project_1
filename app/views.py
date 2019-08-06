from django.shortcuts import render, get_object_or_404,  redirect
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseBadRequest
from django.urls import reverse
from django.views.generic import FormView, TemplateView,DetailView,ListView
from django.template import loader
from .models import Student, Grade
from .forms import StudentForm, ResultForm
from django.contrib import messages
from django.views.generic.edit import FormView, CreateView
from django.views.generic.edit import CreateView



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
        return HttpResponseRedirect('/student/view_result/%s'%a)

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
    #queryset = Student.objects.filter(name='Martin')


class SearchResultView(ListView):
    context_object_name = 'student'
    def get_queryset(self):
        return Student.objects.filter(name=self.request.user)
    template_name = 'studentlist.html'