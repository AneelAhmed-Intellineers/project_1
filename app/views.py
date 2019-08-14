from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.views.generic import CreateView, ListView
from django.contrib import messages
from rest_framework import generics, mixins, viewsets
from .models import Student, Grade
from .serializers import StudentSerializer, ResultSerializer
from .forms import StudentForm
from rest_framework import views
from rest_framework.response import Response
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404

class StudentCreateView(CreateView):

    model = Student
    form_class = StudentForm
    template_name = 'forms.html'

    success_url = '/'

    def form_valid(self, form):
        return_statement = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS,('Thankyou Your request have been Registered.'))
        user = User.objects.create(
            username=form.cleaned_data['enrollment'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['enrollment'],
            is_active=True
        )
        

        self.object.user = user
        self.object.save()

        return return_statement

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

  
    def create(self, request, *args, **kwargs):
        serliazer = self.get_serializer(data=request.data)
        serliazer.is_valid(raise_exception=True)
        self.perform_create(serliazer)
        user = User.objects.create(
                username=serliazer.data['enrollment'],
                email=serliazer.data['email'],
                password=serliazer.data['enrollment'],
                is_active=True
            )
        student = Student.objects.get(enrollment=serliazer.data['enrollment'])
        student.user = user
        student.save()
        return HttpResponseRedirect('/api/student/')

    

class ResultView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = ResultSerializer
    
    def create(self, request, *args, **kwargs):
        serlializer = self.get_serializer(data=request.data)
        serlializer.is_valid()
        if serlializer.errors:
            user = authenticate(username=serlializer.data['enrollment'], password='abcd.1234')
            if user is not None:
                login(request, user)
                student = Student.objects.get(enrollment=serlializer.data['enrollment'])
                return Response(f'name:{student.name} Email:{student.email} Department:{student.department} enrollment:{student.enrollment} grade:{student.grade}')
        return Response("No Data Found..")


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)