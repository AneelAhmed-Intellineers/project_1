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



class IndexCreateView(CreateView):
    form_class = StudentForm
    template_name = 'forms.html'

    def get_absolute_url(self):
        return HttpResponseRedirect( reverse("app:detail", kwargs={"pk": self.pk}))

class CreateDetailView(DetailView):

    model = Student
    template_name =  'detailview.html'   
    pk_url_kwarg = 'pk'



class ResultCreateView(CreateView):
    form_class = ResultForm
    template_name = 'result.html'

    def get_absolute_url(self):
        return HttpResponseRedirect( reverse("app:resultview", kwargs={"enrollment":enrollment}))

class ResultDetailView(DetailView):
    model = Student
    template_name = 'resultview.html'
    pk_url_kwarg = 'enrollment'
    
    def get_object(self, queryset=None):
        return self.model.objects.get(enrollment=self.kwargs['enrollment'])


def thanks(response):

    return HttpResponse("Thankyou For using this Site.....")