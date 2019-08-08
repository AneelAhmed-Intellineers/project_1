from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.views.generic import CreateView, ListView
from django.contrib import messages
from rest_framework import generics, mixins, viewsets
from .models import Student
from .serializers import StudentSerializer
from .forms import StudentForm


class StudentCreateView(CreateView):

    model = Student
    form_class = StudentForm
    template_name = 'forms.html'

    success_url = '/'

    def form_valid(self, form):
        return_statement = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS,('Thankyou Your request have been Registered.'))

        return return_statement

class StudentViews(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_student(self):
        return Student.object.get(pk=self.kwargs['id'])

    def get_queryset(self):

        student = self.get_student
        return self.queryset

