from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.views.generic import CreateView, ListView
from django.contrib import messages
from rest_framework import generics, mixins, viewsets
from .models import Student, Grade
from .serializers import StudentSerializer, ResultSerializer
from .forms import StudentForm
from rest_framework import views
from  rest_framework.response import Response
class StudentCreateView(CreateView):

    model = Student
    form_class = StudentForm
    template_name = 'forms.html'

    success_url = '/'

    def form_valid(self, form):
        return_statement = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS,('Thankyou Your request have been Registered.'))

        return return_statement

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    
    """def get_queryset(self):
        self.request.user --> Entrollment number

        return super().get_queryset().get(enrollment_numb)"""



class ResultView(viewsets.ModelViewSet):
    queryset = Student.objects.none()
    serializer_class = ResultSerializer
    
    def create(self, request, *args, **kwargs):
        serlializer = self.get_serializer(data=request.data)
        print ("Hello..........")
        serlializer.is_valid()
        print ("Hello....")
        if serlializer.errors:
            for student in Student.objects.all():
                if student.enrollment == serlializer.data['enrollment']:
        
                    return Response({'Name:':student.name, 'Department':student.department, 'Email:':student.email,})
        
        return Response("No Data Found..")