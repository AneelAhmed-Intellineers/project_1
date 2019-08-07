from django.urls import path
from .import views


app_name = 'app'
urlpatterns = [
    path('', views.student_list, name='student_list'),
    path ('<int:pk>/', views.student_detail, name='student_detail')
]
